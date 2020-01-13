from random import randint 
class matrix():

    @staticmethod
    def create(x, y):
        value = 0
        # List comprehensions 
        matrix = [[value for i in range(y)] for j in range(x)]
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

    @staticmethod
    def create_unit(x):
        value = 0 
        matrix = [[value for i in range(x)] for j in range(x)]
        return matrix

    @staticmethod
    def fill_random(matrix,m,n):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = randint(m,n)      
        return matrix
    
    @staticmethod
    def transpose(m):
        transposed = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        for row in transposed:
            print(row)

    @staticmethod
    def create_diagonal(x,m,n):
        value = 0 
        matrix = [[value for i in range(x)] for j in range(x)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j:
                    matrix[i][j] = randint(m, n)
                else:
                    continue
        for row in matrix:
            print(row)
        return matrix
    @staticmethod
    def compare(matrix1,matrix2):
        x = 0
        y = len(matrix1[0])
        a = 0 
        b = len(matrix2[0])
        for i in range(len(matrix1)):
            x += 1
        print(x,y)
        for i in range(len(matrix2)):
            a += 1
        print(a,b)
        if x == a and y == b:
            for row1,row2 in zip(matrix1,matrix2):
                i = 0
                isSame = True
                print(row1,row2)
                
                if i == len(row1):
                    break
                elif i < len(row1):
                    if row1[i] == row2[i]:
                        isSame = True
                        continue
                    else:
                        isSame = False
                        print("Same size but diffrent values")
                        break
                if isSame == True:
                    print("Matrix equal")
        else:
            print("Matrix not equal")



m = matrix.create(4, 3)
g = matrix.create(4,3)
#matrix.print(m)
#matrix.print(g)
matrix.compare(m,g)
# matrix.print(m)
# x = matrix.create_unit(5)
# matrix.fill_random(x,5,9)
# matrix.print(x)
# print("==========================")
# matrix.transpose(x)
# matrix.create_diagonal(5,1,9)
