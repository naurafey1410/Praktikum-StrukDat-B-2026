kelasA = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
KelasB = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

#mata kuliah yg diambil kedua kelas
mataKuliahSama = kelasA.intersection(KelasB) #untuk memilih mata kuliah sama yg diambil kedua kelas
print(mataKuliahSama) #menampilkan output

#mata kuliah yg diambil kelas A
print(kelasA) #menampilkan mata kuliah yg diambil kelas A

#seluruh mata kuliah unik yg diambil kelas A dan B
mataKuliah = kelasA.union(KelasB) #menggabungkan mata kuliah yg diambil
print(mataKuliah) #menampilkan seluruh mata kuliah


