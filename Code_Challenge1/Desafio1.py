
# Desafio 1

# Para calcular o ICM para Palantír’s, basta dividir a distância entre os dois 
# Palantír’s, pela soma do diâmetro dos mesmos.

# Entrada:
# A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), 
# que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír 
# de Sauron e o diâmetro do Palantír de Saruman.

# Saída:
# Um valor real indicando o ICM da comunicação dos Palatír de Sauron e Saruman, 
# com 2 casas decimais.

entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])
ICM_resultado = distancia/(diametro1+diametro2)

if (0 < distancia < 10000):
  if(0< diametro1,diametro2< 100):
    print(f'{ICM_resultado:.2f}')



