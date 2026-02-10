mahasiswa = {
    "A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
    "A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
    "A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

#Tampilkan nama mahasiswa yang memiliki IPK di atas 3.5
for x in mahasiswa: #untuk setiap x pada dict mahasiswa
    if (mahasiswa[x]["ipk"]) > 3.5: #jika ipk > 3.5
        print(mahasiswa[x]["nama"]) #tampilkan nama mahasiswa

#Hitung rata-rata IPK seluruh mahasiswa
jumlah = 0 #menyimpan total ipk
hitung = 0 #menyimpan jumlah mahasiswa
for x in mahasiswa: #untuk setiap x pada mahasiswa
    jumlah = jumlah + (mahasiswa[x]["ipk"]) #perulangan jumlah ipk
    hitung = hitung + 1 #menambahkan ipk ke variable jumlah
    rata = jumlah / hitung #hitung rata-rata

print(rata) #menampilkan rata-rata

#Tambahkan satu data mahasiswa baru
mahasiswa ["A001"] = {"nama": "Naurah", "prodi": "Informatika", "ipk": 3.49} #menambahkan data baru pada list mahasiswa
print(mahasiswa)