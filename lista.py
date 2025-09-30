
times = []

times = ['Flamengo']
times.append('Vasco')
times.append('Bangu')      # o .append permite apenas um por um pra inserir
times.append('Dinamo Kiev')

print(times[2])    # [] para saída de elemento unitário indicado no colchete

# FOR COM NÚMERO
# for i in range(0, len(times)):   # não importa o tamanho da lista, vai passar por toda a extensão mesmo que haja exclusão/inserção
#    print(times[i])

for item in times:
    print(item)




