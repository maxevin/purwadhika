def segitiga(x):
    for i in range(1,x+1):
        for j in range(1,x*2):
            if i == x or i+j == x+1 or j-i==x-1:
                print('**',end='')
            else:
                print(end=' ')
        print()

x = int(input('Masukkan Jumlah Baris : '))
segitiga(x)