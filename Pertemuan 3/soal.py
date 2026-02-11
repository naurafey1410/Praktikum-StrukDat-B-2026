class Game:
    def __init__(self, hsr, genshin, zzz):
        self.hsr = hsr
        self.genshin = genshin
        self.zzz = zzz

    def nama(self):
        print("Nama My Mine gwa",self.hsr)

    def hai(self):
        print(f"Hello, {self.genshin}")

game1 = Game("Dan Heng", "Wanderer", "Harumasa")     
game2 = Game("Phainon", "Xiao", "Lycoan")
game3 = Game("Mydei", "Kazuha", "Hugo")

print(game1.hsr, game1.genshin, game1.zzz)
print(game2.hsr, game2.genshin, game2.zzz)
print(game3.hsr, game3.genshin, game3.zzz)
game1.nama()
game2.hai()

game3.zzz = "Seth"
print(game3.zzz)