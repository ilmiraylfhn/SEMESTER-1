#-----------------
# praktik44.py
# NIM : 5210411329
# Nama : Ilmira Yulfihani
#-----------------

import os
os.system('cls')
lagi = "Y"
while lagi=="Y" or lagi=="y":
    os.system('cls')
    i = int(input("Masukkan Nilai : "))
    if i>=0:
        if i%2==0:
            print (i," adalah bilangan genap positif")
        else:
            print (i," adalah bilangan ganjil positif")
    else :
        if i%2==0:
            print (i," adalah bilangan genap negatif")
        else:
            print (i," adalah bilangan ganjil negatif")
    lagi = input("Ulangi? [y/t] : ")
print(">>>Terima kasih sudah menggunakan program ini<<<")
