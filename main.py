# Contact Management Program

import kontak

# kontak1 = {'nama' : "Andi", 'HP' : '081231848114', 'email' : "Andi@python.com"}
# kontak2 = {'nama' : "Ani", 'HP' : '083453732445', 'email' : "Ani@python.com"}
# kontak = [kontak1, kontak2]

def main():
    kontak_kantor = kontak.Kontak()
    kontak_keluarga = kontak.Kontak()

    while True:
        print("\nMenu Kontak")
        print("1. Melihat Semua Kontak")
        print("2. Menambahkan Kotak Baru")
        print("3. Menghapus Kontak")
        print("4. Keluar dari Kontak")

        pilihan = input("Masukkan pilihan menu kontak (1/2/3/4): ")
        print("========================================\n")

        if pilihan == '1':
            kontak_keluarga.melihat_kontak()
        elif pilihan == '2':
            kontak_keluarga.menambah_kontak()
        elif pilihan == '3':
            kontak_keluarga.menghapus_kontak()
        elif pilihan == '4':
            kontak_keluarga.keluar_kontak()
            break
        else:
            print("Anda memasukkan pilihan yang salah!")

if __name__ == "__main__":
    main()