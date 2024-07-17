'Berisi class kontak menjalankan program kontak'

import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()
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
        dokumen.menyimpan_kontak(isi=self.kontak)