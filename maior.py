
# Descobrir maior número entre 3: 

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 >= num2 and num1 >= num3:
    print('O ', num1, ' é maior')
elif num2 >= num3:
    print('O ', num2, ' é maior')
else:
    print('O ', num3, ' é maior')


    


