
# Desafio
# Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português. 
# Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. Nico, amigo de Humberto, 
# ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”. Antes que Humberto pudesse responder, 
# o papagaio gritou: “Aí eu caio, idiota!”.

# Entrada
# A entrada consiste de diversos casos de teste. Cada caso de teste consiste uma string informando qual a situação de levantamento 
# de pernas do papagaio.

# Saída
# Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará. Caso ele levante ambas as pernas, 
# imprima “caiu”. Quebre uma linha a cada caso de teste.

# Exemplo
# Entrada: esquerda ---> Saída: ingles
# Entrada: direita ---> Saída: frances 
# Entrada: nenhuma ---> Saída: portugues
# Entrada: ambas ---> Saída: caiu

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# while True significa que, enquanto houver entradas, o código após o try continuará sendo executado


while True: 
    try: 
           # TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
           # e imprima a saída de acordo com a situação das pernas do papagaio
        pergunta = input()
        if pergunta == "esquerda":
            print("ingles")
        elif pergunta == "direita":
            print("frances")
        elif pergunta == "nenhuma":
            print("portugues")
        elif pergunta == "ambas":
            print("caiu")
    except EOFError: 
        break