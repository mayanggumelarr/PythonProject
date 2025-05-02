# Function membuat program menjado lebih ringkas

def kecepatan():
    v = s/t
    print (v)

def jarak():
    s = v*t
    print(s)

def waktu():
    t = s/v
    print(t)


while True :
    cari = input("\nWhat are you figure out (v/s/t) = ")

    if cari == "v" :
        s = float(input("Masukkan jarak s (km) = "))
        t = float(input("masukkan waktu t (jam) = "))
        kecepatan()
    elif cari == "s" :
        v = float(input("masukkan kecepatan v (km/jam) = "))
        t = float(input("masukkan waktu t (jam) = "))
        jarak()
    elif cari == "t" :
        s = float(input("Masukkan jarak s (km) = "))
        v = float(input("masukkan kecepatan v (km/jam) = "))
        waktu()

    lagi = input("Cari lagi (y/n) = ")
    if lagi == "n" :
        break

print("terima kasih telah mampir")
