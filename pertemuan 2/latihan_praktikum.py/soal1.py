angka = [10, 20, 30, 40, 50]
#menambah 60 ke list

angka.append(60)
print(angka)

#hapus angka 20 dari list
angka.remove(20)
print(angka)

#menampilkan angka tertinggi ke terendah
angka.sort(reverse = True)
print(angka)

#hitung rata-rata
jumlah = 0
total = 0
for x in angka:
    jumlah += x
    total += 1
    rata = jumlah / total
print(rata)