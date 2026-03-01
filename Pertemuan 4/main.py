# main.py

from kurs import mataUang
from konverter import idr_ke_uang_asing, uang_asing_ke_idr
from tabulate import tabulate

print("=== KONVERTER MATA UANG ===")

# Menampilkan tabel mataUang
print(tabulate(mataUang.items(), headers=["Kode", "Kurs"], tablefmt="grid"))

# Input user
dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

# Proses konversi
if dari == "IDR":
    hasil = idr_ke_uang_asing(jumlah, ke)
    print(f"Rp {jumlah:,.0f} = {hasil:.2f} {ke}")

elif ke == "IDR":
    hasil = uang_asing_ke_idr(jumlah, dari)
    print(f"{dari} {jumlah:.2f} = Rp {hasil:,.0f}")

else:
    print("Hanya menerima konversi IDR ke mata uang asing yang tersedia dan sebaliknya.")