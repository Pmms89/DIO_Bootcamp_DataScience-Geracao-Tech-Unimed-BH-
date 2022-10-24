# Desafio 2

# Você deve escrever um programa para determinar o número médio de 
# cachorros-quentes consumidos pelos participantes.

# Entrada:
# A entrada consiste de uma única linha que contém dois inteiros 
# H e P (1 ≤ H, P ≤ 1000) indicando respectivamente o número total de 
# cachorros-quentes consumidos e o número total de participantes na competição.

# Saída:
# Seu programa deve produzir uma única linha com um número racional representando 
# o número médio de cachorros-quentes consumidos pelos participantes. 
# O resultado deve ser escrito como um número racional com exatamente dois dígitos 
# após o ponto decimal, arredondado se necessário.

valores = input().split() 

numero_cachorros = int(valores[0])
total_participantes = int(valores[1])

media_consumo = numero_cachorros/total_participantes

if (numero_cachorros >= 1):
  if (total_participantes <= 1000):
    print(f'{media_consumo:.2f}')

