# Contact Management Program

def membuka_kontak(path='kontak.txt'):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak

def menyimpan_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)

class Kontak:
    def __init__(self):
        self.kontak = membuka_kontak()
    def melihat_kontak(self):
        # melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item)
                # print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")
            return 1
    def menambah_kontak(self):
        # menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor hp kontak yang baru: ")
        email = input("Masukkan email kontak yang baru: ")
        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        # kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil di tambahkan")
    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("\nMasukkan nomor kontak yang akan di hapus: "))
                del self.kontak[i_hapus - 1]
                print(f'Kontak yang dimaksud sudah di hapus')
            except:
                print("Nomor yang anda masukkan salah!")

    def keluar_kontak(self):
        menyimpan_kontak(isi=self.kontak)

# kontak1 = {'nama' : "Andi", 'HP' : '081231848114', 'email' : "Andi@python.com"}
# kontak2 = {'nama' : "Ani", 'HP' : '083453732445', 'email' : "Ani@python.com"}
# kontak = [kontak1, kontak2]

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

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

