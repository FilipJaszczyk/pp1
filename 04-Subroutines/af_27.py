import re
text ='Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
def vowel(text):
    
    a = re.findall('a',text)
    e = re.findall('e', text)
    i = re.findall('i', text)
    o = re.findall('o', text)
    u = re.findall('u', text)
    y = re.findall('y', text)

    print(len(a),len(e),len(i),len(o),len(u),len(y))

vowel(text)