import os

from paint import Map


def comuni() -> None:
    os.chdir("comuni")
    # milano
    map = Map("milano")
    map.plot()
    map.add("Palazzo Marino", 45.46665, 9.19063)
    map.anchor()
    map.save()
    # roma
    map = Map("roma")
    map.plot()
    map.centroid.set_horizontalalignment("right")
    map.centroid.set_verticalalignment("top")
    map.centroid.set_position((map.center[0], map.center[1] + 0.009))
    map.add("Colosseo", 41.89023, 12.49236, va="top")
    # map.add("Campidoglio", 41.8933019, 12.4820307)
    map.add("Piazza Venezia", 41.896044886072275, 12.482606274944748)
    map.anchor()
    map.save()
    # napoli
    map = Map("napoli")
    map.plot()
    map.add("Piazza Municipio", 40.84000825011181, 14.251955191471545, ha="right")
    map.add("Piazza del Plebiscito", 40.83584, 14.24857, va="top", ha="right")
    map.anchor()
    map.save()
    # torino
    map = Map("torino")
    map.plot()
    map.centroid.set_horizontalalignment("right")
    map.centroid.set_verticalalignment("top")
    map.centroid.set_position((map.centroid.xy[0] - map.dx, map.centroid.xy[1] + map.dy))
    map.add("Piazza Palazzo di Città", 45.073112102353434, 7.681075004778438)
    map.anchor()
    map.save()
    # palermo
    map = Map("palermo")
    map.plot()
    map.add("Palazzo Pretorio", 38.115296710693436, 13.36232837643423, ha="right")
    map.anchor()
    map.save()
    # ravenna
    map = Map("ravenna")
    map.plot()
    map.add(" Piazza del Popolo", 44.41754474065065, 12.1990831668707)
    map.centroid.set_position((map.centroid.xy[0] + map.dx, map.centroid.xy[1] - 0.005))
    map.anchor("lower left")
    map.save()
    # genova
    map = Map("genova")
    map.plot()
    map.add("Palazzo Doria Tursi", 44.41134106773606, 8.932586148813286)
    map.add(" Piazza De Ferrari", 44.40732418141119, 8.934092003242254, va="top")
    map.anchor("lower left")
    map.save()
    # firenze
    map = Map("firenze")
    map.plot()
    map.add("Piazza del Duomo", 43.77317381412821, 11.255981678040753)
    map.add("Palazzo della Signoria", 43.76970477133512, 11.2556407170798, va="top")
    map.anchor()
    map.save()
    # sassari
    map = Map("sassari")
    map.plot()
    map.add("Palazzo Ducale", 40.726696148872655, 8.559444702593193)
    map.add("Piazza D'Italia", 40.7249927769171, 8.564340445969853, va="top")
    map.anchor()
    map.save()
    # cerignola
    map = Map("cerignola")
    map.plot()
    map.add("Torre dell'Orologio", 41.26578930057921, 15.89372483438155, va="top", sy=0.003)
    map.add("Piazza della Repubblica", 41.266022330172795, 15.903902121669773)
    map.anchor()
    map.save()
    # noto
    map = Map("noto")
    map.plot()
    map.add("Cattedrale di Noto", 36.89134187706559, 15.07102006671105)
    map.add("Municipio", 36.89159013011308, 15.068331570469713, ha="right")
    map.anchor()
    map.save()
    # bari
    map = Map("bari")
    map.plot()
    map.add("Basilica San Nicola", 41.130622716349286, 16.870613921830852)
    map.add("Municipio", 41.12587759005726, 16.86767466653839, ha="right", va="top")
    map.add("Teatro Petruzzelli", 41.12369411398924, 16.872703665122383, va="top")
    map.anchor()
    map.save()
    # bologna
    map = Map("bologna")
    map.plot()
    map.add("Piazza Maggiore", 44.49379840637986, 11.34313891389058)
    map.anchor()
    map.save()


if __name__ == "__main__":
    comuni()
