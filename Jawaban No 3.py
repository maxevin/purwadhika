def urutan(list_gabung):
  genap = []
  ganjil = []
  for i in list_gabung:
      if i % 2 == 0:
          genap.append(i)
      else:
          ganjil.append(i)
  ganjil.sort(),genap.reverse()
  ganjil.extend(genap)
  return ganjil


sort_odd_even =[1,3,2,2,1,5,1,24,12,124,12,21,32,15]
print(urutan(sort_odd_even))