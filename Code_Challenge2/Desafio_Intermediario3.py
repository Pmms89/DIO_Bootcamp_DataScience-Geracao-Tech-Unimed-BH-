#Desafio 3 

# A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:
# Salário	
# 0 - 600.00
# 600.01 - 900.00
# 900.01 - 1500.00
# 1500.01 - 2000.00
# Acima de 2000.00

# Percentual de Reajuste
# 17%
# 13%
# 12%
# 10%
# 5%

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

# Exemplo
# Entrada: 1000 ---> Saída: Novo salario: 1120,00; Reajuste ganho: 120,00; Em percentual: 12 %
# Entrada: 2000 ---> Saída: Novo salario: 2200,00; Reajuste ganho: 200,00; Em percentual: 10 %                                                                                      


# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = int(input()) 

if salario >= 0 and salario <= 600:
    percentage = 17
    novo_salario = salario + (salario * percentage/100)
    reajuste = novo_salario - salario

    # The way that the challege accepetec
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(reajuste)}\nEm percentual: {percentage} %')

    # If necessary change dot to comman (Brazilian Portuguese number notation):
    # novo_salario = f'{novo_salario:.2f}'
    # novo_salario = novo_salario.replace('.',',')
    # reajuste = f'{reajuste:.2f}'
    # reajuste = reajuste.replace('.',',')
    # print(f'Novo salario: {novo_salario}\nReajuste ganho: {reajuste}\nEm percentual: {percentage:.0f} %')


elif salario >= 600.01 and salario <= 900:
    percentage = 13
    novo_salario = salario + (salario * percentage/100)
    reajuste = novo_salario - salario
    
    # The way that the challege accepetec
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(reajuste)}\nEm percentual: {percentage} %')

    # If necessary change dot to comman (Brazilian Portuguese number notation):
    # novo_salario = f'{novo_salario:.2f}'
    # novo_salario = novo_salario.replace('.',',')
    # reajuste = f'{reajuste:.2f}'
    # reajuste = reajuste.replace('.',',')
    # print(f'Novo salario: {novo_salario}\nReajuste ganho: {reajuste}\nEm percentual: {percentage:.0f} %')

elif salario >= 900.01 and salario <= 1500:
    percentage = 12
    novo_salario = salario + (salario * percentage/100)
    reajuste = novo_salario - salario
    
    # The way that the challege accepetec
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(reajuste)}\nEm percentual: {percentage} %')

    # If necessary change dot to comman (Brazilian Portuguese number notation):
    # novo_salario = f'{novo_salario:.2f}'
    # novo_salario = novo_salario.replace('.',',')
    # reajuste = f'{reajuste:.2f}'
    # reajuste = reajuste.replace('.',',')
    # print(f'Novo salario: {novo_salario}\nReajuste ganho: {reajuste}\nEm percentual: {percentage:.0f} %')

elif salario >= 1500.01 and salario <= 2000:
    percentage = 10/100
    novo_salario = salario + (salario * percentage)
    reajuste = novo_salario - salario
    
    # The way that the challege accepetec
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(reajuste)}\nEm percentual: {percentage} %')

    # If necessary change dot to comman (Brazilian Portuguese number notation):
    # novo_salario = f'{novo_salario:.2f}'
    # novo_salario = novo_salario.replace('.',',')
    # reajuste = f'{reajuste:.2f}'
    # reajuste = reajuste.replace('.',',')
    # print(f'Novo salario: {novo_salario}\nReajuste ganho: {reajuste}\nEm percentual: {percentage:.0f} %')


else: 
    percentage = 5/100
    novo_salario = salario + (salario * percentage)
    reajuste = novo_salario - salario
    
    # The way that the challege accepetec
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(reajuste)}\nEm percentual: {percentage} %')

    # If necessary change dot to comman (Brazilian Portuguese number notation):
    # novo_salario = f'{novo_salario:.2f}'
    # novo_salario = novo_salario.replace('.',',')
    # reajuste = f'{reajuste:.2f}'
    # reajuste = reajuste.replace('.',',')
    # print(f'Novo salario: {novo_salario}\nReajuste ganho: {reajuste}\nEm percentual: {percentage:.0f} %')


# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e 
# o índice reajustado (em porcentagem)