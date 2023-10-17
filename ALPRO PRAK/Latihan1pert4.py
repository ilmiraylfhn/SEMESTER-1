#-----------------
# praktik46.py
# NIM : 5210411329
# Nama : Ilmira Yulfihani
#-----------------

import os
os.system('cls')
lagi="Y"
    
while lagi=="Y" or lagi=="y":
    os.system ('cls')
    nilai=int(input("Masukkan nilai : "))
    def ubahNilai(a):
        if nilai >= 0 and nilai <= 19 :
            return(" E")
        elif nilai >=20 and nilai <= 44 :
            return (" D")
        elif nilai >=45 and nilai <= 64 :
            return (" C")
        elif nilai >=65 and nilai <= 79 :
            return (" B")
        elif nilai >=80 and nilai <= 100 :
            return (" A")
        else :
            return (" F")
    print("Nilai anda",ubahNilai(nilai))
    print("")
    lagi=input("Mencoba Lagi?[Y/T] : ")
print(">>> Terima kasih Anda telah menggunakan program ini. <<<")
        
