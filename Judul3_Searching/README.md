## Mencari kode Buku diperpustakaan (Binary Search)

**a. Judul Program**:
Mencari kode Buku diperpustakaan (Binary Search)

**b. Deskripsi Singkat**:
Program ini merupakan implementasi algoritma Binary Search menggunakan bahasa pemrograman Python untuk mencari kode buku pada sebuah daftar data yang sudah terurut. Program bekerja dengan menentukan posisi tengah data, kemudian membandingkan nilai tengah tersebut dengan kode buku yang dicari. Jika nilai target lebih besar, pencarian dilanjutkan ke bagian kanan, sedangkan jika lebih kecil maka pencarian dilakukan ke bagian kiri. Proses ini dilakukan secara berulang hingga data ditemukan atau tidak ada lagi data yang dapat diperiksa.

Pada program ini terdapat fungsi `binary_search()` yang bertugas melakukan proses pencarian, serta fungsi `main()` yang digunakan untuk menjalankan program utama. Data kode buku disimpan dalam sebuah list yang berisi angka terurut, kemudian pengguna diminta memasukkan kode buku yang ingin dicari. Program juga dilengkapi dengan penanganan kesalahan (`try-except`) untuk mencegah input selain angka sehingga program menjadi lebih aman dan mudah digunakan.


**c. Source Code**:
<img width="1298" height="2202" alt="code-snapshot" src="https://github.com/user-attachments/assets/00578afc-879b-4a2c-8a2d-8a392390ac45" />
Program diawali dengan pembuatan fungsi `binary_search(data, target)`. Fungsi ini digunakan untuk melakukan pencarian data menggunakan algoritma Binary Search. Parameter `data` digunakan untuk menerima list yang berisi kumpulan kode buku yang sudah terurut, sedangkan parameter `target` digunakan untuk menerima nilai kode buku yang ingin dicari oleh pengguna.

Pada bagian awal fungsi terdapat perintah `left = 0` dan `right = len(data) - 1`. Variabel `left` digunakan untuk menyimpan indeks awal data, sedangkan variabel `right` digunakan untuk menyimpan indeks akhir data. Fungsi `len(data)` digunakan untuk menghitung jumlah elemen pada list, kemudian dikurangi 1 karena indeks array dimulai dari 0.

Selanjutnya terdapat perulangan `while left <= right:`. Perulangan ini digunakan untuk menjalankan proses pencarian selama batas kiri (`left`) belum melewati batas kanan (`right`). Jika `left` lebih besar dari `right`, maka data dianggap tidak ditemukan.

Pada bagian berikutnya terdapat perintah `mid = (left + right) // 2`. Variabel `mid` digunakan untuk menentukan posisi tengah data. Operator `//` digunakan agar hasil pembagian menjadi bilangan bulat sehingga dapat digunakan sebagai indeks array.

Selanjutnya terdapat perintah `print(f"Posisi tengah: {mid}, nilai: {data[mid]}")`. Perintah ini digunakan untuk menampilkan posisi indeks tengah beserta nilai data pada indeks tersebut agar proses pencarian dapat terlihat saat program dijalankan.

Bagian berikutnya adalah proses pengecekan data menggunakan `if data[mid] == target:`. Kondisi ini digunakan untuk memeriksa apakah nilai pada indeks tengah sama dengan data yang dicari. Jika sama, maka fungsi akan mengembalikan indeks data tersebut menggunakan `return mid`.

Selanjutnya terdapat kondisi `elif data[mid] < target:`. Kondisi ini digunakan untuk memeriksa apakah nilai tengah lebih kecil dari target yang dicari. Jika benar, berarti data berada di bagian kanan array.

Kemudian terdapat perintah `print("Mencari ke bagian kanan")` dan `left = mid + 1`. Perintah `print()` digunakan untuk menampilkan proses pencarian ke bagian kanan, sedangkan variabel `left` diubah menjadi `mid + 1` agar pencarian dilanjutkan mulai dari bagian kanan data.

Bagian berikutnya adalah `else:`. Bagian ini dijalankan apabila nilai tengah lebih besar dari target yang dicari, sehingga data berada di bagian kiri array.

Kemudian terdapat perintah `print("Mencari ke bagian kiri")` dan `right = mid - 1`. Perintah `print()` digunakan untuk menampilkan proses pencarian ke bagian kiri, sedangkan variabel `right` diubah menjadi `mid - 1` agar pencarian dilanjutkan ke bagian kiri data.

Setelah perulangan selesai dan data tidak ditemukan, terdapat perintah `return -1`. Perintah ini digunakan untuk mengembalikan nilai `-1` sebagai tanda bahwa data tidak ditemukan di dalam list.

Program kemudian melanjutkan ke fungsi utama `def main():`. Fungsi `main()` digunakan sebagai fungsi utama untuk menjalankan seluruh program.

Pada bagian berikutnya terdapat data list `data_buku = [101, 105, 110, 115, 120, 125, 130, 135, 140, 145]`. Variabel `data_buku` digunakan untuk menyimpan daftar kode buku yang sudah terurut secara menaik. Data terurut merupakan syarat utama penggunaan Binary Search.

Selanjutnya terdapat perintah `print("Data kode buku:")` dan `print(data_buku)`. Perintah ini digunakan untuk menampilkan seluruh data kode buku kepada pengguna sebelum proses pencarian dilakukan.

Pada bagian berikutnya terdapat `try:`. Perintah `try` digunakan untuk menangani kemungkinan kesalahan input saat pengguna memasukkan data.

Selanjutnya terdapat input pengguna `target = int(input("Masukkan kode buku yang ingin dicari: "))`. Perintah ini digunakan untuk meminta pengguna memasukkan kode buku yang ingin dicari. Fungsi `int()` digunakan untuk mengubah input menjadi tipe data integer.

Kemudian program menjalankan fungsi Binary Search menggunakan `hasil = binary_search(data_buku, target)`. Variabel `hasil` digunakan untuk menyimpan hasil pencarian berupa indeks data.

Bagian berikutnya adalah proses pengecekan hasil menggunakan `if hasil != -1:`. Kondisi ini digunakan untuk memeriksa apakah data berhasil ditemukan.

Kemudian terdapat perintah `print(f"Kode buku ditemukan pada indeks ke-{hasil}")`. Perintah ini digunakan untuk menampilkan indeks tempat data ditemukan.

Selanjutnya terdapat bagian `else: print("Kode buku tidak ditemukan")`. Bagian ini dijalankan apabila data tidak ditemukan di dalam list.

Program juga memiliki penanganan kesalahan input menggunakan `except ValueError:` dan `print("Input harus berupa angka!")`. Bagian `except` digunakan untuk menangani error apabila pengguna memasukkan input selain angka.

Pada bagian terakhir terdapat `if __name__ == "__main__":` dan `main()`. Perintah ini digunakan agar fungsi `main()` dijalankan secara otomatis ketika file Python dieksekusi langsung.


**d. Output Program**:
<img width="731" height="170" alt="Cuplikan layar 2026-05-07 212015" src="https://github.com/user-attachments/assets/3afb8a59-8bfb-4b85-b792-d5da5cd57abb" />
Pada output program, tampilan pertama yang muncul adalah daftar data kode buku yang tersedia di dalam program. Data tersebut sudah tersusun secara terurut sehingga dapat digunakan dalam proses pencarian menggunakan algoritma Binary Search. Setelah itu, pengguna diminta memasukkan kode buku yang ingin dicari.

Setelah pengguna memasukkan kode buku, program akan mulai menjalankan proses pencarian. Program terlebih dahulu menentukan posisi tengah data, kemudian menampilkan indeks tengah beserta nilai pada posisi tersebut. Jika nilai tengah lebih besar dari data yang dicari, maka program akan mencari ke bagian kiri. Sebaliknya, jika nilai tengah lebih kecil dari data yang dicari, maka program akan mencari ke bagian kanan.

Selama proses pencarian berlangsung, program akan terus menampilkan perpindahan pencarian ke kiri atau ke kanan sampai data ditemukan atau seluruh data selesai diperiksa. Hal ini bertujuan agar pengguna dapat melihat bagaimana algoritma Binary Search bekerja dalam mempersempit area pencarian.

Setelah proses pencarian selesai, program akan menampilkan hasil akhir berupa informasi apakah kode buku berhasil ditemukan atau tidak ditemukan. Jika data ditemukan, program akan menampilkan indeks tempat data berada di dalam list. Namun jika data tidak ditemukan, maka program akan menampilkan pesan bahwa kode buku tidak ditemukan.



**e. Link YouTube**:
https://www.youtube.com/watch?v=c2w29L4aU0k
