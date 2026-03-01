# Diberikan dua daftar hadir mahasiswa di dua sesi yang berbeda:  
# sesi_pagi = {"Andi", "Budi", "Cici"} sesi_siang = {"Budi", "Deni", "Eka"} 
# a. Tampilkan nama mahasiswa yang hadir di kedua sesi (pagi DAN siang) 
# b. Tampilkan total daftar nama unik yang hadir hari itu (semua mahasiswa dari kedua 
# sesi tanpa duplikat). 
# c. Gabungkan kedua set tersebut menjadi satu set bernama sesi_hari_ini.

sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"} 

# hadir semua sesi
hadir_semua = sesi_pagi.intersection(sesi_siang)
print(hadir_semua)

# nama unik
nama_unik = sesi_pagi.difference(sesi_siang)
print(nama_unik)

# set sesi hari ini 
sesi_hari_ini = sesi_pagi.union(sesi_siang)
print(sesi_hari_ini)