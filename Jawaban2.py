print("Menghitung Luas Segitiga")
alas = float(input("Masukkan Alas: "))
tinggi = float(input("Masukkan Tinggi: "))
def segitiga(alas,tinggi):
    luas = 0.5*alas*tinggi
    print("Hasil: "+ str(luas))
segitiga(alas,tinggi)