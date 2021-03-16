def sort():
    angka = map(int,input('Masukkan Angka : ').split(' '))
    list_angka = list(angka)
    min = list_angka[0]
    max = list_angka[0]

    print(list_angka)
    
    for i in range(len(list_angka)):
        if list_angka[i] < min:
            min = list_angka[i]

        if list_angka[i] > max:
            max = list_angka[i]

    for j in range(len(list_angka)):
        if list_angka[i] < list_angka[j]:
            tmp = list_angka[i]
            list_angka[i] = list_angka[j]
            list_angka[j] = tmp

    print("Hasil Sorting: ", list_angka)
    print("Hasil terbesar: ", max)
    print("Hasil terkecil: ", min)

sort()