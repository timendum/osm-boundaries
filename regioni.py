import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from paint import Map

COLOR_A = np.array(mpl.colors.to_rgb("#FFFFCC"))
COLOR_B = np.array(mpl.colors.to_rgb("#FFCC33"))


def color_gradient(max, min, n) -> str:
    r = (n - min) / (max - min)
    return mpl.colors.to_hex((r) * COLOR_A + (1 - r) * COLOR_B)


def regioni() -> None:
    subs = []
    os.chdir("regioni")
    # abruzzo
    map = Map("abruzzo")
    map.add("L'Aquila", 42.34889, 13.39793)
    map.anchor()
    subs.append(map)
    # basilicata
    map = Map("basilicata")
    map.add("Potenza", 40.633333, 15.8)
    map.anchor()
    subs.append(map)
    # calabria
    map = Map("calabria")
    map.add("Catanzaro", 38.90764, 16.59603)
    map.anchor()
    subs.append(map)
    # campania
    map = Map("campania")
    map.add("Napoli", 40.83593, 14.24880, ha="right")
    map.anchor()
    subs.append(map)
    # emilia-romagna
    map = Map("emilia-romagna")
    map.add("Bologna", 44.4938203, 11.3426327)
    map.anchor()
    subs.append(map)
    # friuli-venezia-giulia
    map = Map("friuli-venezia giulia")
    map.add("Trieste", 45.64968, 13.77724, sx=0.001)
    map.anchor()
    subs.append(map)
    # lazio
    map = Map("lazio")
    map.add("Roma", 41.896044886072275, 12.482606274944748)
    map.anchor()
    subs.append(map)
    # liguria
    map = Map("liguria")
    map.add("Genova", 44.41134106773606, 8.932586148813286)
    map.anchor()
    subs.append(map)
    # lombardia
    map = Map("lombardia")
    map.add("Milano", 45.4641943, 9.1896346)
    map.anchor()
    subs.append(map)
    # marche
    map = Map("marche")
    map.add("Ancona", 43.616667, 13.516667)
    map.anchor()
    subs.append(map)
    # molise
    map = Map("molise")
    map.add("Campobasso ", 41.561, 14.6684)
    map.anchor()
    subs.append(map)
    # piemonte
    map = Map("piemonte")
    map.add("Torino", 45.073112102353434, 7.681075004778438)
    map.anchor()
    subs.append(map)
    # puglia
    map = Map("puglia")
    map.add("Bari", 41.12587759005726, 16.86767466653839)
    map.anchor()
    subs.append(map)
    # sardegna
    map = Map("sardegna")
    map.add("Cagliari", 39.216667, 9.116667)
    map.anchor()
    subs.append(map)
    # sicilia
    map = Map("sicilia")
    map.add("Palermo", 38.115296710693436, 13.36232837643423, ha="right")
    map.anchor()
    subs.append(map)
    # toscana
    map = Map("toscana")
    map.add("Firenze", 43.77317381412821, 11.255981678040753)
    map.anchor()
    subs.append(map)
    # trentino-alto-adige
    map = Map("trentino-alto adige")
    map.add("Trento", 46.066667, 11.116667)
    map.anchor()
    subs.append(map)
    # umbria
    map = Map("umbria")
    map.add("Perugia", 43.1121, 12.3888)
    map.anchor()
    subs.append(map)
    # valle-aosta
    map = Map("valle-aosta")
    map.add("Aosta", 45.737222, 7.320556)
    map.anchor()
    subs.append(map)
    # veneto
    map = Map("veneto")
    map.add("Venezia", 45.439722, 12.331944)
    map.anchor()
    subs.append(map)
    # ALL
    fig, ax = plt.subplots(figsize=(10, 10), constrained_layout=True)
    ocenters = [map.ocenter for map in subs]
    min_ocenter = min(ocenters)
    max_ocenter = max(ocenters)
    for map in subs:
        print(f"{map.name};{map.ocenter:.2f}")
        color = color_gradient(min_ocenter, max_ocenter, map.ocenter)
        for points in map.coordinates:
            x, y = zip(*points)
            ax.fill(x, y, facecolor=color, edgecolor="black", linewidth=1)
        ax.plot([map.center[0]], [map.center[1]], marker="x", color="black")
        ax.plot([map.labels[0][0]], [map.labels[0][1]], marker="o", color="black")
    ax.axis("off")
    ax.set_adjustable("datalim")
    ax.set_title("Regioni d'Italia")
    # distorzione per la proiezione di Mercatore
    ax.set_aspect(1.343523427875777)  # (1 / cos(radians(41.9)))
    # legenda
    legend_elements = []
    for i in range(5):
        cvalue = (max_ocenter - min_ocenter) / 4 * i + min_ocenter
        legend_elements.append(
            Line2D(
                [0],
                [0],
                marker="o",
                color=ax.get_facecolor(),
                markerfacecolor=color_gradient(min_ocenter, max_ocenter, cvalue),
                label=f"{cvalue:.0f}%",
                markersize=15,
            )
        )
    ax.legend(handles=legend_elements, loc="lower left")
    fig.savefig("regioni.png", bbox_inches="tight")


if __name__ == "__main__":
    regioni()
