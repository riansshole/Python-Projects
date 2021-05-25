def tambah(a,b):
    print(f"Menambahkan {a} + {b}")
    return a + b

def kurang(a,b):
    print(f"Menambahkan {a} - {b}")
    return a - b

def perkalian(a,b):
    print(f"Mengkalikan {a} * {b}")
    return a * b

def pembagian(a,b):
    print(f"Mengkalikan {a} / {b}")
    return a / b

print("\n")
print("Mari gunakan kalkulator otomatis ini!")
print("\n")

hasil_tambah = tambah(float(input("Masukkan angka untuk ditambah(input 0 jika tidak perlu):\n>")), float(input("Masukkan angka:\n>")))
print("\n")
hasil_kurang = kurang(float(input("Masukkan angka untuk dikurang(input 0 jika tidak perlu):\n>")), float(input("Masukkan angka:\n>")))
print("\n")
hasil_kali = perkalian(float(input("Masukkan angka untuk dikali(input 0 jika tidak perlu):\n>")), float(input("Masukkan angka:\n")))
print("\n")
hasil_bagi = pembagian(float(input("Masukkan angka untuk dibagi(input 0 jika tidak perlu):\n>")), float(input("Masukkan angka:\n>")))

print("\n")
print(f"Hasil penambahan: {hasil_tambah}\nHasil pengurangan: {hasil_kurang}\nHasil perkalian: {hasil_kali}\nHasil pembagian: {hasil_bagi}.")