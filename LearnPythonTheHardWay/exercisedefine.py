def konversicelcius(celsius, fahrenheit, kelvin, reamur):
    print(f"{celsius} Celsius dalam Fahrenheit menjadi {fahrenheit} F")
    print(f"{celsius} Celsius dalam Reamur menjadi {reamur} R")
    print(f"{celsius} Celsius dalam Kelvin menjadi {kelvin} K")

celsius = input("Masukkan suhu dalam celcius:\n>")
fahrenheit = (9/5*float(celsius)+32)
reamur = 4/5*float(celsius)
kelvin = float(celsius)+273
konversicelcius(celsius, fahrenheit, kelvin, reamur)