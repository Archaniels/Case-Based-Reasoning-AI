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
    data  = pd.read_excel('C:\Users\sxpix\Downloads\restoran.xlsx') # ganti sesuai dengan path file anda
    return data 

# menyimpan data ke file peringkat.xlsx
def SaveFile(dataHasil):
    dataHasil.to_excel('peringkat.xlsx', index=False) # menyimpan data ke file peringkat.xlsx

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
        servis_fuzz = kualitas_servis(row['Servis']) # hitung membership kualitas servis
        harga_fuzz = harga_restoran(row['Harga']) # hitung membership harga
        fuzzy_data.append({
            'id': row['ID'],
            'servis': servis_fuzz,
            'harga': harga_fuzz,
            'servis_asli': row['Servis'],
            'harga_asli': row['Harga']
        })
    return fuzzy_data

# proses inferensi
def Inferensi():


# proses defuzzification
def Defuzzification():
    

# main function
def Main():
    # membaca file
    data = ReadFile()

    # Proses Fuzzification
    fuzzy_data = Fuzzification(data)