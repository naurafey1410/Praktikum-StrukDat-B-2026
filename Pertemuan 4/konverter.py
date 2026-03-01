# konverter.py

from kurs import mataUang  #untuk mengambil dictionary mataUang dari file mataUang.py.

def idr_ke_uang_asing(jumlah, kode):   #untuk mengubah mata uang IDR ke mata uang asing
    if kode in mataUang:   #mengecek apakah kode mata uang yang dimasukkan user tersedia di dalam dictionary mataUang.
        return jumlah / mataUang[kode]
    return None  #Jika kode tidak ditemukan fungsi mengembalikan nilai kosong sebagai tanda bahwa kode tidak valid.
 
def uang_asing_ke_idr(jumlah, kode):  #digunakan untuk mengubah mata uang asing ke Rupiah (IDR).
    if kode in mataUang:   #Mengecek apakah kode mata uang tersedia.
        return jumlah * mataUang[kode]
    return None  #jika kode tidak valid