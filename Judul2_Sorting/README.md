## Sistem Pengurutan Harga Kopi Coffee Shop Menggunakan Insertion Sort

**a. Judul Program**:
Sistem Pengurutan Harga Kopi Coffee Shop Menggunakan Insertion Sort

**b. Deskripsi Singkat**:
Program ini digunakan untuk mengurutkan daftar menu kopi berdasarkan harga dari yang termurah hingga termahal menggunakan algoritma Insertion Sort. Pengguna dapat memasukkan nama kopi dan harga, kemudian program akan menampilkan data sebelum dan sesudah proses pengurutan.

Program menerapkan konsep Insertion Sort, yaitu membandingkan data yang sedang diproses dengan data sebelumnya, lalu menyisipkannya pada posisi yang tepat hingga seluruh data tersusun secara berurutan.

**c. Source Code**:
<img width="1298" height="2354" alt="code-snapshot judul 2" src="https://github.com/user-attachments/assets/fdf03679-85f9-4957-bf27-4d248b333b51" />

Program diawali dengan pembuatan fungsi **`insertion_sort_kopi(data_kopi, n)`**. Fungsi ini digunakan untuk mengurutkan data kopi berdasarkan harga menggunakan algoritma **Insertion Sort**. Parameter `data_kopi` digunakan untuk menerima list yang berisi data kopi, sedangkan parameter `n` digunakan untuk menerima jumlah data kopi yang akan diurutkan.

Pada bagian awal fungsi terdapat perulangan **`for i in range(1, n)`**. Perulangan ini dimulai dari indeks ke-1 karena data pada indeks ke-0 dianggap sudah berada pada posisi yang benar. Setiap data pada indeks ke-`i` akan dibandingkan dengan data-data sebelumnya untuk menentukan posisi yang tepat.

Variabel **`temp`** digunakan untuk menyimpan sementara data kopi yang sedang dibandingkan. Data ini perlu disimpan sementara agar tidak hilang ketika terjadi proses pergeseran data. Selanjutnya, variabel **`j`** diberi nilai **`i - 1`**, yang berarti menunjuk ke indeks sebelum data yang sedang dibandingkan.

Bagian **`while j >= 0 and data_kopi[j]["harga"] > temp["harga"]`** digunakan untuk membandingkan harga kopi sebelumnya dengan harga kopi yang sedang disimpan di variabel `temp`. Selama indeks `j` masih valid dan harga kopi sebelumnya lebih besar daripada harga kopi pada `temp`, maka data kopi tersebut akan digeser satu posisi ke kanan.

Perintah **`data_kopi[j + 1] = data_kopi[j]`** digunakan untuk menggeser data kopi yang memiliki harga lebih besar ke posisi sebelah kanan. Setelah itu, perintah **`j -= 1`** digunakan untuk mengurangi nilai `j` agar proses perbandingan berlanjut ke data sebelumnya.

Setelah posisi yang sesuai ditemukan, perintah **`data_kopi[j + 1] = temp`** digunakan untuk menempatkan data kopi yang disimpan pada variabel `temp` ke posisi yang benar. Proses ini akan terus diulang hingga seluruh data berhasil tersusun berdasarkan harga dari yang terkecil sampai yang terbesar.

Pada bagian **`main()`**, fungsi ini digunakan sebagai program utama untuk menjalankan seluruh proses program. Program pertama kali menampilkan judul **Sistem Pengurutan Harga Kopi Coffee Shop**, kemudian meminta pengguna memasukkan jumlah data kopi yang ingin diinput.

Selanjutnya program membuat list kosong **`data_kopi = []`** yang digunakan untuk menyimpan seluruh data kopi yang diinput pengguna. Setelah itu dilakukan perulangan sebanyak jumlah data yang dimasukkan.

Pada setiap perulangan, program meminta pengguna menginput **nama kopi** dan **harga kopi**. Bagian input harga menggunakan struktur **`try-except`** untuk mengantisipasi kesalahan input. Jika pengguna memasukkan data selain angka, program akan menampilkan pesan kesalahan dan meminta pengguna menginput ulang sampai data valid.

Setelah nama dan harga berhasil dimasukkan, data disimpan ke dalam list menggunakan bentuk **dictionary** yang berisi pasangan **nama** dan **harga**. Penggunaan dictionary mempermudah proses penyimpanan serta pengambilan data berdasarkan atribut tertentu.

Setelah seluruh data berhasil dimasukkan, program akan menampilkan daftar kopi sebelum diurutkan. Pada bagian ini data masih ditampilkan sesuai urutan input pengguna sehingga pengguna dapat melihat kondisi awal data.

Kemudian program menjalankan fungsi **`insertion_sort_kopi(data_kopi, n)`** untuk melakukan proses pengurutan berdasarkan harga kopi.

Setelah proses pengurutan selesai, program menampilkan kembali data kopi yang sudah tersusun dari harga paling murah hingga paling mahal. Dengan demikian pengguna dapat membandingkan hasil sebelum dan sesudah proses pengurutan.

Terakhir, bagian **`if __name__ == "__main__": main()`** digunakan agar fungsi `main()` dijalankan secara otomatis ketika file program dieksekusi.


**d. Output Program**:
<img width="1070" height="784" alt="image" src="https://github.com/user-attachments/assets/1cfdfe83-f46a-4d67-8042-3572899b7cc2" />
Pada output program, tampilan pertama yang muncul adalah judul program, yaitu **Sistem Pengurutan Harga Kopi Coffee Shop**. Setelah itu, pengguna diminta memasukkan jumlah data kopi yang ingin diinput ke dalam program.

Setelah jumlah data dimasukkan, program akan meminta pengguna mengisi data kopi satu per satu. Setiap data terdiri dari **nama kopi** dan **harga kopi**. Program juga melakukan validasi pada input harga sehingga jika pengguna memasukkan data selain angka, program akan menampilkan pesan kesalahan dan meminta pengguna menginput ulang hingga data yang dimasukkan valid.

Setelah semua data berhasil dimasukkan, program menampilkan daftar kopi sebelum diurutkan. Pada bagian ini, data kopi masih ditampilkan sesuai urutan input dari pengguna. Hal ini bertujuan untuk memperlihatkan kondisi awal data sebelum proses pengurutan dilakukan.

Kemudian program menjalankan proses pengurutan menggunakan algoritma **Insertion Sort**. Algoritma ini bekerja dengan cara mengambil satu data, membandingkannya dengan data sebelumnya, lalu menyisipkan data tersebut ke posisi yang sesuai sampai seluruh data tersusun dengan benar.

Setelah proses pengurutan selesai, program menampilkan daftar kopi yang telah diurutkan berdasarkan harga dari yang paling murah hingga yang paling mahal. Hasil tersebut menunjukkan perubahan urutan data setelah proses sorting dilakukan sehingga pengguna dapat melihat perbedaan kondisi data sebelum dan sesudah proses pengurutan.

Program akan berakhir setelah seluruh proses selesai dilakukan dan hasil pengurutan berhasil ditampilkan kepada pengguna.


**e. Link YouTube**:
