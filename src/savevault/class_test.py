class Game:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Jogo: {self.nome}")

jogo1 = Game("Hades")
jogo2 = Game("The Witcher 3")
jogo1.apresentar()