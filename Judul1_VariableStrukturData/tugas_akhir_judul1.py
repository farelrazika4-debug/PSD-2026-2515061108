def menu():
    print("\n=== SISTEM NILAI MAHASISWA ===")
    print("1. Tampilkan address array")
    print("2. Tampilkan address semua indeks")
    print("3. Input nilai mahasiswa")
    print("4. Tampilkan nilai")
    print("5. Keluar")


def main():
    nilai = [0] * 5
    running = True

    while running:
        menu()

        try:
            pilihan = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if pilihan == 1:
            print(f"Address array: {id(nilai)}")

        elif pilihan == 2:
            for i in range(5):
                print(f"Address nilai[{i}] : {id(nilai[i])}")

        elif pilihan == 3:
            print("Masukkan nilai mahasiswa:")

            for i in range(5):
                while True:
                    try:
                        nilai[i] = int(
                            input(f"Nilai mahasiswa ke-{i+1}: "))
                        break
                    except ValueError:
                        print("Input harus angka!")

        elif pilihan == 4:
            print("\nDaftar Nilai Mahasiswa")

            for i in range(5):
                print(f"Mahasiswa {i+1}: {nilai[i]}")

        elif pilihan == 5:
            running = False
            print("Program selesai")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()