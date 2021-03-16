def nomorhp(x):
    if len(x) > 13:
        print('Nomor HP hanya maksimal 13 Angka')
    else:
        if x[0:2] != '08':
            print('Nomor HP harus dimulai dengan \'08\'')
        else:
            print('Nomor HP Saya Adalah',x)


x = input('Masukkan Nomor HP : ')
nomorhp(x)