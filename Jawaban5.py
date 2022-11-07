def data():
    nim = int(input("\nNim  : "))
    nama = str(input("Nama : "))

def capucino():
    print("\nMemilih Capucino")
    harga = int(input("Masukkan Harga : "))
    ppn = harga/10
    total = harga + ppn
    print("Jumlah yang harus dibayarkan " + str(total))
    
def teh():
    print("\nMemilih Teh")
    harga = int(input("Masukkan Harga : "))
    ppn = harga/10
    total = harga + ppn
    print("Jumlah yang harus dibararkan " + str(total))
    
def pilihan():
    print("\nPilihan")
    print("1. Capucino")
    print("2. Teh")
    print("3. Exit")
    
while True:
    data()
    pilihan()
    pil = int(input("Masukkan Pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    else :
        break