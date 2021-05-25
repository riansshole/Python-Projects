def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print("Man thats enough for a party.")
    print("Get a blanket.\n")

print("Bisa ngasih angka ke function langsung: ")
cheese_and_crackers(20, 30)

print("Atau assign angka buat function lewat variable: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Kita bisa melakukan matematika didalam juga")
cheese_and_crackers(123 - 51, 123 + 30)

print("Bisa kita gabungin keduanya, variable dan matematika")
cheese_and_crackers(amount_of_cheese + 30, amount_of_crackers * 10)