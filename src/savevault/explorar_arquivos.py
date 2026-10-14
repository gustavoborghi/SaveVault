from pathlib import Path

caminho = Path("save.txt")
caminho.write_text('''Level: 5
Life: 80
Coins: 120''')
texto_anterior = caminho.read_text()

caminho.write_text('''Level: 5
Life: 80
Coins: 60''')
texto_atual = caminho.read_text()
print(texto_anterior != texto_atual)


