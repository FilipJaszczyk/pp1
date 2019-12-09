class Music():
    def __init__(self, author, title, album, year):
        self.author = author
        self.title = title
        self.album = album
        self.year = year
    def __str__(self):
        return f'''
Author: {self.author}
Title: {self.title}
Album: {self.album}
Year: {self.year}
                '''
m1 = Music('Dawid Podsiadło','Nie ma fal', 'Małomiasteczkowy', 2018)
print(m1)
m2 = Music('Mac DeMarco','One Another', 'Another one', 2015)
print(m2)