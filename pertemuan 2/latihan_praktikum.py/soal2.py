#menampilkan nama mahasiswa
mahasiswa = ("A001", "Budi", "Informatika") #sebuah tuple bernama mahasiswa yg berisi nama, nim dan prodi mahasiswa
print(mahasiswa[1]) #menampilkan indeks ke satu dari tuple, yaitu mahasiswa

#menampilkan isi tuple menggunakan pengulangan for
for x in mahasiswa: #untuk setiap x dalam tuple mahasiswa
    print(x) #menampilkan satu per satu elemen

'''
alasan kenapa tuple tidak bisa diubah adalah
tuple bersifat immutable (tujuan dan sifat dasar tuple)
'''