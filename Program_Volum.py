'''
Program dengan fungsi untuk menghitung volume-volume
bangun ruang. Diantaranya
1. Kubus
2. Persegi panjang
3. Limas
4. Silinder
5. Lingkaran
'''

def Kubus():
    print('Hitung Volume Kubus :')
    sisi = int(input('Masukkan panjang sisi(cm): '))
    V = sisi*sisi*sisi
    print(f"Volume kubus : {V} cm3\n")

def Persegi_Panjang():
    print('Hitung Volume Persegi Panjang :')
    p = int(input('Masukkan panjang persegi(cm): '))
    l = int(input('Masukkan lebar persegi(cm): '))
    t = int(input('Masukkan tinggi persegi(cm): '))
    V = p*l*t
    print(f"Volume persegi panjang : {V} cm3\n")

def Limas():
    print('Hitung Volume Limas :')
    p = int(input('Masukkan panjang alas(cm): '))
    l = int(input('Masukkan lebar alas(cm): '))
    t = int(input('Masukkan tinggi limas(cm): '))
    V = (p*l*t)/3
    print(f"Volume limas : {V} cm3\n")

def Silinder():
    print('Hitung Volume Silinder :')
    r = int(input('Masukkan jari-jari tabung(cm): '))
    t = int(input('Masukkan tinggi tabung(cm): '))
    phi = 22/7
    V = (22*t*(r**2))/7
    print(f"Volume tabung : {V} cm3\n")

def Lingkaran():
    print('Hitung Volume Lingkaran :')
    r = int(input('Masukkan jari-jari lingkaran(cm): '))
    V = (3.14*4*(r*r*r))/3
    print(f"Volume lingkaran : {V} cm3\n")


if __name__ : "__main__"

while True :
    print('\nPROGRAM PENGHITUNG VOLUME BANGUN RUANG')
    print('======================================\n')
    print('1. Kubus\n2. Persegi Panjang\n3. Limas\n4. Silinder\n5. Lingkaran')
    pilih = input('Pilih Bangun Ruang : ')

    if (pilih == '1') :
        Kubus()
    elif (pilih == '2') :
        Persegi_Panjang()
    elif (pilih == '3') :
        Limas()
    elif (pilih == '4') :
        Silinder()
    elif (pilih == '5') :
        Lingkaran()
    else :
        print('Pilih opsi 1-5 ya, gengs')

    lagi = input("\nCari lagi (y/n) = ")
    if lagi == "n" :
        break

print('\n.........Terima kasih sudah mampir.........\n')