from tkinter import *                                                                           # pustaka Py untuk menampilkan GUI
import tkinter.font as font                                                                     # atur dan ganti font
import math
import numpy as np

# variabel awal umum
root = Tk()                                                                                     # Buat jendela utama aplikasi
root.title("MY MATCHA CALCULATOR")                                                                        # beri judul utama jendela
root.geometry("310x400")                                                                        # ukuran jendela dalam pixel
root['bg'] = "#a4b465"                                                                          # atur warna latar belakang jendela


myfont = font.Font(size = 50)                                                                   # atur ukuran font jadi 15

# Entry page
e = Entry(root, width=35, justify= "right", borderwidth=0)                                      # membuat kotak teks tempat angka dan hasil perhitungan
e["font"] = myfont                                                                              # menerapkan ukuran font ke kotak teks
e["bg"] = "#f5ecd5"                                                                             # latar belakang kotak teks
e.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky='we')                              # menempatkan kotak teks di atas tampilan dengan jarak tertentu
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# button page
def angka(nilai):
    before = e.get()
    e.delete(0,END)
    e.insert(0, str(before) + str(nilai))

def hasil():
    try:
        num_akhir = float(e.get())
        e.delete(0, END)
        if math == "penjumlahan":
            e.insert(0, n_awal + float(num_akhir))
        elif math == "pengurangan":
            e.insert(0, n_awal - float(num_akhir))
        elif math == "perkalian":
            e.insert(0, n_awal * float(num_akhir))
        elif math == "pembagian":
            if num_akhir != 0:
                e.insert(0, n_awal / float(num_akhir))
            else :
                e.insert(0, "Error")
    except:
        e.insert(0, "Wrong Input")

def tambah():
    num_awal = float(e.get())
    global n_awal
    global math
    math = "penjumlahan"
    n_awal = float(num_awal)
    e.delete(0, END)

def kurang():
    num_awal = float(e.get())
    global n_awal
    global math
    math = "pengurangan"
    n_awal = float(num_awal)
    e.delete(0, END)

def kali():
    num_awal = float(e.get())
    global n_awal
    global math
    math = "perkalian"
    n_awal = float(num_awal)
    e.delete(0, END)

def bagi():
    num_awal = float(e.get())
    global n_awal
    global math
    math = "pembagian"
    n_awal = float(num_awal)
    e.delete(0, END)

def persen():
    curr = e.get()
    try:
        hasil = float(curr)/100
        e.delete(0, END)
        e.insert(0, hasil)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

def hapus():    # hapus per angka
    curr = e.get()
    e.delete(0, END)
    e.insert(0, curr[:-1])

def clear():    # hapus all
    e.delete(0, END)

def koma():
    curr = e.get()
    if "." not in curr.split()[:-1]: # biar tidak ada dua titik dalam satu angka
        e.insert(END, ".")

def akar():
    try:
        nilai = float(e.get())
        hasil = np.sqrt(nilai)
        e.delete(0, END)
        e.insert(0, float(hasil))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")

myfontButton = font.Font(size=15, weight="bold")

btn1 = Button(root, text="1", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=lambda:angka(1))
btn2 = Button(root, text="2", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=lambda:angka(2))
btn3 = Button(root, text="3", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=lambda:angka(3))
btn4 = Button(root, text="4", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=lambda:angka(4))
btn5 = Button(root, text="5", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=lambda:angka(5))
btn6 = Button(root, text="6", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=lambda:angka(6))
btn7 = Button(root, text="7", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=lambda:angka(7))
btn8 = Button(root, text="8", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=lambda:angka(8))
btn9 = Button(root, text="9", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=lambda:angka(9))
btn0 = Button(root, text="0", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=lambda:angka(0))
kar = Button(root, text="√", padx= 27, pady=20, bg="#f5ecd5", font=myfontButton, command=akar)
kom = Button(root, text=",", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=koma)
sama = Button(root, text="=", padx= 30, pady=20, bg="#f0bb78", font=myfontButton, command=hasil)
tam = Button(root, text="+", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=tambah)
kur = Button(root, text="-", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=kurang)
kal = Button(root, text="×", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=kali)
bag = Button(root, text="÷", padx= 30, pady=20, bg="#f5ecd5", font=myfontButton, command=bagi)
per = Button(root, text="%", padx= 28, pady=20, bg="#f5ecd5", font=myfontButton, command=persen)
hap = Button(root, text="⌫", padx= 23, pady=20, bg="#e83f25", font=myfontButton, command=hapus)
cls = Button(root, text="AC", padx= 23, pady=20, bg="#f5ecd5", font=myfontButton, command=clear)

btn0.grid(row=5, column=1, pady= 2)
btn1.grid(row=4, column=0, pady= 2)
btn2.grid(row=4, column=1, pady= 2)
btn3.grid(row=4, column=2, pady= 2)
btn4.grid(row=3, column=0, pady= 2)
btn5.grid(row=3, column=1, pady= 2)
btn6.grid(row=3, column=2, pady= 2)
btn7.grid(row=2, column=0, pady= 2)
btn8.grid(row=2, column=1, pady= 2)
btn9.grid(row=2, column=2, pady= 2)
cls.grid(row=1, column=0, pady= 2)
hap.grid(row=1, column=1, pady= 2)
per.grid(row=1, column=2, pady= 2)
bag.grid(row=1, column=3, pady= 2)
kur.grid(row=2, column=3, pady= 2)
kal.grid(row=3, column=3, pady= 2)
tam.grid(row=4, column=3, pady= 2)
sama.grid(row=5, column=3, pady= 2)
kom.grid(row=5, column=2, pady= 2)
kar.grid(row=5, column=0, pady= 2)



root.mainloop()