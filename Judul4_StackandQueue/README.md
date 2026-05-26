## Sistem Riwayat Lagu Terakhir Diputar Menggunakan Stack (Array)

**a. Judul Program**:
Sistem Riwayat Lagu Terakhir Diputar Menggunakan Stack (Array)

**b. Deskripsi Singkat**:
Program **Sistem Riwayat Lagu Menggunakan Stack (Array)** dibuat untuk mensimulasikan penyimpanan riwayat lagu pada aplikasi pemutar musik dengan menerapkan konsep struktur data **Stack**. Program ini menggunakan prinsip **LIFO (Last In First Out)**, yaitu lagu yang terakhir diputar akan menjadi lagu pertama yang dihapus dari riwayat. Pengguna dapat menambahkan lagu ke dalam riwayat menggunakan operasi *push*, menghapus lagu terakhir menggunakan *pop*, melihat lagu paling atas melalui *peek*, dan menampilkan seluruh riwayat lagu yang tersimpan.

Pada implementasinya, program menggunakan array sebagai media penyimpanan data Stack dengan batas kapasitas tertentu. Program juga dilengkapi pengecekan kondisi **stack penuh (overflow)** dan **stack kosong (underflow)** agar dapat berjalan dengan aman tanpa menimbulkan kesalahan saat proses penambahan atau penghapusan data. Dengan studi kasus ini, pengguna dapat memahami cara kerja Stack dalam penerapan yang dekat dengan kehidupan sehari-hari.


**c. Source Code**:

<img width="1298" height="3722" alt="code-snapshot judul 4" src="https://github.com/user-attachments/assets/581a7d7a-0d6e-4991-837d-2657b2caf757" />
Program diawali dengan pembuatan **class `StackArray`**. Class ini digunakan untuk membuat struktur data **Stack berbasis array** yang berfungsi menyimpan riwayat lagu. Pada class ini terdapat beberapa fungsi utama seperti `push`, `pop`, `peek`, `display`, `is_empty`, dan `is_full` yang digunakan untuk menjalankan operasi Stack.

Pada bagian **`def __init__(self, max_size=10):`**, constructor digunakan untuk menginisialisasi objek Stack. Parameter `max_size` digunakan untuk menentukan kapasitas maksimum Stack yang dapat menampung data lagu.

Perintah **`self.MAX = max_size`**, **`self.stack = [None] * self.MAX`**, dan **`self.top = -1`** digunakan untuk menyimpan ukuran maksimum Stack, membuat array kosong sesuai kapasitas, serta mengatur nilai awal `top` menjadi `-1`. Nilai `-1` menunjukkan bahwa Stack masih kosong dan belum memiliki data.

Pada bagian **`def is_empty(self): return self.top == -1`**, fungsi `is_empty()` digunakan untuk memeriksa apakah Stack dalam keadaan kosong. Jika nilai `top` sama dengan `-1`, maka fungsi akan mengembalikan nilai `True`.

Pada bagian **`def is_full(self): return self.top == self.MAX - 1`**, fungsi `is_full()` digunakan untuk mengecek apakah kapasitas Stack sudah penuh. Jika posisi `top` berada pada indeks terakhir array, maka Stack dianggap penuh.

Pada bagian **`def push(self, lagu):`**, fungsi `push()` digunakan untuk menambahkan lagu baru ke dalam Stack. Operasi ini akan menempatkan data pada posisi paling atas sesuai prinsip **LIFO (Last In First Out)**.

Baris **`if self.is_full():`** digunakan untuk memeriksa apakah Stack sudah penuh sebelum data ditambahkan. Pemeriksaan ini dilakukan untuk mencegah terjadinya kondisi **Stack Overflow**.

Perintah **`self.top += 1`** digunakan untuk menaikkan posisi `top` satu langkah, kemudian **`self.stack[self.top] = lagu`** digunakan untuk menyimpan lagu pada posisi paling atas Stack.

Perintah **`print(f"Lagu '{lagu}' berhasil ditambahkan")`** digunakan untuk menampilkan pesan bahwa lagu berhasil dimasukkan ke dalam riwayat.

Pada bagian **`def pop(self):`**, fungsi `pop()` digunakan untuk menghapus lagu yang berada pada posisi paling atas Stack.

Baris **`if self.is_empty():`** digunakan untuk memeriksa apakah Stack kosong sebelum proses penghapusan dilakukan. Hal ini dilakukan agar program tidak mengalami kondisi **Stack Underflow**.

Perintah **`lagu = self.stack[self.top]`** digunakan untuk menyimpan sementara lagu yang akan dihapus sehingga datanya masih dapat ditampilkan.

Perintah **`self.top -= 1`** digunakan untuk menurunkan posisi `top`, yang menandakan bahwa elemen paling atas telah dihapus dari Stack.

Pada bagian **`def peek(self):`**, fungsi `peek()` digunakan untuk melihat lagu yang berada di posisi paling atas tanpa menghapus data tersebut.

Perintah **`print("Lagu terakhir diputar:", self.stack[self.top])`** digunakan untuk menampilkan lagu terakhir yang tersimpan pada Stack.

Pada bagian **`def display(self):`**, fungsi `display()` digunakan untuk menampilkan seluruh isi Stack.

Perulangan **`for i in range(self.top, -1, -1):`** digunakan untuk menampilkan data dari indeks paling atas menuju indeks paling bawah. Perulangan dimulai dari `top` sampai `0` agar urutan tampil sesuai konsep Stack.

Perintah **`print("-", self.stack[i])`** digunakan untuk menampilkan setiap lagu yang tersimpan dalam Stack.

Pada bagian **`def main():`**, fungsi `main()` digunakan sebagai program utama yang menjalankan seluruh menu dan proses interaksi pengguna.

Baris **`musik = StackArray()`** digunakan untuk membuat objek Stack bernama `musik`.

Perulangan **`while pilih != 5:`** digunakan agar menu terus ditampilkan sampai pengguna memilih menu keluar.

Bagian **`pilih = int(input("Pilih menu: "))`** digunakan untuk menerima pilihan menu dari pengguna.

Jika pengguna memilih menu **1**, program menjalankan perintah input judul lagu kemudian memanggil fungsi `push()` untuk menambahkan lagu ke Stack.

Jika pengguna memilih menu **2**, program menjalankan fungsi `pop()` untuk menghapus lagu terakhir dari riwayat.

Jika pengguna memilih menu **3**, program menjalankan fungsi `peek()` untuk melihat lagu terakhir yang diputar.

Jika pengguna memilih menu **4**, program menjalankan fungsi `display()` untuk menampilkan seluruh isi riwayat lagu.

Jika pengguna memilih menu **5**, program menampilkan pesan **"Program selesai"** dan menghentikan proses.

Bagian **`except ValueError:`** digunakan untuk menangani kesalahan input apabila pengguna memasukkan data yang bukan angka pada pilihan menu.

Terakhir, bagian **`if __name__ == "__main__": main()`** digunakan agar fungsi `main()` otomatis dijalankan saat file program dieksekusi.

**d. Output Program**:

<img width="661" height="208" alt="Cuplikan layar 2026-05-26 221205" src="https://github.com/user-attachments/assets/96210a6b-975c-4187-bbac-2b2c0dabe702" />

Pada output program, tampilan pertama yang muncul adalah judul program, yaitu **Sistem Riwayat Lagu Menggunakan Stack**. Setelah itu, pengguna diberikan beberapa pilihan menu seperti menambahkan lagu, menghapus lagu terakhir, melihat lagu terakhir yang diputar, menampilkan seluruh riwayat lagu, dan keluar dari program.

Ketika pengguna memilih menu **Tambah Lagu**, program akan meminta pengguna memasukkan judul lagu yang ingin disimpan ke dalam riwayat. Setelah lagu dimasukkan, program akan menambahkan lagu tersebut ke dalam Stack dan menampilkan pesan bahwa lagu berhasil ditambahkan. Proses ini dapat dilakukan berulang kali sehingga pengguna dapat menambahkan beberapa lagu ke dalam riwayat.

Setelah beberapa lagu berhasil dimasukkan, pengguna dapat memilih menu **Tampilkan Riwayat**. Pada bagian ini program akan menampilkan seluruh lagu yang tersimpan di dalam Stack. Data lagu ditampilkan mulai dari lagu yang paling akhir dimasukkan hingga lagu yang pertama dimasukkan. Hal ini menunjukkan penerapan konsep Stack yang bekerja menggunakan prinsip **LIFO (Last In First Out)**.

Pengguna juga dapat memilih menu **Lihat Lagu Terakhir** untuk mengetahui lagu yang berada pada posisi paling atas tanpa menghapusnya dari Stack. Program akan menampilkan lagu terakhir yang diputar atau yang terakhir dimasukkan ke dalam riwayat.

Selanjutnya, jika pengguna memilih menu **Hapus Lagu Terakhir**, program akan menjalankan operasi **pop()** untuk menghapus lagu yang berada di posisi paling atas Stack. Lagu yang terakhir ditambahkan akan menjadi lagu pertama yang dihapus. Setelah proses penghapusan selesai, isi Stack akan berubah sesuai data yang tersisa.

Program akan terus menampilkan menu utama selama pengguna belum memilih menu **Keluar**. Jika pengguna memilih menu keluar, program akan menampilkan pesan **"Program selesai"** dan menghentikan seluruh proses.


**e. Link YouTube**:
