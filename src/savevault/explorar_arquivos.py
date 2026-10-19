
from pathlib import Path
import hashlib

caminho = Path("save.txt")
caminho.write_text("""Level: 5
Life: 80
Coins: 120""")
texto_anterior = caminho.read_text()

texto_anterior_hash = hashlib.sha256(texto_anterior.encode()).hexdigest()

caminho.write_text('''Level: 5
Life: 80
Coins: 60''')
texto_atual = caminho.read_text()
texto_atual_hash = hashlib.sha256(texto_atual.encode()).hexdigest()



print(texto_anterior_hash == texto_atual_hash)