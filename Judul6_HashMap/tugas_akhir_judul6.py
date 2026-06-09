class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)

        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return

            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)

        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current

            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)

        current = self.table[index]
        prev = None

        while current is not None:

            if current.key == key:

                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next

                return True

            prev = current
            current = current.next

        return False

    def display(self):

        print("\nIsi Hash Table:")

        for i in range(self.SIZE):

            print(f"{i}: ", end="")

            current = self.table[i]

            while current is not None:
                print(f"({current.key},{current.value}) -> ",
                      end="")
                current = current.next

            print("NONE")


def main():

    hashmap = HashMapSeparateChaining()

    pilih = 0

    while pilih != 5:

        print("\n=== HASH MAP ===")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:

            try:
                key = int(input("Masukkan Key : "))
                value = int(input("Masukkan Value : "))

                hashmap.insert(key, value)

                print("Data berhasil ditambahkan")

            except ValueError:
                print("Input harus berupa angka")

        elif pilih == 2:

            try:
                key = int(input("Cari Key : "))

                hasil = hashmap.search(key)

                if hasil is not None:
                    print(f"Data ditemukan -> Value = {hasil.value}")
                else:
                    print("Data tidak ditemukan")

            except ValueError:
                print("Input harus berupa angka")

        elif pilih == 3:

            try:
                key = int(input("Hapus Key : "))

                if hashmap.remove_key(key):
                    print("Data berhasil dihapus")
                else:
                    print("Data tidak ditemukan")

            except ValueError:
                print("Input harus berupa angka")

        elif pilih == 4:
            hashmap.display()

        elif pilih == 5:
            print("Program selesai")

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()