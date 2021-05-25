from sys import exit

duit = 0
item = []
barangMewahkamar2 = ['laptop','iphone','speaker','kasur','cincin','jam tangan','gelang',]


def melihatinventory():
    print("\n")
    print("Apakah kamu ingin melihat inventory? (Y/N)")
    inventory = input("> ")
    if "Y" in inventory:
        print("Duit: ",duit,"\nItem: ",item)
    elif "y" in inventory:
        print("Duit: ",duit,"\nItem: ",item)
    else:
        ruangtamu

def ruangtamu():
    print("Kamu berada di dalam ruang tamu sebuah rumah tua dengan penerangan yang sangat kurang.\n")
    print("Terdapat 5 pintu dan 1 tangga menuju ke lantai 2. Salah satunya pintunya adalah pintu keluar dari rumah tersebut\n")
    print("Pintu-pintu itu tidak ada keunikannya dan pintu nya sama persis dengan pintu lainnya.\n")
    melihatinventory()

    print("Pintu keberapa yang kamu pilih?")

    pilihan = input('> ')
    if "1" in pilihan:
        kamar1()
    elif "2" in pilihan:
        kamar2()
    elif "3" in pilihan:
        kamarmandi()
    elif "4" in pilihan:
        kamar4()
    elif "5" in pilihan:
        print("Kamu memilih pintu keluar dari rumah ini. Cupu..\n")
        exit(0)
    else:
        print("Kamu kebingungan muter muter di dalam rumah sampai mati kelaparan. Nice\n")
        dead()



def dead():
    print("Yha anak tolol mati..\n")
    print("The end\n")
    exit(0)

def kamarmandi():
    print("Kamu memasuki kamar mandi kecil dengan air yang masih menetes dari kerannya secara perlahan\n")
    print("Terdapat saklar lampu di pojok kamar mandi tersebut\n")
    
    action = input("Apakah kamu ingin memencet saklar lampu tersebut? (Y/N) > ")

    if "Y" in action:
        print("Kamu berusaha meraih saklar lampu yang terdapat di pojok kamar mandi\n")
        print("Saklar tersebut tertutup botol botolan produk yang sudah habis\n")
        print("Kamu merasakan ada helai rambut yang menyentuh tanganmu.\n")
        print("Apa yang akan kamu lakukan?\n")
        action = input("> ")
    elif "y" in action:
        print("Kamu berusaha meraih saklar lampu yang terdapat di pojok kamar mandi\n")
        print("Saklar tersebut tertutup botol botolan produk yang sudah habis\n")
        print("Kamu merasakan ada helai rambut yang menyentuh tanganmu.\n")
        print("Apa yang akan kamu lakukan?\n")
        action = input("> ")

        if "nyala" in action:
            print("Kamu berhasil memencet tombol saklar\n")
            print("Lampu sekarang menyala\n")
            print("Tapi saat kamu membalikkan badan\n")
            print("Tidak ada apa apa dan kamu tidak menemukan apa apa\n")
            print("Mampus. Waktu kamu sia sia.\n")
            print("Apakah kamu ingin melanjutkan explore kamar mandi?\n")
        elif "pencet" in action:
            print("Kamu berhasil memencet tombol saklar\n")
            print("Lampu sekarang menyala\n")
            print("Tapi saat kamu membalikkan badan\n")
            print("Tidak ada apa apa dan kamu tidak menemukan apa apa\n")
            print("Mampus. Waktu kamu sia sia.\n")
            print("Apakah kamu ingin melanjutkan explore kamar mandi?\n")
        elif "meraih" in action:
            print("Kamu berhasil memencet tombol saklar\n")
            print("Lampu sekarang menyala\n")
            print("Tapi saat kamu membalikkan badan\n")
            print("Tidak ada apa apa dan kamu tidak menemukan apa apa\n")
            print("Mampus. Waktu kamu sia sia.\n")
            print("Apakah kamu ingin melanjutkan explore kamar mandi?\n")
        elif "melanjutkan" in action:
            print("Kamu berhasil memencet tombol saklar\n")
            print("Lampu sekarang menyala\n")
            print("Tapi saat kamu membalikkan badan\n")
            print("Tidak ada apa apa dan kamu tidak menemukan apa apa\n")
            print("Mampus. Waktu kamu sia sia.\n")
            print("Apakah kamu ingin melanjutkan explore kamar mandi?\n")
        elif "lanjut" in action:
            print("Kamu berhasil memencet tombol saklar\n")
            print("Lampu sekarang menyala\n")
            print("Tapi saat kamu membalikkan badan\n")
            print("Tidak ada apa apa dan kamu tidak menemukan apa apa\n")
            print("Mampus. Waktu kamu sia sia.\n")
            print("Apakah kamu ingin melanjutkan explore kamar mandi?\n")
            pilihan = input("(Y/N)> ")
            
            if "Y" in pilihan:
                print("Terdapat kotak misterius berwarna hitam dengan foto wajah mu diatasnya. Apakah kamu lakukan?\n")
                action = input("""
                1. Membuka kotak
                2. Menyimpan kotak
                3. Menjauhi kotak
                \n""")
            elif "y" in pilihan:
                print("Terdapat kotak misterius berwarna hitam dengan foto wajah mu diatasnya. Apakah kamu lakukan?\n")
                action = input("""
                1. Membuka kotak
                2. Menyimpan kotak
                3. Menjauhi kotak
                \n""")

                if "1" in action:
                    print("Kamu menemukan uang 2000. Mayan buat parkir\n")
                    global duit
                    duit += 2000
                
                elif "2" in action:
                    print("Kamu menyimpan kotak tersebut di kantong. Kok muat ye. Kamu juga terheran\n")
                    item.append("Kotak")

                else:
                    print("Cupu banget anjing ga punya nyali\n")
            print("Kamu kembali ke ruang tamu dengan wajah abis di prank yahahah kasian\n")

            ruangtamu()
        
        else:
            print("Nyali kamu ciut anjing cemen betul\n")
            print("Kamu kembali ke ruang tamu dengan perasaan takut dan panik\n")
            print("Cupu..\n")

            ruangtamu()
    else:
        print("Kamu menutup saluran air dengan sempurna karena merasa kesal dengan suaranya\n")
        print("Namun saat kamu memutar badan\n")
        print("Terdapat sosok besar dengan taring yang panjang dan mata yang merah menyala\n")
        print("Dia mencabik cabik isi perutmu. Mati deh. Goblok..\n")

        dead()

def kamar1():
    print("Kamu memasuki kamar tidur pertama dengan ukuran yang tidak terlalu besar namun juga tidak terlalu kecil\n")
    print("Kamar tersebut dibentuk seperti labirin dengan\n")
    print("lemari yang membuat jalan setapak seperti lorong\n")
    print("Di ujung lorong kamu bertemu dengan seseorang yang ternyata adalah gamer\n")
    print("Apa yang kamu lakukan?\n")
    print("""
    1. Ajak mabar lah broo
    2. Tampol palanya dari belakang
    3. Kokang lehernya
    4. Pelan pelan cabut keluar
    \n""")

    pilihan = input("> ")
    if "1" in pilihan:
        print("Orang itu bingung lo siapa anjengg trs mutusin kepala lu. Mati dah\n")
        dead()
    elif "2" in pilihan:
        print("Orang itu ternyata akai level 15 max build. Kuat broo ga ngaruh lu geplak doang\n")
        print("Akai tersebut balik badan dan mutusin kepalalu. Mati lu broo tolol\n")
        dead()
    elif "3" in pilihan:
        print("Orang tersebut kaget anjing ga sopan bet tbtb ngokang pala orang\n")
        print("Eh plot twist orang itu kesenengan\n")
        print("Kamu diajak mabar dan winstreak. Orang tersebut senang\n")
        print("Orang tersebut memberi mu uang 3juta\n")
        print("kamu berhasil keluar dari kamar tersebut dengan aman.\n")
        global duit
        duit += 3000000
        ruangtamu()
    elif "4" in pilihan:
        print("Kamu berhasil keluar tanpa menemukan apa apa\n")
        ruangtamu()
    else:
        print("Berisik bgt anjing lu grasak grusuk tu orang denger jadinya\n")
        print("Pala lu diputusin\n")
        dead()

def kamar2():
    print("Kamu memasuki kamar tidur lainnya yang berukuran sangat kecil\n")
    print("Kamu menemukan: ", barangMewahkamar2, " Apa yang kamu lakukan?\n")

    while True:
        lakukan = input("> ")
        if 'laptop' in lakukan:
            item.append('laptop')
        elif 'iphone' in lakukan:
            item.append('iphone')
        elif 'speaker' in lakukan:
            item.append('speaker')
        elif 'kasur' in lakukan:
            print("Gimana cara bawa kasur goblok lu sendirian\n")
        elif 'cincin' in lakukan:
            item.append('cincin')
        elif 'jam tangan' in lakukan:
            item.append('jam tangan')
        elif 'gelang' in lakukan:
            item.append('gelang')
        elif 'tidak' in lakukan:
            print("Kamu membalikkan badan dan tidak mengambil apa apa\n")
            print("Terdapat sosok berwajah terang di hadapanmu dan berkata\n")
            print('"Mulia sekali kamu anak muda, sebagai imbalannya akan saya berikan uang 14 juta"\n')
            print("Kamu keluar ke ruang tamu dengan status kaya raya\n")
            global duit
            duit += 14000000
            ruangtamu()
        elif 'keluar' in lakukan:
            print("Kamu keluar dari kamar tersebut dan kembali ke ruang tamu\n")
            ruangtamu()
        else:
            print("cepet ambil keputusan bangsat\n")

def kamar4():
    print("Kamu memasuki kamar tidur utama yang sangat luas\n")
    print("Kamu menemukan uang berserakan di kasur yang luas itu\n")
    action = input("Apa yang kamu lakukan? \n>")

    if 'ambil' in action:
        print("Sosok besar dengan mata hijau terang tiba tiba muncul dan membelah badan mu menjadi dua\n")
        dead()
    else:
        print("Kamu tidak memiliki nyali untuk mengambil uang itu dan memilih untuk keluar\n")
        print("Ada bapak tua tiba tiba nongol didepan wajah kamu\n")
        print("Beliau berkata: \n")
        print("""Ngapain anjing kerumah gue tolol
        sana lu cabut\n""")
        print("Yha tau gitu mah ngambil duitnye sekalian kan goblok lu keluar rumah sia sia gadapet duit segepok\n")
        print("The end")
        exit(0)

ruangtamu()