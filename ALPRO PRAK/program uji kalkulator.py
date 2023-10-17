import kalkulator as k

a=int(input("Masukkan nilai a = "))
b=int(input("Masukkan nilai b = "))
nama=str(input("Masukkan nama ibu = "))

print("a + b = ",k.tambah(a,b))
print("a - b = ",k.kurang(a,b))
print("a * b = ",k.kali(a,b))
print("a / b = ",k.bagi(a,b))
print("luas segitiga dengan alas a tinggi b = ",k.hitungSegitiga(a,b))
print("luas persegi dengan sisi a = ",k.hitungPersegi(a,b))
print("luas persegi panjang dengan panjang a dan lebar b = ",k.hitungPersegiPanjang(a,b))
print("a^2 = ",k.x_pangkatdua(a))
print("b^2 = ",k.y_pangkatdua(b))
k.tambahString(nama,a,b)
