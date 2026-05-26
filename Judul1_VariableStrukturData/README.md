## Sistem Input dan Pengelolaan Nilai Mahasiswa Menggunakan List 1 Dimensi

**a. Judul Program**:
Sistem Input dan Pengelolaan Nilai Mahasiswa Menggunakan List 1 Dimensi

**b. Deskripsi Singkat**:
Program ini digunakan untuk menyimpan dan menampilkan data nilai mahasiswa menggunakan List 1 Dimensi. Pengguna dapat mengisi nilai ke dalam setiap indeks array, kemudian program akan menampilkan isi data yang telah dimasukkan.

Program dibuat menggunakan konsep List yang terdapat pada modul, di mana data disimpan secara berurutan dan dapat diakses menggunakan indeks.

**c. Source Code**:

<img width="1298" height="2544" alt="code-snapshot" src="https://github.com/user-attachments/assets/bc74d922-7520-486c-af23-5005c036a920" />
Program diawali dengan pembuatan fungsi menu() yang digunakan untuk menampilkan daftar menu pada program. Menu terdiri dari menampilkan address array, menampilkan address seluruh indeks, menginput nilai mahasiswa, menampilkan nilai, dan keluar dari program.

Pada bagian nilai = [0] * 5, program membuat List 1 Dimensi dengan ukuran lima elemen. Seluruh elemen awal bernilai 0. List ini digunakan untuk menyimpan nilai mahasiswa.

Variabel running = True digunakan sebagai penanda agar program terus berjalan selama pengguna belum memilih menu keluar.

Perulangan while running: digunakan agar menu terus muncul dan program dapat dijalankan berulang kali.

Bagian try-except digunakan untuk menangani kesalahan input jika pengguna memasukkan data selain angka sehingga program tidak mengalami error.

Ketika pengguna memilih menu 1, program menjalankan id(nilai) untuk menampilkan address atau lokasi memori dari array utama.

Jika pengguna memilih menu 2, program melakukan perulangan dan menampilkan address masing-masing indeks array menggunakan fungsi id().

Jika pengguna memilih menu 3, program meminta pengguna memasukkan nilai mahasiswa satu per satu. Input juga divalidasi agar hanya menerima angka.

Data nilai yang dimasukkan akan disimpan ke dalam List menggunakan indeks array seperti nilai[i].

Jika pengguna memilih menu 4, program menampilkan seluruh data nilai yang sudah tersimpan pada array.

Jika pengguna memilih menu 5, program menghentikan perulangan dan menampilkan pesan bahwa program selesai dijalankan.

Bagian if __name__ == "__main__": digunakan agar fungsi main() otomatis berjalan ketika file dieksekusi.

**d. Output Program**:

<img width="472" height="213" alt="image" src="https://github.com/user-attachments/assets/271668c9-f81e-4942-b174-be7e35548097" />
Pada output program, tampilan pertama yang muncul adalah judul program, yaitu Sistem Nilai Mahasiswa. Setelah itu, pengguna diberikan beberapa pilihan menu seperti menampilkan address array, menampilkan address setiap indeks, menginput nilai mahasiswa, menampilkan nilai, dan keluar dari program.

Ketika pengguna memilih menu input nilai, program akan meminta pengguna memasukkan nilai mahasiswa satu per satu. Setiap data yang dimasukkan akan disimpan ke dalam List 1 Dimensi pada indeks yang berbeda.

Setelah seluruh data berhasil dimasukkan, pengguna dapat memilih menu tampilkan nilai. Program akan menampilkan seluruh nilai yang tersimpan sesuai urutan indeks array.

Pengguna juga dapat melihat address array utama maupun address masing-masing indeks untuk memahami konsep penyimpanan data pada struktur List.

Program akan terus berjalan sampai pengguna memilih menu keluar. Setelah menu keluar dipilih, program menampilkan pesan Program selesai lalu menghentikan proses.


**e. Link YouTube**:
