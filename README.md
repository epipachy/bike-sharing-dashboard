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

Pertanyaan Analisis

Proyek ini berfokus pada beberapa pertanyaan analisis berikut:
1. Bagaimana tren penyewaan sepeda dari waktu ke waktu, dan bagaimana informasi tersebut dapat membantu perencanaan kebutuhan layanan?
2. Bagaimana perbedaan pola penyewaan sepeda pada setiap jam antara working day dan non-working day, dan kapan penyedia layanan perlu meningkatkan ketersediaan sepeda?
3. Bagaimana rata-rata penyewaan sepeda pada setiap musim, dan bagaimana informasi tersebut dapat digunakan untuk merencanakan ketersediaan armada?
4. Bagaimana hubungan kondisi cuaca dengan rata-rata jumlah penyewaan sepeda, dan bagaimana informasi tersebut dapat membantu mengantisipasi perubahan permintaan?
5. Bagaimana rata-rata penyewaan sepeda berbeda setiap bulan?
6. Bagaimana perbandingan jumlah penyewaan oleh pengguna kasual dan pengguna terdaftar?

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
- `dashboard/dashboard.py`: File utama untuk menjalankan dashboard Streamlit.
- `dashboard/main_data.csv`: Dataset hasil pengolahan yang digunakan oleh dashboard.
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
git clone https://github.com/epipachy/bike-sharing-dashboard.git

### 2. Masuk ke Direktori Proyek
cd bike-sharing-dashboard
Pastikan terminal berada di direktori utama proyek (root repository), yaitu direktori yang berisi requirements.txt dan folder dashboard/.
### 3. Membuat Virtual Environment
Buat virtual environment menggunakan perintah:
python -m venv .venv

### 4. Mengaktifkan Virtual Environment
**Windows (PowerShell):**
.\.venv\Scripts\Activate.ps1

**Linux/macOS:**
source .venv/bin/activate

### 5. Menginstal Dependensi
Pastikan virtual environment sudah aktif dan terminal berada di direktori proyek yang berisi `requirements.txt`.
Kemudian jalankan:
python -m pip install -r requirements.txt

### 6. Menjalankan Dashboard
Jalankan aplikasi Streamlit menggunakan perintah:
streamlit run dashboard/dashboard.py
Dashboard akan terbuka secara otomatis melalui browser. Jika tidak terbuka, akses alamat lokal yang ditampilkan pada terminal.

### 7. Pengujian Dashboard

Setelah dashboard berhasil dijalankan, lakukan pengujian dengan memastikan:

- Statistik penyewaan sepeda berhasil ditampilkan.
- Seluruh grafik dan visualisasi muncul dengan benar.
- Filter dan fitur interaktif dapat digunakan.
- Perubahan filter menghasilkan visualisasi yang sesuai.

## Dashboard Interaktif

- Dashboard dikembangkan menggunakan Streamlit dan menyajikan beberapa informasi utama, yaitu:
- Statistik total penyewaan sepeda, rata-rata penyewaan per jam, serta jumlah pengguna kasual dan terdaftar.
- Tren total penyewaan sepeda berdasarkan tanggal.
- Perbandingan rata-rata penyewaan sepeda per jam antara working day dan non-working day.
- Perbandingan rata-rata penyewaan sepeda berdasarkan musim.
- Perbandingan rata-rata penyewaan sepeda berdasarkan kondisi cuaca.
- Rata-rata penyewaan sepeda harian berdasarkan bulan.
- Distribusi penyewaan sepeda oleh pengguna kasual dan pengguna terdaftar.
Dashboard juga dilengkapi dengan filter interaktif berdasarkan rentang tanggal, musim, dan kondisi cuaca.

Link Dashboard Online:
https://bike-sharing-dashboard-x4gqhsprsxzzabdhnkbqcu.streamlit.app/

## Kesimpulan

Melalui proyek ini, dilakukan analisis terhadap pola penyewaan sepeda berdasarkan faktor waktu, musim, kondisi cuaca, dan karakteristik pengguna. Hasil analisis disajikan dalam bentuk visualisasi dan dashboard interaktif untuk membantu memahami tren serta karakteristik penggunaan layanan penyewaan sepeda.
