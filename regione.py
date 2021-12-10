import os

from paint import Map


def regioni():
    os.chdir("regioni")
    # abruzzo
    map = Map("abruzzo")
    map.plot()
    map.add("L'Aquila", 42.34889, 13.39793)
    map.anchor()
    map.save()
    # basilicata
    map = Map("basilicata")
    map.plot()
    map.add("Potenza", 40.633333, 15.8)
    map.anchor()
    map.save()
    # calabria
    map = Map("calabria")
    map.plot()
    map.add("Catanzaro", 38.90764, 16.59603)
    map.anchor()
    map.save()
    # campania
    map = Map("campania")
    map.plot()
    map.add("Napoli", 40.83593, 14.24880, ha="right")
    map.anchor("lower left")
    map.save()
    # emilia-romagna
    map = Map("emilia-romagna")
    map.plot()
    map.add("Bologna", 44.4938203, 11.3426327)
    map.anchor("lower left")
    map.save()
    # friuli-venezia-giulia
    map = Map("friuli-venezia giulia")
    map.plot("Friuli-Venezia Giulia")
    map.add("Trieste", 45.64968, 13.77724, sx=0.001)
    map.anchor("lower left")
    map.add("Udine", 46.0634632, 13.2358377)
    map.save()
    # lazio
    map = Map("lazio")
    map.plot()
    map.add("Roma", 41.896044886072275, 12.482606274944748)
    map.anchor("lower left")
    map.save()
    # liguria
    map = Map("liguria")
    map.plot()
    map.add("Genova", 44.41134106773606, 8.932586148813286)
    map.anchor()
    map.save()
    # lombardia
    map = Map("lombardia")
    map.plot()
    map.add("Milano", 45.4641943, 9.1896346)
    map.anchor()
    map.save()
    # marche
    map = Map("marche")
    map.plot()
    map.add("Ancona", 43.616667, 13.516667)
    map.anchor("lower left")
    map.save()
    # molise
    map = Map("molise")
    map.plot()
    map.add("Campobasso ", 41.561, 14.6684)
    map.anchor()
    map.save()
    # piemonte
    map = Map("piemonte")
    map.plot()
    map.add("Torino", 45.073112102353434, 7.681075004778438)
    map.anchor()
    map.save()
    # puglia
    map = Map("puglia")
    map.plot()
    map.add("Bari", 41.12587759005726, 16.86767466653839)
    map.anchor("lower left")
    map.save()
    # sardegna
    map = Map("sardegna")
    map.plot()
    map.add("Cagliari", 39.216667, 9.116667)
    map.anchor()
    map.save()
    # sicilia
    map = Map("sicilia")
    map.plot()
    map.add("Palermo", 38.115296710693436, 13.36232837643423, ha="right")
    map.anchor("lower left")
    map.save()
    # toscana
    map = Map("toscana")
    map.plot()
    map.add("Firenze", 43.77317381412821, 11.255981678040753)
    map.anchor()
    map.save()
    # trentino-alto-adige
    map = Map("trentino-alto adige")
    map.plot("Trentino-Alto Adige")
    map.add("Trento", 46.066667, 11.116667)
    map.anchor()
    map.save()
    # umbria
    map = Map("umbria")
    map.plot()
    map.add("Perugia", 43.1121, 12.3888)
    map.anchor()
    map.save()
    # valle-aosta
    map = Map("valle-aosta")
    map.plot("Valle d'Aosta")
    map.add("Aosta", 45.737222, 7.320556)
    map.anchor()
    map.save()
    # veneto
    map = Map("veneto")
    map.plot()
    map.add("Venezia", 45.439722, 12.331944)
    map.anchor("lower left")
    # map.add("Verona", 45.438611, 10.992778)
    map.save()


if __name__ == "__main__":
    regioni()
