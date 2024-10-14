from concurrent.futures import ThreadPoolExecutor, as_completed
import requests, os, json, re
from rich.console import Console
from rich import print


def Load_Domain_From_Files(file_path: str):
    valid_domain = set()
    domain_regex = re.compile(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b")
    try:
        with open(f"{file_path}", "r") as reads:
            for line in reads:
                domains = domain_regex.findall(line)
                valid_domain.update(domains)
            return valid_domain
    except FileNotFoundError:
        print(
            f"[bold white][[bold red]ERROR[bold white]][bold red] File '{file_path}' Tidak Ditemukan!"
        )
        return []


def Scanning_Domain(domain: str, valid_results: list):
    try:
        response = requests.get(
            f"{domain}",
            allow_redirects=False,
            timeout=10,
            verify=domain.startswith("https://"),
        )
        status_code = response.status_code
        if status_code == 200:
            print(f"[bold white][[bold green]200[bold white]][bold green] {domain}")
            valid_results.append(f"{domain}")
        else:
            print(
                f"[bold white][[bold yellow]{status_code}[bold white]][bold yellow] {domain}"
            )
    except requests.exceptions.ConnectionError:
        print(
            f"[bold white][[bold red]ERROR[bold white]][bold red] {domain} - Connection Error"
        )
    except requests.exceptions.Timeout:
        print(f"[bold white][[bold red]ERROR[bold white]][bold red] {domain} - Timeout")
    except requests.exceptions.RequestException as e:
        print(f"[bold white][[bold red]ERROR[bold white]][bold red] {domain} - {e}")


def Save_Results(valid_results: list, output_file="Temporary/200.json"):
    try:
        with open(f"{output_file}", "w") as save:
            json.dump(valid_results, save, indent=4)
        print(
            f"\n[bold white][[bold green]INFO[bold white]] Hasil Disimpan Ke[bold green] {output_file}[bold white]!"
        )
    except IOError as e:
        print(
            f"\n[bold white][[bold red]ERROR[bold white]][bold red] Gagal Menyimpan Hasil Ke {output_file} - {e}!"
        )


def Main(file_path: str, protocol: str):
    domains = Load_Domain_From_Files(file_path)

    if not domains:
        print(
            "[bold white][[bold red]INFO[bold white]][bold red] Tidak Ada Domain Valid Untuk Diproses!"
        )
        return
    else:
        print(
            f"[bold white][[bold green]INFO[bold white]] Jumlah Domain:[bold green] {len(domains)}\n"
        )
    valid_results = []

    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = {
            executor.submit(
                Scanning_Domain, f"{protocol}://{domain}", valid_results
            ): domain
            for domain in domains
        }

        for future in as_completed(futures):
            domain = futures[future]
            try:
                future.result()
            except Exception as e:
                print(
                    f"[bold white][[bold red]ERROR[bold white]][bold red] Gagal Memeriksa {domain} - {e}"
                )
    Save_Results(valid_results=valid_results)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print(
        r"""[bold red] _____                   _____ _               _             
[bold red]|  __ \                 / ____| |             | |            
[bold red]| |  | | ___  _ __ ___ | |    | |__   ___  ___| | _____ _ __ 
[bold red]| |  | |/ _ \| '_ ` _ \| |    | '_ \ / _ \/ __| |/ / _ \ '__|
[bold red]| |__| | (_) | | | | | | |____| | | |  __/ (__|   <  __/ |   
[bold white]|_____/ \___/|_| |_| |_|\_____|_| |_|\___|\___|_|\_\___|_|   
"""
    )  # Coded by Rozhak
    file_name = (
        Console()
        .input("[bold white][[bold green]MASUKAN[bold white]][bold white] Nama File: ")
        .strip()
    )
    protocol = Console().input(
        "[bold white][[bold green]MASUKAN[bold white]][bold white] Pakai (HTTPS/HTTP): "
    )
    if protocol.lower() == "http":
        Main(file_path=file_name, protocol="http")
    else:
        Main(file_path=file_name, protocol="https")