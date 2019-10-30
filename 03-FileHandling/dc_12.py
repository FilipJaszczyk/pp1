with open('shopinglist.txt','a') as file:
    product = input('Nazwa dodanego produktu: ')
    file.write(product)
    file.write('\n')
file.close
with open('shopinglist.txt','r') as file:
    for line in file:
        print(line, end='\n')
file.close