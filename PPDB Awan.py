import os
import time
import json
import csv

fileDataSiswa = 'dataSiswa.json'
fileSiswaLolos = 'lolos.csv'
fileSiswaGagal = 'gagal.csv'

hasilAkhir = []

nama = ''
nisn = ''
namaPrint = ''
nisnPrint = ''
jalur = 0
gagal = 0
bhss = ''

#zonasi
ipaZonasi = {'kZonasi1': [0], 'namaZonasi1': ['0'], 'jarak1': [1], 'nemZonasi1': [0]}
ipsZonasi = {'kZonasi2': [0], 'namaZonasi2': ['0'], 'jarak2': [1], 'nemZonasi2': [0]}
bhsZonasi = {'kZonasi3': [0], 'namaZonasi3': ['0'], 'jarak3': [1], 'nemZonasi3': [0]}

#reguler
ipaReguler = {'kReguler1': [0], 'namaReguler1': ['0'], 'umur1': [0], 'nemReguler1': [0]}
ipsReguler = {'kReguler2': [0], 'namaReguler2': ['0'], 'umur2': [0], 'nemReguler2': [0]}
bhsReguler = {'kReguler3': [0], 'namaReguler3': ['0'], 'umur3': [0], 'nemReguler3': [0]}

#prestasi
ipaPrestasi = {'kPrestasi1': [0], 'namaPrestasi1': ['0'], 'tingkatSertif1': [0], 'banyakSertif1': [0]}
ipsPrestasi = {'kPrestasi2': [0], 'namaPrestasi2': ['0'], 'tingkatSertif2': [0], 'banyakSertif2': [0]}

def hapusLayar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilan():
    hapusLayar()

    print("-" * 69)
    print("""
                        Selamat Datang di
                      Pendaftaran Siswa Baru
                         SMA Awan Ceria
""")
    print("-" * 69)
    print(namaPrint)
    print(nisnPrint)

def login():
    global nama, nisn, namaPrint, nisnPrint

    try:
        with open(fileDataSiswa, 'r') as dataSiswa:
            dataLogin = json.load(dataSiswa)
    except IOError as e:
        print(e)

    tampilan()

    print("Silakan Login")

    while True:
        nisnn = int(input("Masukkan NISN Anda     : "))
        passs = int(input("Masukkan Password Anda : "))
        time.sleep(0.5)
        print("")
        if nisnn in dataLogin['nisn']:
            indexNISN = dataLogin['nisn'].index(nisnn)
            if passs == dataLogin['pass'][indexNISN]:
                print("Login Berhasil")
                time.sleep(0.5)
                nama = dataLogin['nama'][indexNISN]
                nisn = dataLogin['nisn'][indexNISN]
                namaPrint = (f"Nama : {nama}")
                nisnPrint = (f"NISN : {nisn}")
                mainMenu()
                break
            else:
                print("Password Salah")
                time.sleep(0.5)
                login()
        else:
            print("NISN Tidak Ditemukan")
            time.sleep(0.5)
            login()
    
def mainMenu():
    global namaPrint, nisnPrint
    tampilan()

    print("""
Silakan Pilih Menu :
1] Daftar
2] Hasil
0] Logout
""")
    pilihMenu = int(input("Masukkan Nomor Pilihan : "))

    if pilihMenu == 1:
        daftar()
    elif pilihMenu == 2:
        hasil()
    elif pilihMenu == 0:
        namaPrint = ""
        nisnPrint = ""
        print("Keluar Akun")
        time.sleep(0.5)
        login()
    else:
        print("Menu Tidak Ada")
        time.sleep(0.5)
        mainMenu()

def daftar():
    global jalur, bhss
    tampilan()

    print("""
Silakan Pilih Jalur Pendaftaran :
1] Zonasi
2] Reguler
3] Prestasi
0] Kembali
""")
    pilihDaftar = int(input("Masukkan Nomor Pilihan : "))

    if pilihDaftar == 1:
        jalur = 1
        jurusan()
    elif pilihDaftar == 2:
        jalur = 2
        jurusan()
    elif pilihDaftar == 3:
        jalur = 3
        bhss = '(Tidak Tersedia)'
        jurusan()

def jurusan():
    tampilan()

    print(f"""
Silakan Pilih Jurusan Anda :
1] IPA
2] IPS
3] Bahasa {bhss}
""")
    pilihJurusan = int(input("Masukkan Nomor Pilihan : "))

    if pilihJurusan == 1:
        ipa()
    elif pilihJurusan == 2:
        ips()
    elif pilihJurusan == 3:
        if jalur == 3:
            jurusan()
        else:
            bhs()

#zonasi
gagalZonasi1 = []
gagalZonasi2 = []
gagalZonasi3 = []

def knapsackZonasi(kuotaZonasi, kZonasi, jarak, nemZonasi, n, hasilZonasi):
        if kuotaZonasi == 0 or n == 0:
            return 0
        if kZonasi[n-1] > kuotaZonasi:
            return knapsackZonasi(kuotaZonasi, kZonasi, jarak, nemZonasi, n-1, hasilZonasi)
        else:
            zonasiMax = len(hasilZonasi)
            maxx = nemZonasi[n-1] // jarak[n-1] + knapsackZonasi(kuotaZonasi-kZonasi[n-1], kZonasi, jarak, nemZonasi, n-1, hasilZonasi)

            zonasiMin = len(hasilZonasi)
            minn = knapsackZonasi(kuotaZonasi, kZonasi, jarak, nemZonasi, n-1, hasilZonasi)

            if maxx > minn:
                if len(hasilZonasi) > zonasiMin:
                    del hasilZonasi[zonasiMin:len(hasilZonasi)]
                hasilZonasi.append(int(n-1))
                return maxx
            else:
                if zonasiMin > zonasiMax:
                    del hasilZonasi[zonasiMax:zonasiMin]
                return minn

#reguler
gagalReguler1 = []
gagalReguler2 = []
gagalReguler3 = []
def knapsackReguler(kuotaReguler, kReguler, nemReguler, umur, n, hasilReguler):
    if kuotaReguler == 0 or n == 0:
        return 0
    if kReguler[n-1]>kuotaReguler:
        return knapsackReguler(kuotaReguler,kReguler,nemReguler,umur,n-1,hasilReguler)
    else:
        regulerMaxx = len(hasilReguler)
        maxx = nemReguler[n-1] + umur[n-1] + knapsackReguler(kuotaReguler-kReguler[n-1], kReguler, nemReguler, umur, n-1, hasilReguler)

        regulerMinn = len(hasilReguler)
        minn = knapsackReguler(kuotaReguler, kReguler, nemReguler, umur, n-1, hasilReguler)
        if maxx > minn:
          if len(hasilReguler) > regulerMinn:
              del hasilReguler[regulerMinn:len(hasilReguler)]
          hasilReguler.append(int(n-1))
          return maxx
        else:
          if regulerMinn > regulerMaxx:
              del hasilReguler[regulerMaxx:regulerMinn]
          return minn

#prestasi
gagalPrestasi1 = []
gagalPrestasi2 = []
def knapsackPrestasi(kuotaPrestasi, kPrestasi, tingkatSertif, banyakSertif, n, hasilPrestasi):
    if kuotaPrestasi == 0 or n == 0:
        return 0
    if kPrestasi[n-1] > kuotaPrestasi:
        return knapsackPrestasi(kuotaPrestasi, kPrestasi, tingkatSertif, banyakSertif, n-1, hasilPrestasi)
    else:
        prestasiMax = len(hasilPrestasi)
        maxx = banyakSertif[n-1] * tingkatSertif[n-1] + knapsackPrestasi(kuotaPrestasi-kPrestasi[n-1], kPrestasi, tingkatSertif, banyakSertif, n-1, hasilPrestasi)

        prestasiMin = len(hasilPrestasi)
        minn = knapsackPrestasi(kuotaPrestasi, kPrestasi, tingkatSertif, banyakSertif, n-1, hasilPrestasi)

        if maxx > minn:
            if len(hasilPrestasi) > prestasiMin:
                del hasilPrestasi[prestasiMin:len(hasilPrestasi)]
            hasilPrestasi.append(int(n-1))
            return maxx
        else:
            if prestasiMin > prestasiMax:
                del hasilPrestasi[prestasiMax:prestasiMin]
            return minn

def tulisData():
    try:
        field = ["Nama", "NISN", "Jurusan", "Jalur Pendaftaran", "Keterangan"]

        with open(fileSiswaLolos, 'w', newline='') as fileTulis:
            tulis = csv.DictWriter(fileTulis, fieldnames=field)
            tulis.writeheader()
            tulis.writerows(hasilAkhir)
    except IOError as e:
        print(e)
    
    hapusData()

def hapusData():
    global gagal
    field = ['Nama', 'NISN', 'Jurusan', 'Jalur Pendaftaran', 'Keterangan']
    daftarHapus = []
    daftarBaru = []

    try:
        with open(fileSiswaLolos, 'r') as fileBaca:
            baca = csv.DictReader(fileBaca, delimiter=',')
            for i in baca:
                if i['Nama'] in gagalZonasi1:
                    daftarHapus.append(i)
                    continue
                elif i['Nama'] in gagalZonasi2:
                    daftarHapus.append(i)
                    continue
                elif i['Nama'] in gagalZonasi3:
                    daftarHapus.append(i)
                    continue
                elif i['Nama'] in gagalReguler1:
                    daftarHapus.append(i)
                    continue
                elif i['Nama'] in gagalReguler2:
                    daftarHapus.append(i)
                    continue
                elif i['Nama'] in gagalReguler3:
                    daftarHapus.append(i)
                    continue
                elif i['Nama'] in gagalPrestasi1:
                    daftarHapus.append(i)
                    continue
                elif i['Nama'] in gagalPrestasi2:
                    daftarHapus.append(i)
                    continue
                else:
                    daftarBaru.append(i)
    except IOError as e:
        print(e)
    
    if len(daftarHapus) == 0:
        print("")
    else:
        try:
            with open(fileSiswaLolos, 'w', newline='') as fileTulis:
                tulis = csv.DictWriter(fileTulis, fieldnames=field)
                tulis.writeheader()
                tulis.writerows(daftarBaru)
        except IOError as e:
            print(e)
        try:
            gagal = 1
            with open(fileSiswaGagal, 'w', newline='') as fileTulis:
                tulis = csv.DictWriter(fileTulis, fieldnames=field)
                tulis.writeheader()
                tulis.writerows(daftarHapus)
        except IOError as e:
            print(e)
    
    hasil()

def ipa():
    global hasilAkhir, gagalZonasi1, gagalReguler1, gagalPrestasi1

    if jalur == 1:
        jarakk = int(input("Masukkan Jarak Rumah Anda ke Sekolah (KM) : "))
        nemmZonasi = int(input("Masukkan Nilai Ebtanas Murni Anda         : "))

        ipaZonasi['kZonasi1'].append(1)
        ipaZonasi['namaZonasi1'].append(nama)
        ipaZonasi['jarak1'].append(jarakk)
        ipaZonasi['nemZonasi1'].append(nemmZonasi)

        kuotaZonasi = 2
        kZonasi = ipaZonasi['kZonasi1']
        namaZonasi = ipaZonasi['namaZonasi1']
        jarak = ipaZonasi['jarak1']
        nemZonasi = ipaZonasi['nemZonasi1']

        hasilZonasi = list()
        gagalZonasi1 = list()

        n = len(ipaZonasi['kZonasi1'])
        knapsackZonasi(kuotaZonasi, kZonasi, jarak, nemZonasi, n, hasilZonasi)

        for i in range(n):
            if i not in hasilZonasi:
                gagalZonasi1.append(namaZonasi[i])
        
        dataCSV = {'Nama': nama, 'NISN': nisn, 'Jurusan': 'IPA', 'Jalur Pendaftaran': 'ZONASI'}
        hasilAkhir.append(dataCSV)

        tulisData()
    
    if jalur == 2:
        umurr = int(input("Masukkan Umur Anda                : "))
        nemmReguler = int(input("Masukkan Nilai Ebtanas Murni Anda : "))

        ipaReguler['kReguler1'].append(1)
        ipaReguler['namaReguler1'].append(nama)
        ipaReguler['umur1'].append(umurr)
        ipaReguler['nemReguler1'].append(nemmReguler)

        kuotaReguler = 1
        kReguler = ipaReguler['kReguler1']
        namaReguler = ipaReguler['namaReguler1']
        umur = ipaReguler['umur1']
        nemReguler = ipaReguler['nemReguler1']

        hasilReguler = list()
        gagalReguler1 = list()

        n = len(ipaReguler['kReguler1'])
        knapsackReguler(kuotaReguler, kReguler, nemReguler, umur, n, hasilReguler)
        
        for i in range(n):
            if i not in hasilReguler:
                gagalReguler1.append(namaReguler[i])
        
        dataCSV = {'Nama': nama, 'NISN': nisn, 'Jurusan': 'IPA', 'Jalur Pendaftaran': 'REGULER'}
        hasilAkhir.append(dataCSV)
        
        tulisData()
    
    if jalur == 3:
        tampilan()
        print("""
Nilai Tiap Tingkatan Sertif :
1] Nasional : 10
2] Provinsi : 7
3] Kabupaten : 4
""")
        tingkatanSertiff = int(input("Masukkan Tingkatan Sertifikat Anda     : "))
        banyakSertiff = int(input("Masukkan Banyaknya Sertifikat Dimiliki : "))

        tingkatanSertif = 0

        if tingkatanSertiff == 1:
            tingkatanSertif = 10
        elif tingkatanSertiff == 2:
            tingkatanSertif = 7
        elif tingkatanSertiff == 3:
            tingkatanSertif = 4

        ipaPrestasi['kPrestasi1'].append(1)
        ipaPrestasi['namaPrestasi1'].append(nama)
        ipaPrestasi['tingkatSertif1'].append(tingkatanSertif)
        ipaPrestasi['banyakSertif1'].append(banyakSertiff)

        kuotaPrestasi = 1
        kPrestasi = ipaPrestasi['kPrestasi1']
        namaPrestasi = ipaPrestasi['namaPrestasi1']
        tingkatSertif = ipaPrestasi['tingkatSertif1']
        banyakSertif = ipaPrestasi['banyakSertif1']

        hasilPrestasi = list()
        gagalPrestasi1 = list()

        n = len(ipaPrestasi['kPrestasi1'])
        knapsackPrestasi(kuotaPrestasi, kPrestasi, tingkatSertif, banyakSertif, n, hasilPrestasi)
        
        for i in range(n):
            if i not in hasilPrestasi:
                gagalPrestasi1.append(namaPrestasi[i])
        
        dataCSV = {'Nama': nama, 'NISN': nisn, 'Jurusan': 'IPA', 'Jalur Pendaftaran': 'PRESTASI'}
        hasilAkhir.append(dataCSV)

        tulisData()

def ips():
    global hasilAkhir, gagalZonasi2, gagalReguler2, gagalPrestasi2
    if jalur == 1:
        jarakk = int(input("Masukkan Jarak Rumah Anda ke Sekolah (KM) : "))
        nemmZonasi = int(input("Masukkan Nilai Ebtanas Murni Anda         : "))

        ipsZonasi['kZonasi2'].append(1)
        ipsZonasi['namaZonasi2'].append(nama)
        ipsZonasi['jarak2'].append(jarakk)
        ipsZonasi['nemZonasi2'].append(nemmZonasi)

        kuotaZonasi = 2
        kZonasi = ipsZonasi['kZonasi2']
        namaZonasi = ipsZonasi['namaZonasi2']
        jarak = ipsZonasi['jarak2']
        nemZonasi = ipsZonasi['nemZonasi2']

        hasilZonasi = list()
        gagalZonasi2 = list()

        n = len(ipsZonasi['kZonasi2'])
        knapsackZonasi(kuotaZonasi, kZonasi, jarak, nemZonasi, n, hasilZonasi)
        
        for i in range(n):
            if i not in hasilZonasi:
                gagalZonasi2.append(namaZonasi[i])
        
        dataCSV = {'Nama': nama, 'NISN': nisn, 'Jurusan': 'IPS', 'Jalur Pendaftaran': 'ZONASI'}
        hasilAkhir.append(dataCSV)

        tulisData()
    
    if jalur == 2:
        umurr = int(input("Masukkan Umur Anda                : "))
        nemmReguler = int(input("Masukkan Nilai Ebtanas Murni Anda : "))

        ipsReguler['kReguler2'].append(1)
        ipsReguler['namaReguler2'].append(nama)
        ipsReguler['umur2'].append(umurr)
        ipsReguler['nemReguler2'].append(nemmReguler)

        kuotaReguler = 1
        kReguler = ipsReguler['kReguler2']
        namaReguler = ipsReguler['namaReguler2']
        umur = ipsReguler['umur2']
        nemReguler = ipsReguler['nemReguler2']

        hasilReguler = list()
        gagalReguler2 = list()

        n = len(ipsReguler['kReguler2'])
        knapsackReguler(kuotaReguler, kReguler, nemReguler, umur, n, hasilReguler)
        
        for i in range(n):
            if i not in hasilReguler:
                gagalReguler2.append(namaReguler[i])
        
        dataCSV = {'Nama': nama, 'NISN': nisn, 'Jurusan': 'IPS', 'Jalur Pendaftaran': 'REGULER'}
        hasilAkhir.append(dataCSV)

        tulisData()
    
    if jalur == 3:
        tampilan()
        print("""
Nilai Tiap Tingkatan Sertif :
1] Nasional : 10
2] Provinsi : 7
3] Kabupaten : 4
""")
        tingkatanSertiff = int(input("Masukkan Tingkatan Sertifikat Anda     : "))
        banyakSertiff = int(input("Masukkan Banyaknya Sertifikat Dimiliki : "))

        tingkatanSertif = 0

        if tingkatanSertiff == 1:
            tingkatanSertif = 10
        elif tingkatanSertiff == 2:
            tingkatanSertif = 7
        elif tingkatanSertiff == 3:
            tingkatanSertif = 4

        ipsPrestasi['kPrestasi2'].append(1)
        ipsPrestasi['namaPrestasi2'].append(nama)
        ipsPrestasi['tingkatSertif2'].append(tingkatanSertif)
        ipsPrestasi['banyakSertif2'].append(banyakSertiff)

        kuotaPrestasi = 1
        kPrestasi = ipsPrestasi['kPrestasi2']
        namaPrestasi = ipsPrestasi['namaPrestasi2']
        tingkatSertif = ipsPrestasi['tingkatSertif2']
        banyakSertif = ipsPrestasi['banyakSertif2']

        hasilPrestasi = list()
        gagalPrestasi2 = list()

        n = len(ipsPrestasi['kPrestasi2'])
        knapsackPrestasi(kuotaPrestasi, kPrestasi, tingkatSertif, banyakSertif, n, hasilPrestasi)
        
        for i in range(n):
            if i not in hasilPrestasi:
                gagalPrestasi2.append(namaPrestasi[i])
        
        dataCSV = {'Nama': nama, 'NISN': nisn, 'Jurusan': 'IPS', 'Jalur Pendaftaran': 'PRESTASI'}
        hasilAkhir.append(dataCSV)

        tulisData()

def bhs():
    global hasilAkhir, gagalZonasi3, gagalReguler3

    if jalur == 1:
        jarakk = int(input("Masukkan Jarak Rumah Anda ke Sekolah (KM) : "))
        nemmZonasi = int(input("Masukkan Nilai Ebtanas Murni Anda         : "))

        bhsZonasi['kZonasi3'].append(1)
        bhsZonasi['namaZonasi3'].append(nama)
        bhsZonasi['jarak3'].append(jarakk)
        bhsZonasi['nemZonasi3'].append(nemmZonasi)

        kuotaZonasi = 1
        kZonasi = bhsZonasi['kZonasi3']
        namaZonasi = bhsZonasi['namaZonasi3']
        jarak = bhsZonasi['jarak3']
        nemZonasi = bhsZonasi['nemZonasi3']

        hasilZonasi = list()
        gagalZonasi3 = list()

        n = len(bhsZonasi['kZonasi3'])
        knapsackZonasi(kuotaZonasi, kZonasi, jarak, nemZonasi, n, hasilZonasi)
        
        for i in range(n):
            if i not in hasilZonasi:
                gagalZonasi3.append(namaZonasi[i])
        
        dataCSV = {'Nama': nama, 'NISN': nisn, 'Jurusan': 'BHS', 'Jalur Pendaftaran': 'ZONASI'}
        hasilAkhir.append(dataCSV)

        tulisData()
    
    if jalur == 2:
        umurr = int(input("Masukkan Umur Anda                : "))
        nemmReguler = int(input("Masukkan Nilai Ebtanas Murni Anda : "))

        bhsReguler['kReguler3'].append(1)
        bhsReguler['namaReguler3'].append(nama)
        bhsReguler['umur3'].append(umurr)
        bhsReguler['nemReguler3'].append(nemmReguler)

        kuotaReguler = 1
        kReguler = bhsReguler['kReguler3']
        namaReguler = bhsReguler['namaReguler3']
        umur = bhsReguler['umur3']
        nemReguler = bhsReguler['nemReguler3']

        hasilReguler = list()
        gagalReguler3 = list()

        n = len(bhsReguler['kReguler3'])
        knapsackReguler(kuotaReguler, kReguler, nemReguler, umur, n, hasilReguler)
        
        for i in range(n):
            if i not in hasilReguler:
                gagalReguler3.append(namaReguler[i])
        
        dataCSV = {'Nama': nama, 'NISN': nisn, 'Jurusan': 'BHS', 'Jalur Pendaftaran': 'REGULER'}
        hasilAkhir.append(dataCSV)

        tulisData()

def hasil():
    hapusLayar()

    try:
        with open(fileSiswaLolos, 'r') as fileBaca:
            baca = csv.DictReader(fileBaca, delimiter=',')
            print('-' * 69)
            print(f"|\tNAMA \t\t NISN \t JURUSAN    JALUR      KETERANGAN   |")
            print('-' * 69)
            for i in baca:
                print(f"|   {i['Nama']} \t {i['NISN']} \t   {i['Jurusan']}\t    {i['Jalur Pendaftaran']} \t LULUS      |")
            print("")
    except IOError as e:
        print(e)
    
    if gagal == 1:
        try:
            with open(fileSiswaGagal, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                for i in baca:
                    print(f"|   {i['Nama']} \t {i['NISN']} \t   {i['Jurusan']}\t    {i['Jalur Pendaftaran']} \tTDK LULUS   |")
                print("")
        except IOError:
            print("")
    else:
        print("")

    input("Tekan Enter Untuk Kembali...")
    mainMenu()

if __name__ == "__main__":
    login()