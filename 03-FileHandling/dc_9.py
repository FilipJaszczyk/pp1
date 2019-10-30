counter = 1
with open('NoEducation.txt','r') as file:
    for line in file:
        print(counter,line,end='')
        counter += 1 
file.closed