import sys

P = [1, 2, 4, 8, 16]

if len(sys.argv) != 2:
    sys.exit("uso: python3 codificador.py <26 bits>")

data = sys.argv[1]
if len(data) != 26 or data.count("0") + data.count("1") != 26:
    sys.exit("erro: são necessários 26 bits (0 ou 1)")

word = [0] * 32
k = 0
for i in range(1, 32):
    if i not in P:
        word[i] = int(data[k])
        k += 1

print("Entrada:", data)

for p in P:
    positions = []
    ones = 0
    for i in range(1, 32):
        if i & p:
            positions.append(i)
            ones += word[i]
    word[p] = ones % 2
    print(f"P{p} = {word[p]}  {positions}")

text = ""
for i in range(1, 32):
    text += str(word[i])

print("Hamming:", text)
