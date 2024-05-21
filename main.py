import main as db

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
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        db.tambah_data_barang()
    elif pilihan == "2":
        db.edit_data()
    elif pilihan == "3":
        db.hapus_data_barang()
    elif pilihan == "4":
        db.cari_data()
    elif pilihan == "5":
        db.tampilkan_data_barang()
    elif pilihan == "6":
        db.tampilkan_jumlah_data()
    elif pilihan == "7":
        print("Terima kasih telah menggunakan program Manajemen Stok Barang!")
        break
    else:
        print("Pilihan tidak valid!")
