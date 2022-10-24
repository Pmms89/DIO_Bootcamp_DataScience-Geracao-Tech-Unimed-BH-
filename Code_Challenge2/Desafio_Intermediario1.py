# Desafio:
# Dada a letra N do alfabeto, nos diga qual a sua posição.

# Entrada
# Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).

# Saída
# Um único inteiro, que representa a posição da letra no alfabeto.

# Exemplo:
# Entrada = C --> Saida = 3
# Entrada = J --> Saida = 10
# Entrada = Z --> Saida = 26
# Entrada = A --> Saida = 1

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;


letra = input() 

# # TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;


NUM = 31
  
# Function to calculate the position of characters
def positions(letra):
    for i in letra:
          
        # Performing AND operation
        # with number 31
        return (ord(i) & NUM)
  
# Driver code
print(positions(letra))

  
