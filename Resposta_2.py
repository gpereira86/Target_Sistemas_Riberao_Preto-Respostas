# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’,
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
#
# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

def contar_letra_a(s):
    return s.lower().count('a')

texto = input("Informe uma string: ")
quantidade = contar_letra_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes na string.")
