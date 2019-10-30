with open('students.txt', 'r') as file:
    for line in file:
        new_line = line.split(',')
        if new_line[2] == 'age':
            continue
        if int(new_line[2]) < 30:
            print(f'{new_line[0]} {new_line[1]} {new_line[4]}')
