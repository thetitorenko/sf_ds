import pandas as pd

data_kaz = pd.read_html('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD%D0%B0')
data_rus = pd.read_html('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8')
data_ukr = pd.read_html('https://population-hub.com/ru/ua/list-of-cities-in-ukraine-by-population.html')
data_blr = pd.read_html('https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D1%83%D1%81%D1%81%D0%B8%D0%B8')
data_uzb = pd.read_html('https://population-hub.com/ru/uz/list-of-cities-in-uzbekistan-by-population.html')

with open('./cities_kaz.txt', 'w') as f:
    f.write('(')
    for i in data_kaz[0].iloc[:, 1].to_list():
        f.write("'" + i + "'")
        f.write(', ')
    f.seek(f.tell() - 2)
    f.write(')')

with open('./cities_rus.txt', 'w') as f:
    f.write('(')
    for i in data_rus[0].iloc[:, 2].to_list():
        f.write("'" + i + "'")
        f.write(', ')
    f.seek(f.tell() - 2)
    f.write(')')

with open('./cities_ukr.txt', 'w') as f:
    f.write('(')
    for i in data_ukr[0].iloc[:, 1].to_list():
        f.write("'" + i + "'")
        f.write(', ')
    f.seek(f.tell() - 2)
    f.write(')')

with open('./cities_blr.txt', 'w') as f:
    f.write('(')
    for i in data_blr[1].iloc[:, 1].to_list():
        f.write("'" + i + "'")
        f.write(', ')
    f.seek(f.tell() - 2)
    f.write(')')

with open('./cities_uzb.txt', 'w') as f:
    f.write('(')
    for i in data_uzb[0].iloc[:, 1].to_list():
        f.write("'" + i + "'")
        f.write(', ')
    f.seek(f.tell() - 2)
    f.write(')')
