tab =[32, 16, 5, 8, 24, 7]

with open('13.txt','a') as file:
    for i in tab:
        file.write(str(i))
        file.write('\n')
file.close

        