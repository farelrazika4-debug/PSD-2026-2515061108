## Implementasi Hash Map Menggunakan Metode Separate Chaining

**a. Judul Program**:
Implementasi Hash Map Menggunakan Metode Separate Chaining

**b. Deskripsi Singkat**:
Program ini dibuat untuk mengimplementasikan struktur data Hash Map menggunakan metode Separate Chaining sebagai penanganan collision. Setiap data disimpan dalam bentuk pasangan key-value, dimana key digunakan sebagai identitas unik untuk mengakses value yang tersimpan. Apabila terjadi collision atau dua key menghasilkan indeks yang sama, maka data akan disimpan menggunakan linked list pada slot yang sama. Metode ini sesuai dengan contoh yang digunakan pada modul praktikum.

Program menyediakan beberapa fitur utama, yaitu menambahkan data (insert), mencari data (search), menghapus data (delete), dan menampilkan seluruh isi hash table (display). Dengan adanya menu interaktif, pengguna dapat mengelola data yang tersimpan dalam Hash Map secara mudah dan memahami bagaimana proses hashing serta penanganan collision bekerja.

**c. Source Code**:

<img width="1410" height="6344" alt="code-snapshot" src="https://github.com/user-attachments/assets/d5f8f934-4d17-4067-b7a8-8e2d76fe8d99" />

Program diawali dengan pembuatan class Node. Class ini digunakan untuk membuat node pada linked list yang akan digunakan sebagai penampung data ketika terjadi collision pada Hash Map.

Pada fungsi __init__(self, key, value), parameter key digunakan untuk menerima kunci data yang akan disimpan, sedangkan parameter value digunakan untuk menerima nilai yang berhubungan dengan key tersebut.

Perintah self.key = key digunakan untuk menyimpan nilai key ke dalam node. Nilai ini nantinya digunakan sebagai identitas utama saat proses pencarian, penghapusan, maupun pembaruan data.

Perintah self.value = value digunakan untuk menyimpan value yang berhubungan dengan key tertentu. Value ini merupakan informasi yang akan diakses ketika key ditemukan.

Perintah self.next = None digunakan untuk menyimpan alamat node berikutnya. Nilai awal None menunjukkan bahwa node tersebut belum terhubung dengan node lain.

Selanjutnya dibuat class HashMapSeparateChaining yang digunakan untuk mengelola seluruh operasi Hash Map.

Pada fungsi __init__(self, size=10), parameter size digunakan untuk menentukan ukuran hash table yang akan digunakan.

Perintah self.SIZE = size digunakan untuk menyimpan ukuran hash table ke dalam variabel objek sehingga dapat digunakan pada seluruh fungsi.

Perintah self.table = [None] * self.SIZE digunakan untuk membuat array hash table dengan jumlah indeks sesuai ukuran yang ditentukan. Setiap indeks awalnya bernilai None karena belum terdapat data yang disimpan.

Pada bagian berikut terdapat fungsi hash_function(self, key).

Fungsi ini digunakan untuk mengubah nilai key menjadi indeks tertentu pada hash table menggunakan operasi modulus.

Perintah return (key % self.SIZE + self.SIZE) % self.SIZE digunakan untuk menghasilkan indeks hash yang valid. Rumus ini memastikan bahwa indeks selalu berada dalam rentang ukuran hash table dan tetap aman apabila terdapat nilai negatif.

Selanjutnya terdapat fungsi insert(self, key, value) yang digunakan untuk menambahkan data baru ke dalam Hash Map.

Perintah index = self.hash_function(key) digunakan untuk menentukan posisi penyimpanan data berdasarkan hasil fungsi hash.

Perintah current = self.table[index] digunakan untuk mengambil node pertama pada indeks yang dituju.

Bagian while current is not None: digunakan untuk menelusuri linked list apabila pada indeks tersebut sudah terdapat data sebelumnya.

Perintah if current.key == key: digunakan untuk memeriksa apakah key yang dimasukkan sudah ada di dalam Hash Map.

Perintah current.value = value digunakan untuk memperbarui value apabila key yang sama ditemukan.

Perintah return digunakan untuk menghentikan proses karena data telah berhasil diperbarui tanpa perlu membuat node baru.

Perintah current = current.next digunakan untuk berpindah ke node berikutnya selama proses penelusuran linked list berlangsung.

Perintah new_node = Node(key, value) digunakan untuk membuat node baru apabila key belum ditemukan.

Perintah new_node.next = self.table[index] digunakan untuk menghubungkan node baru dengan node lama yang berada pada indeks yang sama.

Perintah self.table[index] = new_node digunakan untuk menjadikan node baru sebagai node pertama pada linked list di indeks tersebut.

Berikutnya terdapat fungsi search(self, key) yang digunakan untuk mencari data berdasarkan key.

Perintah index = self.hash_function(key) digunakan untuk menentukan lokasi pencarian data berdasarkan hasil hashing.

Perintah current = self.table[index] digunakan untuk mengambil node pertama pada indeks yang diperoleh.

Bagian while current is not None: digunakan untuk melakukan penelusuran linked list pada indeks tersebut.

Perintah if current.key == key: digunakan untuk memeriksa apakah key yang dicari sama dengan key yang terdapat pada node saat ini.

Perintah return current digunakan untuk mengembalikan node yang ditemukan sehingga informasi value dapat diakses.

Perintah current = current.next digunakan untuk berpindah ke node berikutnya apabila key belum ditemukan.

Perintah return None digunakan untuk menunjukkan bahwa data tidak ditemukan setelah seluruh linked list diperiksa.

Selanjutnya terdapat fungsi remove_key(self, key) yang digunakan untuk menghapus data berdasarkan key.

Perintah index = self.hash_function(key) digunakan untuk menentukan indeks tempat data berada.

Perintah current = self.table[index] digunakan untuk mengambil node pertama pada linked list.

Perintah prev = None digunakan untuk menyimpan node sebelumnya selama proses penelusuran linked list berlangsung.

Bagian while current is not None: digunakan untuk mencari node yang memiliki key sesuai dengan input pengguna.

Perintah if current.key == key: digunakan untuk memeriksa apakah key yang dicari telah ditemukan.

Bagian if prev is None: digunakan untuk memeriksa apakah node yang akan dihapus berada di posisi pertama linked list.

Perintah self.table[index] = current.next digunakan untuk memindahkan kepala linked list ke node berikutnya apabila node pertama dihapus.

Perintah prev.next = current.next digunakan untuk menghubungkan node sebelumnya dengan node setelah node yang dihapus sehingga linked list tetap tersambung.

Perintah return True digunakan untuk menandakan bahwa proses penghapusan berhasil dilakukan.

Perintah prev = current digunakan untuk menyimpan node saat ini sebagai node sebelumnya sebelum berpindah ke node berikutnya.

Perintah current = current.next digunakan untuk melanjutkan proses pencarian pada node berikutnya.

Perintah return False digunakan apabila key tidak ditemukan sehingga tidak ada data yang dapat dihapus.

Pada bagian berikut terdapat fungsi display(self) yang digunakan untuk menampilkan seluruh isi hash table.

Perintah print("\nIsi Hash Table:") digunakan untuk menampilkan judul hasil tampilan hash table.

Bagian for i in range(self.SIZE): digunakan untuk melakukan perulangan pada seluruh indeks hash table.

Perintah print(f"{i}: ", end="") digunakan untuk menampilkan nomor indeks yang sedang diproses.

Perintah current = self.table[i] digunakan untuk mengambil node pertama pada indeks tersebut.

Bagian while current is not None: digunakan untuk menampilkan seluruh node yang terdapat pada linked list di indeks tersebut.

Perintah print(f"({current.key},{current.value}) -> ", end="") digunakan untuk menampilkan pasangan key dan value yang tersimpan pada node.

Perintah current = current.next digunakan untuk berpindah ke node berikutnya hingga seluruh data berhasil ditampilkan.

Perintah print("NONE") digunakan untuk menandai akhir linked list pada setiap indeks hash table.

Pada bagian akhir program terdapat fungsi main() yang digunakan sebagai menu utama program.

Perintah hashmap = HashMapSeparateChaining() digunakan untuk membuat objek Hash Map yang akan digunakan selama program berjalan.

Perintah pilih = 0 digunakan untuk menyimpan pilihan menu dari pengguna.

Bagian while pilih != 5: digunakan agar menu terus ditampilkan sampai pengguna memilih opsi keluar.

Perintah print() digunakan untuk menampilkan daftar menu yang tersedia, yaitu Insert, Search, Delete, Display, dan Keluar.

Perintah pilih = int(input("Pilih: ")) digunakan untuk menerima pilihan menu dari pengguna.

Pada menu Insert, program meminta pengguna memasukkan key dan value, kemudian memanggil fungsi insert() untuk menyimpan data ke dalam Hash Map.

Pada menu Search, program meminta key yang ingin dicari, kemudian memanggil fungsi search() untuk mencari data dan menampilkan hasil pencarian.

Pada menu Delete, program meminta key yang akan dihapus, kemudian memanggil fungsi remove_key() untuk menghapus data dari Hash Map.

Pada menu Display, program memanggil fungsi display() untuk menampilkan seluruh isi hash table beserta linked list yang terbentuk akibat collision.

Pada menu Keluar, program menampilkan pesan bahwa program telah selesai dijalankan dan kemudian menghentikan seluruh proses.

**d. Output Program**:
<img width="1919" height="1079" alt="Cuplikan layar 2026-06-09 205659" src="https://github.com/user-attachments/assets/2c3c88c7-fd08-4e9a-9aca-4d5db1320541" />

Pada output program, tampilan pertama yang muncul adalah menu utama **Hash Map** yang berisi beberapa pilihan operasi, yaitu **Insert, Search, Delete, Display, dan Keluar**. Setelah menu ditampilkan, pengguna diminta memilih operasi yang ingin dijalankan dengan memasukkan nomor menu yang tersedia.

Ketika pengguna memilih menu **Insert**, program akan meminta pengguna memasukkan **key** dan **value** yang akan disimpan ke dalam Hash Map. Setiap data yang dimasukkan akan diproses menggunakan fungsi hash untuk menentukan indeks penyimpanannya pada hash table. Jika terdapat lebih dari satu data yang memiliki indeks yang sama, maka program akan menyimpan data tersebut menggunakan metode **Separate Chaining** dengan bantuan linked list sehingga tidak terjadi kehilangan data akibat collision.

Setelah beberapa data berhasil dimasukkan, pengguna dapat memilih menu **Display** untuk melihat seluruh isi hash table. Pada bagian ini, program akan menampilkan setiap indeks beserta data yang tersimpan di dalamnya. Jika terjadi collision, data-data yang berada pada indeks yang sama akan ditampilkan dalam bentuk rantai linked list. Tampilan ini bertujuan untuk memperlihatkan bagaimana Hash Map menyimpan dan mengelola data yang memiliki hasil hash yang sama.

Selanjutnya pengguna dapat memilih menu **Search** untuk mencari data berdasarkan key tertentu. Program akan menghitung indeks menggunakan fungsi hash, kemudian menelusuri linked list pada indeks tersebut hingga data ditemukan. Jika key yang dicari tersedia, program akan menampilkan value yang terkait dengan key tersebut. Namun jika data tidak ditemukan, program akan menampilkan pesan bahwa data tidak tersedia di dalam Hash Map.

Program juga menyediakan menu **Delete** yang digunakan untuk menghapus data berdasarkan key yang dimasukkan pengguna. Setelah key ditemukan, program akan menghapus node yang sesuai dari linked list dan memperbarui struktur data agar tetap tersusun dengan benar. Untuk memastikan proses penghapusan berhasil, pengguna dapat kembali memilih menu **Display** dan melihat bahwa data yang dihapus sudah tidak muncul lagi pada hash table.

Setelah seluruh operasi selesai dilakukan, pengguna dapat memilih menu **Keluar** untuk mengakhiri program. Program kemudian menampilkan pesan bahwa proses telah selesai dijalankan dan seluruh aktivitas pada Hash Map berakhir dengan baik. Dengan output tersebut, pengguna dapat memahami cara kerja Hash Map dalam menyimpan, mencari, menampilkan, dan menghapus data menggunakan metode Separate Chaining.

**e. Link YouTube**:
