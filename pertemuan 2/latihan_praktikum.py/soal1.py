angka = [10, 20, 30, 40, 50] #list dengan nama angka yg berisi bilangan-bilangan
#menambah 60 ke list

angka.append(60) #append() digunakan untuk menambahkan angka 60 ke akhir list
print(angka) #menampilkan output

#hapus angka 20 dari list
angka.remove(20) #remove() digunakan untuk mengahapus angka 20 dari list
print(angka)

#menampilkan angka tertinggi dan terendah
tertinggi = max(angka) #menyimpan angka tertinggi dari list
terendah = min(angka) #menyimpan angka terendah dari list

print(tertinggi, terendah) #menampilkan output bilangan teringgi dan terendah

#hitung rata-rata
jumlah = 0 #menyimpan jumlah angka
total = 0 #menyimpan elemen dalam list
for x in angka: #setiap x dalam angka, maka
    jumlah += x #menjumlahkan setiap elemen
    total += 1 #menghitung jumlah elemen
    rata = jumlah / total #operasi menghitung rata-rata
print(rata) #mencetak hasil hitung rata-rata