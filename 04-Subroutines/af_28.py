lang = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
values = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]
def graph():
    for i,j in zip(lang,values):
        print(i,'#'*j)
graph()