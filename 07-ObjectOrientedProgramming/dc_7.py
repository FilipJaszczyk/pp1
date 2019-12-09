class Student():
    uni = 'UEK Kraków'
    field = 'Informatyka Stosowana'
    album = 1000000
    def __init__(self, fullname):
        self.fullname = fullname
        Student.album += 1 
        self.nrAlbum = Student.album
    def __str__(self):
        return f'''
Fullname: {self.fullname}
Album: {self.nrAlbum}
Field: {Student.field}
Uni: {Student.uni}'''

s1 = Student('Wacław Potocki')
print(s1)
s2 = Student('Ryszard Kapuścinśki')
print(s2)
s3 = Student('Henryk Sienkiewicz')
print(s3)