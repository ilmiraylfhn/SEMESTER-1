#-----------------
# praktik45.py
# NIM : 5210411329
# Nama : Ilmira Yulfihani
#-----------------

import os
os.system('cls')
lagi="Y"
while lagi=="Y" or lagi=="y":
    os.system ('cls')
    nilai=int(input("Masukkan nilai : "))
    if nilai >= 0 and nilai <= 19 :
        print ("Nilai anda E")
    elif nilai >=20 and nilai <= 44 :
        print ("Nilai anda D")
    elif nilai >=45 and nilai <= 64 :
        print ("Nilai anda C")
    elif nilai >=65 and nilai <= 79 :
        print ("Nilai anda B")
    elif nilai >=80 and nilai <= 100 :
        print ("Nilai anda A")
    else :
        print ("Maaf Anda salah input")
    print("")
    lagi=input("Mencoba Lagi?[Y/T] : ")
print(">>> Terima kasih Anda telah menggunakan program ini. <<<")
        
