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
    r'class="vrsta">(?P<vrsta>.*?)</span>.*'
    r'(class="tipi">(?P<koliko_sobno>.*?)</span></span>)?.*'
    r'\s*.*\s*.*\s*.*\s*.*'
    r'(class="atribut leto">Leto: <strong>(?P<leto_izgradnje>.*?)</strong>)?.*'
    r'(<span class="atribut">Zemljišče: <strong>(?P<zemljisce>.*?) m2</strong>)?(.*\s*)*?'
    r'(<span class="velikost" lang="sl">(?P<velikost>.*?) m2</span><br />\s)?'
    r'<span class="cena">(?P<cena>.*?) &euro(.*)?</span>'
    r'(\s*<span class="agencija">(?P<agencija>.*?)</span>)?'
    )

flags = re.DOTALL

    # r'<span class="title">(?P<ime>.*?)</span></a></h2>.*?'
    # r'\s*.*\s*.*\s*.*\s*.*'                                        #nepomembno
    # r'<span class="vrsta">(?P<tip>.*?)</span>'
    # r'.*\s*.*\s*.*\s*.*\s*.*'                           #pridem do vrstice z nadstropje
    #r'<span class="atribut">Nadstropje: <strong>(?P<nadstropje>.*?)'    #nadstropje kak naredit da jemlje iz dveh delckov?
    # r'<span class="atribut leto">Leto: <strong>(?P<leto>.*?)</strong></span><span class="invisible">, </span>'  #leto izgradnje
    # r'<span class="velikost" lang="sl">(?P<velikost_nepremicnine>.*?) m2</span><br />'
    # r'<span class="atribut">Zemljišče: <strong>(?P<zemljisce>.*?) m2</strong></span>'
    # r'<span class="cena">(?P<cena>.*?) &euro.*?</span>'


nepremicnine = []
count = 0

# for i in range(1, 667):
#     with open(f'spletne_strani/nepremicnine{i}.html', encoding='utf-8') as f:
#         vsebina = f.read()
#     for zadetek in re.finditer(vzorec, vsebina):
#         nepremicnine.append(zadetek.groupdict())
#         count += 1
#         print(zadetek.groupdict())
#print(nepremicnine)

# orodja.zapisi_json(nepremicnine, 'nepremicnine.json')


#ZA POSKUSAT
with open(f'spletne_strani/nepremicnine5.html', encoding='utf-8') as f:
     vsebina = f.read()

for zadetek in re.finditer(vzorec, vsebina):
    nepremicnine.append(zadetek.groupdict())
    print(zadetek.groupdict())
    count += 1
print(count)


imena_polj = ['ime', 'vrsta', 'koliko_sobno', 'leto_izgradnje', 'zemljisce',
                'velikost', 'cena', 'agencija']
orodja.zapisi_csv(nepremicnine, imena_polj, 'podatki/nepremicnine1.csv')
orodja.zapisi_json(nepremicnine, 'podatki/nepremicnine1.json')

