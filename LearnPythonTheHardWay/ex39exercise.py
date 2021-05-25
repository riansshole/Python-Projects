#mapping

kota = {
    'Jakarta' : 'JKT',
    'Surabaya' : 'SBY',
    'Depok' : 'DPK',
    'Magelang' : 'MGL',
    'Malang' : 'MLG',
    'Bogor' : 'BGR',
    'Tangerang' : 'TGR',
    'Bekasi' : 'BKS'
    }

kecamatan = {
    'JKT' : 'Cakung',
    'SBY' : 'Gunung Anyar',
    'DPK' : 'Beji',
    'MGL' : 'Borobudur',
    'MLG' : 'Blimbing',
    'BGR' : 'Bogor Barat',
    }

#nambahin kecamatan
kecamatan['TGR'] = 'Cibodas'
kecamatan['BKS'] = 'Bantar Gebang'

#print beberapa kota
print("\n")
print("Jakarta punya kecamatan", kecamatan[kota['Jakarta']])
print("Malang punya kecamatan", kecamatan[kota['Malang']])

#print singkatan kota
print("\n")
print("Singkatan kota Jakarta adalah",kota['Jakarta'])
print("Singkatan kota Malang adalah",kota['Malang'])

#print semua singkatan kota
print("\n")
for kota, singkatan in list(kota.items()):
    print(f"{kota} singkatannya adalah {singkatan}")
    print(f"dan memiliki kecamatan {kecamatan[singkatan]}")

#print semua kecataman di dalam kota
print("\n")
for singkatan, kecamatan in list(kecamatan.items()):
    print(f"{singkatan} memiliki kecamatan {kecamatan}")

#safely gets an abbreviation of states that might not be there
kota = kota.get('Riau')

if not kota:
    print("Ga ada kota Riau cok di dictionary lo")