# Analisis Data Bike Sharing

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis pola dan tren penggunaan layanan penyewaan sepeda (_Bike Sharing_) berdasarkan berbagai faktor, seperti waktu, musim, kondisi cuaca, dan jenis pengguna.

Analisis dilakukan untuk memperoleh informasi mengenai perilaku penyewaan sepeda serta faktor-faktor yang memengaruhi jumlah penyewaan. Hasil analisis kemudian disajikan melalui dashboard interaktif menggunakan Streamlit agar informasi lebih mudah dipahami.

## Dataset

Dataset yang digunakan dalam proyek ini adalah **Bike Sharing Dataset**, yang terdiri dari dua file utama:

- `day.csv`: Berisi data penyewaan sepeda berdasarkan hari.
- `hour.csv`: Berisi data penyewaan sepeda berdasarkan jam.

Dataset mencakup beberapa variabel, antara lain tanggal, musim, kondisi cuaca, suhu, kelembapan, kecepatan angin, jumlah pengguna kasual, jumlah pengguna terdaftar, dan total penyewaan sepeda.

Data `hour.csv` juga digunakan sebagai dasar pengolahan untuk menghasilkan `main_data.csv`, yang menjadi sumber data dashboard.

## Pertanyaan Analisis

Proyek ini berfokus pada beberapa pertanyaan analisis berikut:

1. Bagaimana perubahan jumlah penyewaan sepeda dari waktu ke waktu?
2. Pada jam berapa jumlah penyewaan sepeda mencapai titik tertinggi?
3. Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?
4. Bagaimana hubungan kondisi cuaca dengan aktivitas penyewaan sepeda?
5. Bagaimana perbandingan jumlah pengguna kasual dan pengguna terdaftar?

## Struktur Proyek

```text
Submission/
├── data/
│   ├── day.csv
│   └── hour.csv
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── requirements.txt
├── notebook.ipynb
├── README.md
├── url.txt
└── .gitignore
```

**Keterangan:**

- `data/`: Menyimpan dataset mentah.
- `dashboard.py`: File utama untuk menjalankan dashboard Streamlit.
- `main_data.csv`: Dataset hasil pengolahan yang digunakan oleh dashboard.
- `requirements.txt`: Daftar library dan dependensi proyek.
- `notebook.ipynb`: Notebook untuk proses analisis data.
- `README.md`: Dokumentasi proyek.
- `url.txt`: Berisi tautan dashboard online.
- `.gitignore`: Mengatur file dan folder yang tidak perlu diunggah ke GitHub.

## Tools dan Library

Beberapa tools dan library yang digunakan dalam proyek ini adalah:

- **Python**: Bahasa pemrograman utama untuk proses analisis data.
- **Pandas**: Mengolah dan memanipulasi data.
- **NumPy**: Melakukan operasi numerik.
- **Matplotlib**: Membuat visualisasi data.
- **Seaborn**: Membuat visualisasi statistik.
- **Plotly**: Membuat visualisasi data interaktif.
- **Streamlit**: Mengembangkan dashboard interaktif.
- **Google Colab**: Lingkungan untuk melakukan analisis data.

## Cara Menjalankan Dashboard

Ikuti langkah-langkah berikut untuk menjalankan dashboard secara lokal.

### 1. Clone Repository

Buka terminal atau PowerShell, kemudian jalankan:

```bash
git clone https://github.com/epipachy/bike-sharing-dashboard.git
```

### 2. Masuk ke Direktori Proyek

```bash
cd bike-sharing-dashboard
```

Pastikan terminal berada di direktori yang sama dengan file `dashboard.py` dan `requirements.txt`.

### 3. Membuat Virtual Environment

Buat virtual environment menggunakan perintah:

```bash
python -m venv .venv
```

### 4. Mengaktifkan Virtual Environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 5. Menginstal Dependensi

Pastikan virtual environment sudah aktif dan terminal berada di direktori proyek yang berisi `requirements.txt`.

Kemudian jalankan:

```bash
python -m pip install -r requirements.txt
```

### 6. Menjalankan Dashboard

Jalankan aplikasi Streamlit menggunakan perintah:

```bash
streamlit run dashboard.py
```

Dashboard akan terbuka secara otomatis melalui browser. Jika tidak terbuka, akses alamat lokal yang ditampilkan pada terminal.

### 7. Pengujian Dashboard

Setelah dashboard berhasil dijalankan, lakukan pengujian dengan memastikan:

- Statistik penyewaan sepeda berhasil ditampilkan.
- Seluruh grafik dan visualisasi muncul dengan benar.
- Filter dan fitur interaktif dapat digunakan.
- Perubahan filter menghasilkan visualisasi yang sesuai.

## Dashboard Interaktif

Dashboard dikembangkan menggunakan Streamlit dan menyajikan beberapa informasi utama, yaitu:

- Statistik total penyewaan sepeda.
- Tren penyewaan sepeda berdasarkan tanggal.
- Distribusi penyewaan berdasarkan jam.
- Perbandingan penyewaan berdasarkan musim.
- Perbandingan penyewaan berdasarkan kondisi cuaca.
- Perbandingan pengguna kasual dan pengguna terdaftar.

**Link Dashboard Online:**

https://bike-sharing-dashboard-gv2mrowv3xrtp9kwdlch8x.streamlit.app/

## Kesimpulan

Melalui proyek ini, dilakukan analisis terhadap pola penyewaan sepeda berdasarkan faktor waktu, musim, kondisi cuaca, dan karakteristik pengguna. Hasil analisis disajikan dalam bentuk visualisasi dan dashboard interaktif untuk membantu memahami tren serta karakteristik penggunaan layanan penyewaan sepeda.
