#-----------------
#Latihan 3
#Nama : Ilmira Yulfihani
#NIM : 5210411329
#-----------------

import os
os.system('cls')#digunakan untuk bersihkan layar
lagi = "Y"
while lagi == "Y" or lagi == "y" :
    os.system('cls')
    nilai1=int(input("Nilai 1 :"))
    nilai2=int(input("Nilai 2 :"))
    nilai3=int(input("Nilai 3 :"))
    nilai4=int(input("Nilai 4 :"))
    nilai5=int(input("Nilai 5 :"))
    jumlah = nilai1+nilai2+nilai3+nilai4+nilai5
    rata_rata = jumlah/5
    print("Jumlah =",jumlah)
    print("Rata-rata =", rata_rata)
    print(" ")
    lagi = input("Ingin mencoba lagi? [Y/T] :" )
print("======= Terima Kasih =======")
#untuk mencoba jalankan lewat CMD
