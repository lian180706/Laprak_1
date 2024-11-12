def luaspersegipanjang (panjang,lebar):
    return panjang*lebar
def kelilingpersegipanjang (panjang,lebar):
    return 2*(panjang+lebar)
 #nilai luas jika panjang=10, dan lebar=5
panjang =int(input("masukkan nilai panjang: "))
lebar=int(input("masukkan nilai lebar: "))

hasil_luas=luaspersegipanjang(panjang,lebar)
print("Luasnya adalah ",hasil_luas)
hasil_keliling=kelilingpersegipanjang(panjang,lebar)
print("Kelilingnya adalah ", hasil_keliling)
