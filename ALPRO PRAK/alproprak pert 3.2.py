#-------------------
# Program diskon
# Nama : Ilmira Yulfihani
# NIM : 5210411329
#-------------------

def hitDiskon(pemb,disk):
    return pemb*disk/100

bayar = int(input("Jumlah Bayar: "))
disk = int(input("Diskon [1..00] : "))
diskon = hitDiskon(bayar, disk)
Total_Bayar = bayar-diskon
print("Bayar : ",bayar)
print("Diskon : ",disk,"% =",diskon)
print("Total Bayar : ",Total_Bayar)
