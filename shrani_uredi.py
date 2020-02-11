import re
import orodja

#funkcija ki se zapelje po vseh straneh in jih shrani
def shrani_strani_iz_nepremicnine(stevilo_oglasov):
    stevilo_strani = stevilo_oglasov // 30 + 1
    for stevilka in range(1, stevilo_strani + 1):
        url = (
            f'https://www.nepremicnine.net/oglasi-prodaja/slovenija/{stevilka}/'             #f dela kot format
        )
        orodja.shrani_spletno_stran(url, f'spletne_strani/nepremicnine{stevilka}.html', vsili_prenos=False)


vzorec = (
    r'<span class="title">(?P<ime>.*?)</span></a></h2>.*?'
    r'\s*.*\s*.*\s*.*\s*.*'
    r'<span class="posr">(?P<posred>.*?): <span class="vrsta">(?P<vrsta>.*?)</span>.*'
    r'(class="tipi">(?P<koliko_sobno>.*?)</span></span>)?'
    r'\s*.*\s*.*\s*.*\s*.*'
    r'(class="atribut leto">Leto: <strong>(?P<leto_izgradnje>.*)</strong>)?'
    r'(\s*<span class="atribut">Zemljišče: <strong>(?P<zemljisce>.*) m2</strong>)?'
    r'(.*\s*)*?'
    r'(<span class="velikost" lang="sl">(?P<velikost>.*) m2</span><br />)?'
    r'\s*<span class="cena">(?P<cena>.*) &euro(.*)?</span>'
    r'(\s*<span class="agencija">(?P<agencija>.*?)</span>)?'
    )

# vzorec1 = r'<span class="title">(?P<ime>.*?)</span></a></h2>.*?\s*.*\s*.*\s*.*\s*.*<span class="posr">(?P<posred>.*?): <span class="vrsta">(?P<vrsta>.*?)</span>.*class="tipi">(?P<koliko_sobno>.*?)</span></span>\s*.*\s*.*\s*.*\s*.*<span class="atribut leto">Leto: <strong>(?P<leto_izgradnje>.*)</strong>.*<span class="atribut">Zemljišče: <strong>(?P<zemljisce>.*) m2</strong>.*\s*</div>\s*<!---->\s*<div class="kratek_container">\s*.*\s*</div>\s*.*\s*.*\s*<tr>\s*<td>\s*.*\s*</td>\s*.*\s*.*\s*.*\s*.*\s*<span class="velikost" lang="sl">(?P<velikost>.*) m2</span><br />\s*<span class="cena">(?P<cena>.*) &euro;</span>\s*<span class="agencija">(?P<agencija>.*?)</span>'

# vzorec = (
#         r'<span class="title">(?P<ime>.*?)</span></a></h2>.*'
#         r'<span class="posr">(?P<posred>.*?): <span class="vrsta">(?P<vrsta>.*?)</span>.*class="tipi">(?P<koliko_sobno>.*?)</span></span>.*'
#         r'<span class="atribut leto">Leto: <strong>(?P<leto_izgradnje>.*?)</strong>.*<span class="atribut">Zemljišče: <strong>(?P<zemljisce>.*?) m2</strong>.*'
#         r'<span class="velikost" lang="sl">(?P<velikost>.*?) m2</span><br />.*<span class="cena">(?P<cena>.*?) &euro;</span>.*<span class="agencija">(?P<agencija>.*?)</span>'
#         )

# vzorec = (
#     r'<span class="title">(?P<ime>.*?)</span></a></h2>.*?'
#     r'\s*.*\s*.*\s*.*\s*.*'
#     r'<span class="posr">(?P<posred>.*?): <span class="vrsta">(?P<vrsta>.*?)</span>.*'
#     r'(class="tipi">(?P<koliko_sobno>.*?)</span></span>)?'
#     r'\s*.*\s*.*\s*.*\s*.*'
#     r'(class="atribut leto">Leto: <strong>(?P<leto_izgradnje>.*?)</strong>)?'
#     r'(<span class="atribut">Zemljišče: <strong>(?P<zemljisce>.*?) m2</strong>)?(.*\s*)*?'
#     r'(<span class="velikost" lang="sl">(?P<velikost>.*?) m2</span><br />\s)?'
#     r'<span class="cena">(?P<cena>.*?) &euro(.*)?</span>'
#     r'(\s*<span class="agencija">(?P<agencija>.*?)</span>)?'
#     )

# vzorec = (
#     r'<span class="title">(?P<ime>.*?)</span></a></h2>.*?'
#     r'\s*.*\s*.*\s*.*\s*.*'                                        #nepomembno
#     r'<span class="vrsta">(?P<tip>.*?)</span>'
#     r'.*\s*.*\s*.*\s*.*\s*.*'                           #pridem do vrstice z nadstropje
#     r'<span class="atribut">Nadstropje: <strong>(?P<nadstropje>.*?)'    #nadstropje kak naredit da jemlje iz dveh delckov?
#     r'<span class="atribut leto">Leto: <strong>(?P<leto>.*?)</strong></span><span class="invisible">, </span>'  #leto izgradnje
#     r'<span class="velikost" lang="sl">(?P<velikost_nepremicnine>.*?) m2</span><br />'
#     r'<span class="atribut">Zemljišče: <strong>(?P<zemljisce>.*?) m2</strong></span>'
#     r'<span class="cena">(?P<cena>.*?) &euro.*?</span>'
#     )

nepremicnine = []
count = 0

count_stran = 0

for i in range(1, 667):
    if i == 118:
        continue
    else:
        count = 0
        with open(f'spletne_strani/nepremicnine{i}.html', encoding='utf-8') as f:
            vsebina = f.read()
            count_stran += 1
            print(count_stran)
        for zadetek in re.finditer(vzorec, vsebina):
            nepremicnine.append(zadetek.groupdict())
            count += 1
            #print(zadetek.groupdict())
        print(count)
#print(nepremicnine)


#ZA POSKUSAT
# with open(f'spletne_strani/nepremicnine5.html', encoding='utf-8') as f:
#      vsebina = f.read()

# for zadetek in re.finditer(vzorec, vsebina, flags=re.DOTALL):
#     nepremicnine.append(zadetek.groupdict())
#     print(zadetek.groupdict())
#     count += 1
# print(count)



#daj bek ad-bg
#stran 40 je ena oddaja namesto prodaja

imena_polj = ['ime', 'posred', 'vrsta', 'koliko_sobno', 'leto_izgradnje', 'zemljisce',
                'velikost', 'cena', 'agencija']
orodja.zapisi_csv(nepremicnine, imena_polj, 'podatki/nepremicnine5.csv')
orodja.zapisi_json(nepremicnine, 'podatki/nepremicnine5.json')

