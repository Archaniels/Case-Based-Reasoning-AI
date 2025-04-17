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


def