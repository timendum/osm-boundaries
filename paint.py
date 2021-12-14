import json
from math import cos, radians, sqrt
from typing import Optional

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from shapely.geometry import Point
from shapely.geometry import shape as makeShape

matplotlib.style.use("fivethirtyeight")
plt.rcParams["figure.constrained_layout.use"] = True
plt.rcParams["lines.markersize"] = 6
plt.rcParams["figure.dpi"] = 200


COLOR = "black"
FONTSIZE = 9


class Map:
    def __init__(self, name: str) -> None:
        self.name = name
        with open(f"{name}.geojson", "r") as fo:
            geojson = json.load(fo)
        self.geojson = geojson
        self.coordinates: list[list[list[float]]] = []
        self.holes: list[list[list[float]]] = []
        if geojson["features"][0]["geometry"]["type"] == "Polygon":
            self.coordinates.append(geojson["features"][0]["geometry"]["coordinates"][0])
            if len(geojson["features"][0]["geometry"]["coordinates"]) > 1:
                self.holes.extend(geojson["features"][0]["geometry"]["coordinates"][1:])
        else:
            for porygon in geojson["features"][0]["geometry"]["coordinates"]:
                self.coordinates.append(porygon[0])
                if len(porygon) > 1:
                    self.holes.extend(porygon[1:])
        # find center
        shape = makeShape(geojson["features"][0]["geometry"])
        self.center = shape.centroid.x, shape.centroid.y
        # calc sqarea
        self.sqarea = sqrt(shape.area)
        self.ocenters: list[float] = []
        self.labels: list[tuple[float, float, "matplotlib.text.Text"]] = []
        self.ax: Optional[matplotlib.axes.Axes] = None
        self.fig: Optional[matplotlib.fig.Figure] = None

    def plot(self, title="") -> None:
        self.fig, self.ax = plt.subplots(figsize=(10, 10), constrained_layout=True)
        if not title:
            title = self.name.capitalize()
        self.ax.set_title(title)
        # plot borders
        for points in self.coordinates:
            x, y = zip(*points)
            self.ax.fill(x, y, facecolor="none", edgecolor=COLOR, linewidth=1)
        # calc dx dy
        ya, yb = self.ax.yaxis.get_data_interval()
        dy = (yb - ya) / 300
        xa, xb = self.ax.xaxis.get_data_interval()
        dx = (xb - xa) / 100
        self.dx = self.dy = (dx + dy) / 2
        # plot centroid
        self.ax.plot([self.center[0]], [self.center[1]], marker="x", color=COLOR)
        self.centroid = self.ax.annotate(
            "Centroide", (self.center[0] + self.dx, self.center[1] + self.dy), fontsize=FONTSIZE
        )
        self.ax.axis("off")
        self.ax.set_adjustable("datalim")
        # distorzione per la proiezione di Mercatore
        self.ax.set_aspect(1 / cos(radians(self.center[1])))

    def add(
        self, label, y, x, sx=None, sy=None, va="baseline", ha="left"
    ) -> Optional["matplotlib.text.Text"]:
        txt = None
        if self.ax:
            if not sy:
                sy = self.dy
            if not sx:
                sx = self.dx
            if va == "top":
                sy = -sy
            if ha == "right":
                sx = -sx
            self.ax.plot([x], [y], marker="o", color=COLOR)
            txt = self.ax.annotate(
                label,
                (x + sx, y + sy),
                fontsize=FONTSIZE,
                verticalalignment=va,
                horizontalalignment=ha,
            )
            self.labels.append((x, y, txt))
        else:
            self.labels.append((x, y, None))
        self.ocenters.append(Point(self.center).distance(Point(x, y)) / self.sqarea * 100)
        return txt

    def anchor(self, loc="lower right") -> Optional[AnchoredText]:
        ocenter = sum(self.ocenters) / len(self.ocenters)
        at = None
        if self.ax:
            at = AnchoredText(
                f"Decentramento: {ocenter:.2f}", prop=dict(size=15), frameon=True, loc=loc
            )
            at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
            self.ax.add_artist(at)
        self.ocenter = ocenter
        return at

    def save(self) -> None:
        if self.fig:
            self.fig.savefig(f"{self.name}.png", bbox_inches="tight")
            plt.close(self.fig)
            self.fig = None
            self.ax = None
