zakaz = '20-753951'
klient = 'ООО Рога и копыта'
mrf = 'Центр'
gorod = 'Тула'
city = 'Ефремов'
ulica = 'Лермонтова'
dom = '36'
td = '2'
cms = 'Организован'
if str(gorod) == str(city):
    addr = [klient, mrf, gorod,str(ulica + ', ' + dom), td, cms,zakaz]
    print(addr)
else:
    addr = [klient, mrf, gorod,city + ', ' + ulica + ', ' + dom, td, cms, zakaz]
    print(addr)