def kalimat(x):
    list_kalimat = list(x)
    max_len = -1
    for i in list_kalimat: 
        if len(i) > max_len: 
            max_len = len(i) 
            panjang = i
    
    jumlah = len(panjang)

    print('Jumlah Karakter Terbanyak adalah',jumlah,'Karakter')
    print('Karakter Yang Berjumlah',jumlah,'adalah',panjang)


x = input('Masukkan kalimat : ').split (' ')
kalimat(x)


