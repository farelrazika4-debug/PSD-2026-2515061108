def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        print(f"Posisi tengah: {mid}, nilai: {data[mid]}")

        if data[mid] == target:
            return mid

        elif data[mid] < target:
            print("Mencari ke bagian kanan")
            left = mid + 1

        else:
            print("Mencari ke bagian kiri")
            right = mid - 1

    return -1


def main():

    data_buku = [101, 105, 110, 115, 120, 125, 130, 135, 140, 145]

    print("Data kode buku:")
    print(data_buku)

    try:
        target = int(input("Masukkan kode buku yang ingin dicari: "))

        hasil = binary_search(data_buku, target)

        if hasil != -1:
            print(f"Kode buku ditemukan pada indeks ke-{hasil}")
        else:
            print("Kode buku tidak ditemukan")

    except ValueError:
        print("Input harus berupa angka!")


if __name__ == "__main__":
    main()