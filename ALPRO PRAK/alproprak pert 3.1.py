def cetakHewan (*hewan):
    print("tipe argumen:",type(hewan))
    print("menambahkan argumen")
    for h in hewan :
        print(h)

#memanggil fungsi
cetakHewan("gajah","sapi","kerbau")
