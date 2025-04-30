# -*- coding: utf-8 -*-

## Aplikasi genetic algorithm untuk memenuhi tugas besar mata kuliah kecerdasan buatan
## Dibuat oleh Kelompok 11: Daniyal Arshaq Sudrajat, Riziq Rizwan.

## =========== DESKRIPSI TUGAS ===========
## Diberikan file restoran.xlsx berupa himpunan data 100 review restoran yang ada di kota Bandung 
## dengan dua atribut: Kualitas Servis (1-100; semakin tinggi semakin baik) dan Harga (bilangan real 25000-55000, 
## semakin tinggi semakin mahal). Bangunlah sebuah sistem berbasis Fuzzy Logic untuk memilih 10 
## restoran terbaik di kota Bandung. Sistem membaca masukan file restoran.xlsx dan mengeluarkan output 
## berupa sebuah file peringkat.xlsx yang berisi 5 nomor/ID restoran terbaik beserta skor-nya (output 
## Defuzzification), dilengkapi dengan info kualitas servis dan harganya. 

## Tugas Anda ialah membuat sebuah sistem berbasis Fuzzy Logic Inference untuk memilih 5 restoran 
## terbaik. Program yang Anda bangun membaca masukan file supplier.xlsx dan menampilkan output berupa 
## 5 supplier terbaik yang dilengkapi informasi berupa: Id pelanggan, info kualitas servis dan harganya, 
## serta skor kelayakan supplier untuk dipilih (hasil dari proses defuzzification). 

##  =========== POIN POIN YANG HARUS ANDA ANALISIS DAN DESAIN ===========
    ##  Jumlah dan Nama Linguistik setiap atribut input
    ##  Bentuk dan Batas Fungsi Keanggotaan Input
    ##  Aturan Inferensi
    ##  Metode Defuzzification
    ##  Bentuk dan Batas Fungsi Keanggotaan Output (sesuai metode Defuzzification)

##  =========== PROSES YANG HARUS ANDA IMPLEMENTASIKAN KE DALAM PROGRAM ===========
    ## Membaca data dari file
    ## Fuzzification
    ## Inferensi 
    ## Defuzzification 
    ## Menyimpan output ke file

##  =========== OUTPUT PROGRAM ===========
##  Output program Anda adalah tampilan daftar 5 restoran terbaik pilihan Sistem Fuzzy Anda yang berisi 
##  informasi terkait berupa: Id restoran, kualitas servis, harga, dan skor kelayakannya.

##  =========== PEMBAGIAN TUGAS ===========
##  Sistem 50/50
##  Daniyal: 
    ## Membaca data dari file
    ## Fuzzification
    ## Menyimpan output ke file
##  Riziq:
    ## Inferensi 
    ## Defuzzification

## =========== SOURCE CODE PROGRAM ===========
## Program dibangun menggunakan bahasa pemrograman Python. 
## Tidak diperkenankan menggunakan Library yang secara langsung melakukan proses-proses pada 
## Fuzzy Systems (fuzzification, inferensi, defuzzification); Penggunaan Library, akan mengurangi nilai tugas ini. 
## Berikan catatan/keterangan untuk masing-masing bagian atau baris program anda. 
## Berikan catatan terkait cara menggunakan/menjalankan program Anda pada file Readme.txt; 
## Tempatkan di folder yang sama dengan file utama program.

## ================================================================================================================== 
##                                                 PROGRAM
## ================================================================================================================== 


import pandas as pd

# membaca data dari file
def ReadFile():
    # membaca data dari file restoran.xlsx
    data  = pd.read_excel(r'C:\Users\sxpix\Downloads\restoran.xlsx') # ganti sesuai dengan path file anda
    return data 

# menyimpan data ke file peringkat.xlsx
def SaveFile(dataHasil):
    dataHasil.to_excel(r'C:\Users\sxpix\Downloads\Hasil Run\peringkat.xlsx', index=False) # menyimpan data ke file peringkat.xlsx

# fungsi membership untuk kualitas servis
def kualitas_servis(x):
    # menghitung derajat keanggotaan 'buruk', 'sedang', dan 'bagus' untuk nilai servis
    # fungsi keanggotaan berbentuk segitiga
    return {
        'buruk': max(min((40 - x) / 40, 1), 0), # semakin kecil x, semakin 'buruk' (0-40)
        'sedang': max(min((x - 30) / 40, (70 - x) / 40, 1), 0), # nilai tengah antara 30-70
        'bagus': max(min((x - 60) / 40, 1), 0) # semakin besar x, semakin 'bagus' (60-100)
    }

# fungsi membership untuk harga
def harga_restoran(x):
    # menghitung derajat keanggotaan 'murah', 'sedang', dan 'mahal' untuk nilai harga
    # fungsi keanggotaan berbentuk segitiga
    return {
        'murah': max(min((35000 - x) / 10000, 1), 0), # semakin kecil harga, semakin 'murah' 
        'sedang': max(min((x - 30000) / 15000, (45000 - x) / 15000, 1), 0), # harga sedang antara 30rb-45rb
        'mahal': max(min((x - 40000) / 15000, 1), 0) # semakin besar harga, semakin 'mahal'
    }

# proses fuzzification
def Fuzzification(data):
    # Melakukan proses fuzzifikasi semua data restoran
    fuzzy_data = []
    for index, row in data.iterrows():
        servis_fuzz = kualitas_servis(row['Pelayanan']) # hitung membership kualitas servis
        harga_fuzz = harga_restoran(row['harga']) # hitung membership harga
        fuzzy_data.append({
            'ID': row['id Pelanggan'],
            'servis': servis_fuzz,
            'harga': harga_fuzz,
            'servis_asli': row['Pelayanan'],
            'harga_asli': row['harga']
        })
    return fuzzy_data

#proses inferensi
def inferensi(servis, harga):
    # Ambil derajat keanggotaan dari masing-masing kategori pada servis
    buruk, sedang, bagus = servis['buruk'], servis['sedang'], servis['bagus']
    # Ambil derajat keanggotaan dari masing-masing kategori pada harga
    murah, harga_sedang, mahal = harga['murah'], harga['sedang'], harga['mahal']

    # Buat aturan fuzzy berdasarkan kombinasi servis dan harga
    rules = [
        (min(buruk, mahal), 'rendah'),          # Jika pelayanan buruk dan harga mahal -> skor rendah
        (min(buruk, harga_sedang), 'rendah'),   # Jika pelayanan buruk dan harga sedang -> skor rendah
        (min(buruk, murah), 'sedang'),          # Jika pelayanan buruk dan harga murah -> skor sedang

        (min(sedang, mahal), 'sedang'),         # Jika pelayanan sedang dan harga mahal -> skor sedang
        (min(sedang, harga_sedang), 'sedang'),  # Jika pelayanan sedang dan harga sedang -> skor sedang
        (min(sedang, murah), 'tinggi'),         # Jika pelayanan sedang dan harga murah -> skor tinggi

        (min(bagus, mahal), 'sedang'),          # Jika pelayanan bagus dan harga mahal -> skor sedang
        (min(bagus, harga_sedang), 'tinggi'),   # Jika pelayanan bagus dan harga sedang -> skor tinggi
        (min(bagus, murah), 'tinggi'),          # Jika pelayanan bagus dan harga murah -> skor tinggi
    ]
    return rules  # Kembalikan aturan dalam bentuk list pasangan (nilai_minimum, kategori)

# Proses defuzzifikasi
def Defuzzification(rules):
    num = 0     # Pembilang dari perhitungan weighted average
    denom = 0   # Penyebutnya (total bobot yang digunakan)

    # Iterasi semua aturan fuzzy
    for nilai, kategori in rules:
        # Tetapkan nilai numerik berdasarkan kategori fuzzy
        if kategori == 'rendah':
            score = 30
        elif kategori == 'sedang':
            score = 50
        elif kategori == 'tinggi':
            score = 100
        else:
            score = 0  # Jika tidak cocok dengan kategori manapun

        # Akumulasi nilai * skor ke pembilang dan nilai ke penyebut
        num += nilai * score
        denom += nilai

    # Menghitung hasil akhir (nilai defuzzifikasi), jika penyebut tidak nol
    if denom != 0:
        return num / denom
    else:
        return 0  # Jika semua nilai 0, hasil juga 0


# Fungsi utama
def utama():
    data = ReadFile()
    fuzzy_data = Fuzzification(data)

    hasil_akhir = []
    for item in fuzzy_data:
        servis = item['servis']
        harga = item['harga']
        rules = inferensi(servis, harga)
        skor = Defuzzification(rules)

        hasil_akhir.append({
            'ID': item['ID'],
            'Servis': item['servis_asli'],
            'Harga': item['harga_asli'],
            'Skor': skor
        })

    # Ambil 5 restoran terbaik
    top5 = sorted(hasil_akhir, key=lambda x: x['Skor'], reverse=True)[:5]
    SaveFile(pd.DataFrame(top5))
    print(f"{'No':<5}{'ID Pelanggan':<15}{'Servis':<10}{'Harga':<10}{'Skor'}")
    for i, res in enumerate(top5, 1):
        print(f"{i:<5}{res['ID']:<15}{res['Servis']:<10}{res['Harga']:<10}{res['Skor']:.2f}")


utama()
