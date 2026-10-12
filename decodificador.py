import sys

P = [1, 2, 4, 8, 16]

if len(sys.argv) != 2:
    sys.exit("uso: python3 decodificador.py <31 bits>")

text = sys.argv[1]
if len(text) != 31 or text.count("0") + text.count("1") != 31:
    sys.exit("erro: são necessários 31 bits (0 ou 1)")

word = [0]
for char in text:
    word.append(int(char))

syndrome = 0
syndrome_bits = ""
for p in [16, 8, 4, 2, 1]:
    ones = 0
    for i in range(1, 32):
        if i & p:
            ones += word[i]
    bit = ones % 2
    syndrome_bits += str(bit)
    if bit == 1:
        syndrome += p

if syndrome != 0:
    word[syndrome] = 1 - word[syndrome]

corrected = ""
data = ""
for i in range(1, 32):
    corrected += str(word[i])
    if i not in P:
        data += str(word[i])

print("Recebida: ", text)
print("Síndrome: ", syndrome_bits, "=", syndrome)
print("Corrigida:", corrected)
print("Dados:    ", data)
