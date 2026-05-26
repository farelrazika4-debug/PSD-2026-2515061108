def insertion_sort_kopi(data_kopi, n):
    for i in range(1, n):
        temp = data_kopi[i]
        j = i - 1

        while j >= 0 and data_kopi[j]["harga"] > temp["harga"]:
            data_kopi[j + 1] = data_kopi[j]
            j -= 1

        data_kopi[j + 1] = temp


def main():
    print("=== SISTEM PENGURUTAN HARGA KOPI COFFEE SHOP ===")

    try:
        n = int(input("Masukkan jumlah data kopi: "))
    except ValueError:
        print("Input tidak valid!")
        return

    data_kopi = []

    for i in range(n):
        print(f"\nData kopi ke-{i+1}")

        nama = input("Masukkan nama kopi: ")

        while True:
            try:
                harga = int(input("Masukkan harga kopi: "))
                break
            except ValueError:
                print("Harga harus berupa angka!")

        data_kopi.append({
            "nama": nama,
            "harga": harga
        })

    print("\nData sebelum diurutkan:")
    for kopi in data_kopi:
        print(f"{kopi['nama']} - Rp{kopi['harga']}")

    insertion_sort_kopi(data_kopi, n)

    print("\nData setelah diurutkan (termurah → termahal):")
    for kopi in data_kopi:
        print(f"{kopi['nama']} - Rp{kopi['harga']}")


if __name__ == "__main__":
    main()