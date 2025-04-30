# Case-Based-Reasoning-AI

Diberikan file restoran.xlsx berupa himpunan data 100 review restoran yang ada di kota Bandung dengan dua atribut: Kualitas Servis (1-100; semakin tinggi semakin baik) dan Harga (bilangan real 25000-55000, semakin tinggi semakin mahal). Bangunlah sebuah sistem berbasis Fuzzy Logic untuk memilih 10 restoran terbaik di kota Bandung. Sistem membaca masukan file restoran.xlsx dan mengeluarkan output berupa sebuah file peringkat.xlsx yang berisi 5 nomor/ID restoran terbaik beserta skor-nya (output Defuzzification), dilengkapi dengan info kualitas servis dan harganya. 

Tugas Anda ialah membuat sebuah sistem berbasis Fuzzy Logic Inference untuk memilih 5 restoran terbaik. Program yang Anda bangun membaca masukan file supplier.xlsx dan menampilkan output berupa 5 supplier terbaik yang dilengkapi informasi berupa: Id pelanggan, info kualitas servis dan harganya, serta skor kelayakan supplier untuk dipilih (hasil dari proses defuzzification).  

Poin-poin yang harus Anda desain dan analisis: 
- Jumlah dan Nama Linguistik setiap atribut input
- Bentuk dan Batas Fungsi Keanggotaan Input
- Aturan Inferensi
- Metode Defuzzification
- Bentuk dan Batas Fungsi Keanggotaan Output (sesuai metode Defuzzification) 
Catatan: Poin-poin di atas harus ada di dalam Laporan Tugas! 


Proses yang harus Anda implementasikan ke dalam program (bisa berbentuk fungsi/prosedur):
- Membaca data dari file
- Fuzzification
- Inferensi
- Defuzzification
- Menyimpan output ke file 
Catatan: Proses-proses di atas harus dibangun tanpa menggunakan Library!

Panduan Penggunaan Program:
- Karena program menggunakan bahasa Python, buka IDE pilihan anda, seperti Visual Studio Code, atau Visual Studio 2022.
- Di ReadFile(), harap ganti lokasi yang telah di tentukan di kode dengan lokasi file restoran.xlsx yang anda miliki, atau yang telah di attach di repository ini.
- Jalankan program menggunakan tombol "run" di toolbar IDE anda.
- Jika program berjalan, window terminal baru akan tampil di layar, serta hasil kerja program.
- Selain itu, juga terdapat function SaveFile() dan anda dapat mengatur dimana anda ingin menyimpan lokasi file tersebut.

Resource:
Link Presentasi: https://www.canva.com/design/DAGmANG05cc/9ptEZTTUCWQzWymcD4Bd6g/edit?utm_content=DAGmANG05cc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
Link Laporan: https://docs.google.com/document/d/14yUIvnY2U87wUFnTI39OCyHLZ3ojc1vgN9fRyKHnjYc/edit?usp=sharing
