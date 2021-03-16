def caps(kalimat):
    if kalimat == '':
        print('Masukkan Sebuah Inputan')
    else:
        caps = kalimat.upper()
        hasil = caps.replace(' ','')
        print('*'+ hasil + '*')

kalimat = input('Masukkan Sebuah Kalimat : ')
caps(kalimat)