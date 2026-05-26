## Implementasi Binary Search Tree (BST) Menggunakan Python

**a. Judul Program**:
Implementasi Binary Search Tree (BST) Menggunakan Python

**b. Deskripsi Singkat**:
Program Implementasi Operasi Dasar Binary Search Tree (BST) Menggunakan Python dibuat untuk menerapkan konsep struktur data Binary Search Tree, yaitu struktur data pohon biner yang memiliki aturan bahwa nilai pada anak kiri lebih kecil dari node induk dan nilai pada anak kanan lebih besar dari node induk. Program ini menggunakan class Node untuk membuat simpul dan class BST untuk mengelola operasi-operasi pada pohon. Dengan konsep tersebut, proses pencarian dan pengelolaan data dapat dilakukan lebih efisien dibandingkan pencarian secara berurutan.

Program ini menyediakan beberapa fitur utama, seperti insert untuk menambahkan data, search untuk mencari data, traversal (inorder, preorder, dan postorder), mencari **nilai minimum dan maksimum**, menghitung jumlah node, serta menjumlahkan seluruh isi node pada BST. Program dibuat menggunakan sistem menu interaktif sehingga pengguna dapat memilih operasi yang diinginkan dengan mudah. Dengan adanya fitur-fitur tersebut, program dapat membantu memahami cara kerja BST sekaligus mengimplementasikan konsep struktur data pohon dalam bahasa Python.

**c. Source Code**:

<img width="1258" height="7256" alt="code-snapshot judul 5" src="https://github.com/user-attachments/assets/94a9425b-de1d-475c-9977-ccff484034fc" />

Program diawali dengan pembuatan **class `Node`**. Class ini digunakan untuk membuat simpul (node) pada Binary Search Tree. Di dalam class terdapat fungsi `__init__(self, key)` yang digunakan untuk menerima nilai yang akan disimpan pada node. Variabel `self.key` digunakan untuk menyimpan data utama, sedangkan `self.left` dan `self.right` digunakan untuk menyimpan alamat anak kiri dan anak kanan. Nilai awal kedua variabel tersebut diatur `None`, karena saat node pertama kali dibuat node tersebut belum memiliki cabang.

Selanjutnya dibuat **class `BST`** yang berfungsi untuk mengatur seluruh proses pada Binary Search Tree. Pada fungsi `__init__(self)` terdapat variabel `self.root = None` yang digunakan untuk menyimpan node akar (root). Nilai `None` menandakan bahwa pohon masih kosong dan belum memiliki data.

Pada bagian berikut terdapat fungsi `insert_node(self, root, key)` yang digunakan untuk menambahkan data baru ke dalam Binary Search Tree secara rekursif. Parameter `root` digunakan untuk menunjukkan node yang sedang diperiksa, sedangkan parameter `key` digunakan untuk menerima data baru yang akan dimasukkan ke dalam pohon.

Baris `if root is None: return Node(key)` digunakan untuk memeriksa apakah posisi node saat ini kosong. Jika kosong, maka node baru akan dibuat dan langsung ditempatkan pada posisi tersebut. Hal ini menandakan bahwa lokasi penyisipan data telah ditemukan.

Baris `if key < root.key:` digunakan untuk membandingkan nilai data baru dengan node saat ini. Jika nilai yang dimasukkan lebih kecil dari node sekarang, maka data akan ditempatkan pada cabang kiri sesuai aturan Binary Search Tree.

Baris `root.left = self.insert_node(root.left, key)` digunakan untuk memanggil fungsi `insert_node()` secara rekursif menuju cabang kiri hingga menemukan posisi kosong yang sesuai.

Baris `elif key > root.key:` digunakan untuk memeriksa apakah nilai baru lebih besar daripada node saat ini. Jika kondisi tersebut benar, maka data akan diproses menuju sisi kanan pohon.

Baris `root.right = self.insert_node(root.right, key)` digunakan untuk melakukan proses rekursif pada anak kanan hingga ditemukan tempat yang tepat untuk menyimpan data.

Baris `return root` digunakan untuk mengembalikan node sehingga struktur pohon tetap tersusun dengan benar setelah proses penambahan data selesai dilakukan.

Fungsi `insert(self, key)` digunakan sebagai fungsi pemanggil agar pengguna cukup memasukkan data tanpa perlu menentukan posisi node secara manual. Pada baris `self.root = self.insert_node(self.root, key)` proses penyisipan dimulai dari akar pohon Binary Search Tree.

Selanjutnya terdapat fungsi `search_node(self, root, key)` yang digunakan untuk mencari data tertentu di dalam BST. Fungsi ini bekerja menggunakan konsep perbandingan nilai untuk menentukan arah pencarian.

Baris `if root is None: return False` digunakan untuk memeriksa apakah node saat ini kosong. Jika kosong berarti data yang dicari tidak ditemukan di dalam BST.

Baris `if root.key == key: return True` digunakan untuk memeriksa apakah data yang dicari sama dengan node saat ini. Jika sama, proses pencarian dihentikan karena data telah ditemukan.

Baris `if key < root.key:` digunakan untuk menentukan arah pencarian. Jika nilai yang dicari lebih kecil, maka proses pencarian akan dilanjutkan menuju cabang kiri BST.

Baris `return self.search_node(root.left, key)` digunakan untuk melakukan pencarian secara rekursif ke sisi kiri pohon.

Baris `return self.search_node(root.right, key)` digunakan untuk melakukan pencarian rekursif menuju cabang kanan apabila nilai lebih besar dari node saat ini.

Fungsi `inorder(self, root)` digunakan untuk melakukan traversal atau penelusuran data menggunakan metode Inorder. Pada metode ini urutan penelusuran dilakukan dari kiri, root, lalu kanan.

Baris `self.inorder(root.left)` digunakan untuk menelusuri seluruh cabang kiri terlebih dahulu. Setelah itu `print(root.key, end=" ")` digunakan untuk menampilkan node saat ini. Kemudian `self.inorder(root.right)` digunakan untuk menelusuri cabang kanan. Traversal Inorder menghasilkan data yang terurut dari nilai terkecil ke terbesar.

Fungsi `preorder(self, root)` digunakan untuk melakukan traversal menggunakan metode Preorder. Pada metode ini urutan traversal dilakukan dengan pola root, kiri, lalu kanan.

Baris `print(root.key, end=" ")` digunakan untuk menampilkan node saat ini terlebih dahulu. Setelah itu `self.preorder(root.left)` digunakan untuk menelusuri cabang kiri dan `self.preorder(root.right)` digunakan untuk menelusuri cabang kanan.

Fungsi `postorder(self, root)` digunakan untuk traversal dengan metode Postorder. Pada metode ini penelusuran dilakukan dengan urutan kiri, kanan, lalu root.

Baris `self.postorder(root.left)` digunakan untuk menelusuri sisi kiri terlebih dahulu, kemudian `self.postorder(root.right)` menelusuri sisi kanan, dan terakhir `print(root.key, end=" ")` digunakan untuk menampilkan node saat ini.

Fungsi `find_min(self, root)` digunakan untuk mencari nilai terkecil pada BST. Pada Binary Search Tree nilai terkecil selalu berada pada node paling kiri.

Baris `while current.left is not None:` digunakan untuk terus bergerak menuju cabang kiri sampai mencapai node terakhir. Setelah posisi terakhir ditemukan, baris `return current.key` digunakan untuk mengembalikan nilai terkecil.

Fungsi `find_max(self, root)` digunakan untuk mencari nilai terbesar pada BST. Nilai terbesar pada BST selalu berada pada node paling kanan.

Baris `while current.right is not None:` digunakan untuk bergerak terus menuju cabang kanan hingga node terakhir ditemukan. Setelah itu `return current.key` digunakan untuk mengembalikan nilai terbesar.

Fungsi `count_nodes(self, root)` digunakan untuk menghitung jumlah seluruh node pada BST.

Baris `return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)` digunakan untuk menjumlahkan node saat ini dengan jumlah node pada cabang kiri dan kanan. Nilai `1` merepresentasikan node yang sedang diproses.

Fungsi `sum_nodes(self, root)` digunakan untuk menghitung jumlah seluruh isi data pada BST.

Baris `return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)` digunakan untuk menjumlahkan nilai node saat ini dengan seluruh nilai node pada cabang kiri dan kanan.

Pada bagian akhir program terdapat fungsi `main()` yang digunakan sebagai menu utama program. Fungsi ini berisi pilihan operasi seperti insert, search, traversal, pencarian nilai minimum, nilai maksimum, menghitung jumlah node, serta menjumlahkan seluruh node. Menu tersebut mempermudah pengguna untuk berinteraksi dengan program Binary Search Tree melalui tampilan yang sederhana dan mudah digunakan.


**d. Output Program**:
<img width="945" height="314" alt="Cuplikan layar 2026-05-26 213931" src="https://github.com/user-attachments/assets/82388f06-cf1c-4a47-9bf6-b33edf516d7a" />

Pada output program, tampilan pertama yang muncul adalah menu utama **Binary Search Tree (BST)** yang berisi beberapa pilihan operasi seperti **Insert, Search, Inorder, Preorder, Postorder, Nilai Minimum, Nilai Maksimum, Hitung Node, Jumlah Seluruh Node**, dan **Keluar**. Setelah menu ditampilkan, pengguna diminta memilih operasi yang ingin dijalankan dengan memasukkan nomor menu yang tersedia.

Pada tahap awal, pengguna memilih menu **Insert** untuk memasukkan data ke dalam Binary Search Tree. Program akan meminta pengguna memasukkan nilai satu per satu. Data yang dimasukkan akan otomatis disusun berdasarkan aturan BST, yaitu nilai yang lebih kecil ditempatkan pada cabang kiri dan nilai yang lebih besar ditempatkan pada cabang kanan. Proses ini dilakukan secara berulang sampai pengguna selesai menambahkan data.

Setelah semua data berhasil dimasukkan, pengguna dapat memilih menu traversal seperti **Inorder**, **Preorder**, atau **Postorder**. Pada menu **Inorder**, data akan ditampilkan dari nilai terkecil ke terbesar. Pada menu **Preorder**, data ditampilkan dengan urutan akar, kiri, kemudian kanan. Sedangkan pada **Postorder**, data ditampilkan dengan urutan kiri, kanan, lalu akar. Bagian ini digunakan untuk melihat susunan data berdasarkan metode traversal yang berbeda.

Selain traversal, program juga menyediakan menu **Search** untuk mencari data tertentu pada BST. Pengguna hanya perlu memasukkan nilai yang ingin dicari, kemudian program akan menampilkan informasi apakah data ditemukan atau tidak. Program juga memiliki fitur untuk mencari **nilai minimum**, **nilai maksimum**, menghitung **jumlah node**, dan menjumlahkan seluruh isi node yang terdapat di dalam pohon.

Setelah seluruh proses selesai dilakukan, pengguna dapat memilih menu **Keluar** untuk mengakhiri program. Program kemudian menampilkan pesan bahwa proses telah selesai dijalankan dan seluruh operasi Binary Search Tree berakhir dengan baik.


**e. Link YouTube**:
