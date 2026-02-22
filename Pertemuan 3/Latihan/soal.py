class Game: #sebuah kelas bernama Game
    def __init__(self, hsr, genshin, zzz): #memiliki 3 paramater
        self.hsr = hsr #dan juga 3 atribut
        self.genshin = genshin
        self.zzz = zzz

    def nama(self): #method nama
        print("Nama My Mine gwa:",self.hsr) #untuk menampilkan pesan

    def hai(self): #method hai
        print(f"Hello, {self.genshin}") #untuk menampilkan pesan

#memiliki 3 objek dengan nama-nama karakter
game1 = Game("Dan Heng", "Wanderer", "Harumasa")   
game2 = Game("Phainon", "Xiao", "Seth")
game3 = Game("Mydei", "Kazuha", "Hugo")

#menampilkan hasil dari objek
print(game1.hsr, game1.genshin, game1.zzz)
print(game2.hsr, game2.genshin, game2.zzz)
print(game3.hsr, game3.genshin, game3.zzz)

#memanggil method nama dan hai
game1.nama()
game2.hai()

#mengganti nilai game3 zzz dari Hugo ke Ye Shiyuan
game3.zzz = "Ye Shiyuan"
print(game3.zzz)