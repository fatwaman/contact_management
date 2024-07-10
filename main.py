#Program Manajemen Kontak

def melihat_kontak():
    # melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Kontak masih kosong!")
        return 1

def menambah_kontak():
    # menambahkan kontak
    nama = input("Masukkan nama kontak yang baru: ")
    HP = input("Masukkan nomor hp kontak yang baru: ")
    email = input("Masukkan email kontak yang baru: ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil di tambahkan")

def menghapus_kontak():
    # menghapus kontak
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("\nMasukkan nomor kontak yang akan di hapus: "))
        del kontak[i_hapus - 1]
        print(f'Kontak yang dimaksud sudah di hapus')

kontak1 = {'nama' : "Andi", 'HP' : '081231848114', 'email' : "Andi@python.com"}
kontak2 = {'nama' : "Ani", 'HP' : '083453732445', 'email' : "Ani@python.com"}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kotak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1/2/3/4): ")
    print("========================================\n")

    if pilihan == '1':
        melihat_kontak()
    elif pilihan == '2':
        menambah_kontak()
    elif pilihan == '3':
        menghapus_kontak()
    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah!")

