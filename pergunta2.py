def verificString(string):
    cont = 0
    for i in range(0, len(string)):
        if string[i].lower() == "a":
            cont += 1
    
    return cont


string = input('Digite algo: ')
cont = verificString(string)

print(f'A letra "A" aparece {cont} vezes na string')