data = []

def insert():
    nama = input('nama barang = ')
    stok = int(input('stok barang = '))
    data.append({'nama': nama, 'stok': stok})

def edit():
    id = int(input('masukan data yang ke berapa'))
    if 0 <= id < len(data):
        nama = input('nama barang = ')
        stok = int(input('stok barang = '))
        data[id] = {'nama': nama, 'stok': stok}
    else:
        print('data tidak ditemukan')

def delete():
    id = int(input('masukan data yang ke berapa'))
    if 0 <= id < len(data):
        del data[id]
        print('hapus data berhasil')
    else:
        print('data tidak ditemukan')

def search():
    nama = input('cari nama barang = ')
    for i, item in enumerate(data):
        if item['nama'] == nama:
            print(f'data ke {i}')
            return
    print('data tidak ditemukan')

def view():
    for i, item in enumerate(data):
        print(f'{i+1}. {item["nama"]} ({item["stok"]})')

def total():
    print(f'jumlah data: {len(data)}')

def main():
    while True:
        print("Selamat datang di program Manajemen Stok Barang!")
        print("Pilihan:")
        print("1. Tambah Data Barang")
        print("2. Edit Data")
        print("3. Hapus Data Barang")
        print("4. Cari Data")
        print("5. Tampilkan Data Barang")
        print("6. Tampilkan Jumlah Data")
        print("7. Keluar")
        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            insert()
        elif pilihan == 2:
            edit()
        elif pilihan == 3:
            delete()
        elif pilihan == 4:
            search()
        elif pilihan == 5:
            view()
        elif pilihan == 6:
            total()
        elif pilihan == 7:
            print("Terima kasih telah menggunakan program Manajemen Stok Barang!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "_main_":

    main()