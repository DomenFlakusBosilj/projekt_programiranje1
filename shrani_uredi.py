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


vzorec = re.compile (
    r'<span class="title">(?P<ime>.*?)</span></a></h2>.*?'
    r'<span class="posr">(?P<posred>.*?): <span class="vrsta">(?P<vrsta>.*?)</span>.*?'
    r'<span class="tipi">(?P<tip>.*?)</span>.*?'
    r'<span class="atribut leto">Leto: <strong>(?P<leto>.*?)</strong>.*?'
    r'<span class="atribut">Zemljišče: <strong>(?P<zemljisce>.*?) m2</strong>.*?'
    r'<span class="velikost" lang="sl">(?P<velikost>.*?) m2</span><br />.*?'
    r'<span class="cena">(?P<cena>.*?) &euro.*?</span>.*?'
    r'<span class="agencija">(?P<agencija>.*?)</span>', 
    flags=re.DOTALL
    )


def razbij_na_oglase(vsebina_strani):
    vzorec_oglasa = re.compile (
        r'<!--<meta itemprop="url" content.*?'
        r'</i><span>O ponudniku</span></a>',
        flags=re.DOTALL    
        )
    oglasi = re.findall(vzorec_oglasa, vsebina_strani)
    return oglasi


def naredi_seznam_nepremicnin(st_htmljev, vzorec):
    nepremicnine = []
    count = 0
    count_stran = 0
    for i in range(1, (st_htmljev+1)):
        if i == 118:
            continue
        else:
            count = 0
            with open(f'spletne_strani/nepremicnine{i}.html', encoding='utf-8') as f:
                vsebina = f.read()
                count_stran += 1
                print(count_stran)
                oglasi = razbij_na_oglase(vsebina)
                for oglas in oglasi:
                    for zadetek in re.finditer(vzorec, oglas):
                        nepremicnine.append(zadetek.groupdict())
                        count += 1
                        #print(zadetek.groupdict())
                    #print(count)
    #print(nepremicnine)
    return nepremicnine


def popravi_zapisi(seznam, i):
    for nepremicnina in seznam:
        nepremicnina['leto'] = int(nepremicnina['leto'])
        nepremicnina['zemljisce'] = float(nepremicnina['zemljisce'].replace('.','').replace(',','.'))
        nepremicnina['velikost'] = float(nepremicnina['velikost'].replace('.','').replace(',','.'))
        nepremicnina['cena'] = float(nepremicnina['cena'].replace('.','').replace(',','.'))
    imena_polj = ['ime', 'posred', 'vrsta', 'tip', 'leto', 'zemljisce',
                'velikost', 'cena', 'agencija']
    orodja.zapisi_csv(seznam, imena_polj, f'podatki/nepremicnine{i}.csv')
    orodja.zapisi_json(seznam, f'podatki/nepremicnine{i}.json')

