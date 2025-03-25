# Conversor de temperaturas:

def c_f(c):
    return float((c * 1.8) + 32)

def f_c(f):
    return float((f - 32) / 1.8)

def c_k(c):
    return c + 273

def k_c(k):
    return k - 273

def f_k(f):
    return c_k(f_c(f))

def k_f(k):
    return float((k_c(k) * 1.8) + 32)

# Para o usuário interagir c/ o sistema

print('Qual unidade de temperatura está sendo usada?')
print('1- Celsius')
print('2- Fahrenheit')
print('3- Kelvin\n')

decisao = input(('Digite a opção desejada (1, 2 ou 3): '))
print('')
    
while decisao != '1' and decisao != '2' and decisao != '3':
    print('Input inválido! Tente novamente.')
    decisao = input(('Digite a opção desejada (1, 2 ou 3): '))

# Celsius --> any

if decisao == '1':
    c = float(input('Digite o valor dessa temperatura: '))
    print('Para qual unidade deseja converter?')
    print('1- Fahrenheit')
    print('2- Kelvin\n')
    print('')
    
    decisao2 = input(('Digite a opção desejada (1 ou 2): '))
    print('')

    while decisao2 != '1' and decisao2 != '1' :
        print('Input inválido! Tente novamente.')
        decisao2 = input(('Digite a opção desejada (1, ou 2): '))

    if decisao2 == '1':
        print(f'\nA conversão de Celsius para Fahrenheit é {c_f(c)}°F')

    if decisao2 == '2':
        print(f'A conversão de Celsius para Kelvin é {c_k(c)}K')

# Fahrenheit --> any

if decisao == '2':
    f = float(input('Digite o valor dessa temperatura: '))
    print('')
    print('Para qual unidade deseja converter?')
    print('1- Celsius')
    print('2- Kelvin')
    print('')
    
    decisao2 = input(('Digite a opção desejada (1 ou 2): '))

    while decisao2 != '1' and decisao2 != '2':
        print('Input inválido! Tente novamente.')
        decisao2 = input(('Digite a opção desejada (1, ou 2): '))  

    if decisao2 == '1':
        print(f'\nA conversão de Fahrenheit para Celsius é {f_c(f)}°C')
    elif decisao2 == '2':
        print(f'\nA conversão de Fahrenheit para Kelvin é {f_k(f)}K')

# Kelvin --> any

if decisao == '3':
    k = float(input('Digite o valor dessa temperatura: '))
    print('Para qual unidade deseja converter?')
    print('1- Celsius')
    print('2- Fahrenheit\n')
    
    decisao2 = input(('Digite a opção desejada (1 ou 2): '))

    while decisao2 != '1' and decisao2 != '2':
        print('Input inválido! Tente novamente.')
        decisao2 = input(('Digite a opção desejada (1, ou 2): '))  

    if decisao2 == '1':
        print(f'\nA conversão de Kelvin para Celsius é {k_c(k)}°C')
    elif decisao2 == '2':
        print(f'\nA conversão de Kelvin para Fahrenheit é {k_f(k)}°F')
