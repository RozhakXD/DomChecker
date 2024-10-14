# 🛡️ **DomChecker**
![DomChecker](https://github.com/user-attachments/assets/685cfbc7-6914-434f-a9d0-40481099fcfa)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Requests](https://img.shields.io/badge/Requests-2.31-red)
![Threading](https://img.shields.io/badge/ThreadPoolExecutor-30_workers-yellow)

**DomChecker** adalah alat yang memudahkan Anda memeriksa apakah suatu hostname atau domain memberikan response code HTTP 200 (OK). Alat ini dirancang untuk efisiensi, multi-threading, dan handling error otomatis. Dengan menggunakan DomChecker, Anda dapat memindai daftar domain dari file teks dan menyimpan hasilnya dalam format JSON.

## 📋 Fitur Utama
- Memindai secara otomatis daftar domain dari file apa pun dengan pola yang tidak beraturan.
- Multi-threading untuk pemrosesan cepat (menggunakan 30 worker).
- Handling error otomatis (connection error, timeout, dll.).
- Tampilan konsol lebih rapi dan elegan dengan Rich library.
- Hasil disimpan dalam file **JSON**.
- Protokol **HTTP/HTTPS** dapat dipilih pengguna.

## 🚀 Instalasi
1. Clone Repository dari GitHub
    ```bash
    git clone https://github.com/RozhakXD/DomChecker.git
    cd DomChecker
    ```
2. Install Dependensi yang Dibutuhkan
    ```bash
    pip install -r requirements.txt
    ```
3. Menjalankan DomChecker
    ```bash
    python Run.py
    ```

## 📝 Contoh Penggunaan
1. Setelah menjalankan program, masukkan nama file yang berisi daftar domain:
    ```scss
    [MASUKAN] Nama File: Penyimpanan/Example.txt
    ```
2. Pilih protokol yang ingin digunakan (**HTTP** atau **HTTPS**):
    ```scss
    [MASUKAN] Pakai (HTTPS/HTTP): HTTPS
    ```
3. Hasil yang valid (response 200) akan disimpan di `Temporary/200.json`:
    ```json
    [
        "https://web.whatsapp.com",
        "https://api.whatsapp.com",
        "https://faq.whatsapp.com",
    ]
    ```

## 🛠️ Struktur Proyek
```bash
DomChecker/
│
├── Run.py        # Kode utama DomChecker
├── README.md     # Dokumentasi ini
└── Temporary/    # Folder untuk menyimpan hasil JSON
```

## ⚡ Teknologi yang Digunakan
- **Requests Library** – Untuk mengirim HTTP request.
- **ThreadPoolExecutor** – Untuk menjalankan proses secara paralel.
- **Python**
- **Rich Library** – Untuk memperindah tampilan konsol.

## 📌 Catatan Penting
- File input harus berisi daftar domain atau hostname (berantakan atau terstruktur).
- **Timeout** telah diset ke **10 detik** untuk menghindari request yang menggantung.
- Hanya domain dengan status **200** yang disimpan di JSON output.

## Tangkapan Layar
![FunPic_20241014](https://github.com/user-attachments/assets/22021b15-61ea-4491-ab2a-c0e5e1f9b1e5)

## 🧑‍💻 Kontribusi
Kontribusi sangat terbuka! Silakan fork repository ini dan buat pull request jika Anda menemukan bug atau ingin menambahkan fitur baru.

## ⚖️ Lisensi
Proyek ini dilisensikan di bawah lisensi **MIT**.
