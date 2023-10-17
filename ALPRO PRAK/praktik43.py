#-----------------
# praktik43.py
# NIM : 5210411329
# Nama : Ilmira Yulfihani
#-----------------

import os
os.system('cls')
lagi = "Y"
while lagi=="Y" or lagi=="y":
    nilai = int(input("Masukkan Nilai [0..100] : "))
    if nilai <0 and nilai > 100:
        print("Anda salah memasukkan nilai")
    lagi=int(input("Ulangi [Y/T] : "))
    if nilai >= 80:
        print ("Nilai anda A")
        print ("Anda lulus sangat memuaskan!")
    elif nilai >= 65:
        print ("Nilai anda B")
        print ("Anda lulus memuaskan!")
    elif nilai >= 50:
        print ("Nilai anda C")
        print ("Anda lulus Cukup!")
    elif nilai >= 40:
        print ("Nilai anda D")
        print ("Anda tidak lulus. Harap Mengulang!")
    else :
        print ("Nilai anda E")
        print ("Anda tidak lulus. Harap Mengulang!")
    lagi =input("Mencoba lagi [Y/T] : ")
print(">>> Terima kasih Anda telah menggunakan program ini <<<")
    
