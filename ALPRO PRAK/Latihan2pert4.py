#-----------------
# Latihan2pert4.py
# NIM : 5210411329
# Nama : Ilmira Yulfihani
#-----------------

import os
os.system('cls')
lagi="Y"
    
while lagi=="Y" or lagi=="y":
    os.system ('cls')
    def ubahNilai(a):
        if a >= 0 and a <= 19 :
            return("E")
        elif a >=20 and a <= 44 :
            return ("D")
        elif a >=45 and a <= 64 :
            return ("C")
        elif a >=65 and a <= 79 :
            return ("B")
        elif a >=80 and a <= 100 :
            return ("A")
        else :
            return ("F")

    def pengaliSkor(b):
        if b == "A" :
            return 4
        elif b == "B" :
            return 3
        elif b == "C" :
            return 2
        elif b == "D" :
            return 1
        elif b == "E" :
            return 0
        
    def hitungSkor (nilai,sks):
        return nilai*sks
    
    nilaiKuliah=int(input("Masukkan nilai : "))
    sks = int(input("Masukkan jumlah sks : "))
    nilaiAq = ubahNilai(nilaiKuliah)
    nilai = pengaliSkor(nilaiAq)
    
    print("Skor anda",hitungSkor(nilai,sks))
    print("")
    lagi=input("Mencoba Lagi?[Y/T] : ")
print(">>> Terima kasih Anda telah menggunakan program ini. <<<")
