#----------------------------
# Tugas Pert 4.py
# NIM : 5210411329
# Nama : Ilmira Yulfihani
#----------------------------

import os
os.system('cls')
lagi="Y"

while lagi == "Y" or lagi == "y":
    a=int(input("Masukan nilai1 : "))
    b=int(input("Masukan nilai2 : "))
    c=int(input("Masukan nilai3 : "))
    d=int(input("Masukan nilai4 : "))
    maks=int()
    minim=int()

    if a > b :
        maks = a
    elif b > a :
        maks = b
    else :
        maks = a

    if c > maks :
        maks = c

    if d > maks :
        maks = d
        
    if a < b :
        minim = a
    elif b < a :
        minim = b
    else :
        minim = a

    if c < minim :
        minim = c

    if d < minim :
        minim = d

    print ("Nilai terbesar : ",maks," Nilai terkecil : ",minim)
    print ("")
    lagi = str(input("Ingin mencoba lagi? [Y/T] : "))
print (">>> Terima kasih sudah menggunakan program ini. <<<")
