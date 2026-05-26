class StackArray:
    def __init__(self, max_size=10):
        self.MAX = max_size
        self.stack = [None] * self.MAX
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.MAX - 1

    def push(self, lagu):
        if self.is_full():
            print("Riwayat lagu penuh!")
            return

        self.top += 1
        self.stack[self.top] = lagu
        print(f"Lagu '{lagu}' berhasil ditambahkan")

    def pop(self):
        if self.is_empty():
            print("Riwayat lagu kosong!")
            return

        lagu = self.stack[self.top]
        print(f"Lagu '{lagu}' dihapus dari riwayat")
        self.top -= 1

    def peek(self):
        if self.is_empty():
            print("Riwayat lagu kosong!")
            return

        print("Lagu terakhir diputar:",
              self.stack[self.top])

    def display(self):
        if self.is_empty():
            print("Riwayat kosong")
            return

        print("\nRiwayat Lagu:")
        for i in range(self.top, -1, -1):
            print("-", self.stack[i])


def main():
    musik = StackArray()

    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM RIWAYAT LAGU ===")
        print("1. Tambah Lagu")
        print("2. Hapus Lagu Terakhir")
        print("3. Lihat Lagu Terakhir")
        print("4. Tampilkan Riwayat")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))

            if pilih == 1:
                lagu = input("Masukkan judul lagu: ")
                musik.push(lagu)

            elif pilih == 2:
                musik.pop()

            elif pilih == 3:
                musik.peek()

            elif pilih == 4:
                musik.display()

            elif pilih == 5:
                print("Program selesai")

            else:
                print("Pilihan tidak tersedia")

        except ValueError:
            print("Input harus angka!")


if __name__ == "__main__":
    main()