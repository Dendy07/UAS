def inputan():
    from model.daftar_nilai import tambah_kontak
    while (True):
        nama = input("Nama\t\t: ")
    while (True):
        try:
            nim = int(input("NIM\t\t: "))
        else:
            break
    while (True):
        try:
            uts = int(input("Nilai UTS\t: "))
        else:
            break
    while (True):
        try:
            uas = int(input("Nilai UAS\t: "))
        else:
            break
    while (True):
        try:
            tugas = int(input("Nilai Tugas\t: "))
        else:
            break
    tambah_kontak(nama, nim, tugas, uts, uas)
    c = input("\n(L)ihat, (T)ambah, (U)bah), (H)apus, (C)ari, (K)eluar: ")

def ubah():
    from model.daftar_nilai import ubah_kontak
    print("Ubah Data")
        nama = input("Masukkan Nama   : ")
        if nama in data.keys():
            nim = int(input("NIM\t\t: "))
            uts = int(input("Nilai UTS\t: "))
            uas = int(input("Nilai UAS\t: "))
            tugas = int(input("Nilai Tugas\t: "))
            akhir = tugas*30/100 + uts*35/100 + uas*35/100
            data[nama] = nim, uts, uas, tugas, akhir
        else:
            print("Nama {0} tidak ditemukan".format(nama))


def hapus():
    from model.daftar_nilai import hapus
     print("Hapus Data")
        nama = input("Masukkan Nama  : ")
        if nama in data.keys():
            del data[nama]
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))
            
def cari():
    from model.daftar_nilai import cari
     print("Cari Data[case-sensitive]")
        nama = input("Masukkan Nama : ")
        if nama in data.keys():
            print("="*73)
            print("|                             Daftar Mahasiswa                          |")
            print("="*73)
            print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*73)
            print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                  .format(nama, nim, uts, uas, tugas, akhir))
            print("="*73)
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))
