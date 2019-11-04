import re
import orodja

#funkcija ki se zapelje po vseh straneh in jih shrani
def shrani_strani_iz_nepremicnine(stevilo_oglasov):
    stevilo_strani = stevilo_oglasov // 30 + 1
    for stevilka in range(1, stevilo_strani + 1):
        url = (
            f'https://www.nepremicnine.net/oglasi-prodaja/slovenija/{stevilka}/'             #f dela kot format
        )
        orodja.shrani_spletno_stran(url, f'nepremicnine{stevilka}.html', vsili_prenos=False)


with open('nepremicnine3.html', encoding='utf-8') as f:
    vsebina = f.read()

vzorec = (
    r'<span class="title">(?P<ime>.*?)</span></a></h2>.*?'
    # r'\s*.*\s*.*\s*.*\s*.*'                                        #nepomembno
    # r'<span class="vrsta">(?P<tip>.*?)</span>'

    # r'<span class="title">(?P<ime>.*?)</span></a></h2>.*?'  #imena nepremicninskih oglasov                                       #karkoli vmes 
    # r'<span class="vrsta">(?P<tip>.*?)</span>'              #tip nepremicnine
    # NE DELA!! # r'<span class="atribut">Nadstropje: <strong>P</strong>/3<span class="invisible">'    #nadstropje kak naredit da jemlje iz dveh delckov?
    # r'<span class="atribut leto">Leto: <strong>(?P<leto>.*?)</strong></span><span class="invisible">, </span>'  #leto izgradnje
    # r'<span class="velikost" lang="sl">(?P<velikost_nepremicnine>.*?) m2</span><br />'
    # r'<span class="atribut">Zemljišče: <strong>(?P<zemljisce>.*?) m2</strong></span>'
    # r'<span class="cena">(?P<cena>.*?) &euro.*?</span>'
    )

flags = re.DOTALL

count = 0
for zadetek in re.finditer(vzorec, vsebina):
    print(zadetek.groupdict())
    count += 1
print(count)