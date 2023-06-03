# Wegweiser Kommune: Neue Indikatoren auf Basis von Mapping Data

## Challenge
Name des Teams: Daten für die Gesellschaft

**1.	Was ist das Ziel eurer Forschung? Oder: Was ist das gesellschaftliche Problem, was ihr mit eurem Projekt bearbeitet? Was ist die Wirkung, die ihr erreichen wollt?**

Im Wegweiser Kommune reichern wir Daten aus der Amtlichen Statistik mit spannenden Indikatoren aus anderen Datenquellen an und bieten sie visuell in Dashboards und Berichten aufbereitet auf Gemeindeebene als Hilfestellung zur Planung kommunaler Räume an.
 
**2.	Was versprecht ihr euch von der Diskussion im Datendialog?**

Während des Datendialogs möchten wir wenig reden und viel coden: Wir möchten mit den Freiwilligen von CorrelAid e.V. einen Prototyp entwickeln. Unsere Idee ist, die Indikatoren der wohnungsnahen Grundversorgung (kommunale Infrastruktur) weiterzuentwickeln, indem Daten von Kartendienstleistern als Grundlage für die Indikatorberechnung genutzt werden. In Frage kommen die Google Places API und die Open Street Map API, wobei letzteres lizenzrechtlich einfacher einzubinden wäre, ggf. aber auf Grund fehlender Einträge nicht hinreichend valide ist. Der Prototyp soll sich zunächst für die Abfrage von Daten zu Apotheken gebaut werden, perspektivisch jedoch auf andere Einrichtungen (Schulen, Bibliotheken, Arztpraxen, etc.) ausgeweitet werden.  

**3.	Habt ihr dafür bereits Daten zur Verfügung?**
Uns liegt eine Liste der Kommunen mit über 5.000 Einwohnern, die auf dem Wegweiser Kommune dargestellt werden, vor. Zudem verfügen wir über Geometriedaten für das geographische Mapping und wird für das Projekt das Apothekenregister für den Abgleich angefragt.

**4.	Welche Datenkompetenzen sollten die Teilnehmer:innen eurer Meinung nach idealerweise haben?**

-	R oder Python (fortgeschritten)
-	Erfahrung in der Interaktion mit APIs
-	Umgang mit Geometriedaten
-	Datenvalidierung

**5.	Gibt es noch weiterführende Links, Publikationen o.ä., mit denen sich die Teilnehmenden vorbereiten können?**
-	Wegweiser Kommune: [Daten - Wegweiser Kommune (wegweiser-kommune.de)](https://www.wegweiser-kommune.de/daten/wohnungsnahe-grundversorgung-apotheke+gemeinden-und-staedte+2017+tabelle)
-	Google Places API: [Dokumentation zur Google Maps Platform  |  Places API  |  Google Developers](https://developers.google.com/maps/documentation/places/web-service?hl=de) und [Informationen zu dem Ortstyp 'type = pharmacy'](https://developers.google.com/maps/documentation/places/web-service/supported_types?hl=de)
-	Open Street Map API: [API – OpenStreetMap Wiki](https://wiki.openstreetmap.org/wiki/API), [Informationen zu dem Tag 'amenity = pharmacy'](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dpharmacy) und [Overpass Turbo Query](https://overpass-turbo.eu/s/1uGP)
-	Relevante R-Packages: A) Google Maps API: ggmap, mapsapi, googleway, etc. B) OSM API: osmdata
-	Relevante Python-Packages: A) Google Maps API: googlemaps B) OSM API: OSMPythonTools, OSMapi

## Daten
- Liste der Kommunen auf dem Wegweiser Kommune
- [Geometrie zu Kommunen Open Data](https://opendata-esri-de.opendata.arcgis.com/datasets/esri-de-content::vg250-gemeindegrenzen/about) oder leicht abgwandelte [Geometrie aus dem Wegweiser Kommune ](https://petstore.swagger.io/?url=https://www.wegweiser-kommune.de/openapi#/default/get_rest_map_data__friendlyUrl_)
- Zuordnung von Postleitzahlen zu Gemeinden
- Apothekenregisterdaten (Stichprobe mit 100 Kommunen)

## Product Backlog Items
Arbeitspaket 1: Für Datenanalyst:innen mit Affinität zu APIs

o	Automatisierte Abfrage der Daten zu Kommunen über Wegweiser Kommune API

o	Path 1: Open Street Maps (Präferenz)
 - Automatisierte Abfrage der Daten zu Apotheken über Open Street Maps API
 
o	Path 2: Google Maps (Back-Up)
 - Automatisierte Abfrage der Daten zu Apotheken über Google Places API 
 
o	Optional: Proof of Concept und Set-up für GitHub Actions (ins. .yml-File in einem festzulegenden Turnus, min. 2x jährlich)

Arbeitspaket 2: Für Datenanalyst:innen mit Affinität zur Indikatorberechnung 
o	Zuordnung der Apotheken zu Kommunen (low-hanging fruit über PLZ)

o	Berechnung von Indikator „Anzahl der Apotheken in Kommune“

o	Abgleich der Daten mit Apothekenregister und Beurteilung Datenvalidität

o	Optional: Berechnung des Indikators „Entfernung der nächsten Apotheke zum Ortskern“ (Zentrum des Apothekenpolygons mit den Geometriedaten der Gemeinden)

Ausblick: Berechnung des Indikators "durchschnittliche Entfernung zur nächsten Apotheke" (hierzu benötigt man Daten zur Bevölkerungsdichte, beispielsweise verfügbar über das [BKG](https://mis.bkg.bund.de/trefferanzeige?docuuid=02B4A03F-A187-484E-B6B6-7C0FF1BC7270), die statt Melderegisterdaten allerdings selbst die Prognosedaten von Nexiga GmbH und Infas nutzen)

## Aufteilung der Regionalschlüssel
```
1.–2. Stelle   = Kennzahl des Bundeslandes
3. Stelle      = Kennzahl des Regierungsbezirks; wenn nicht vorhanden: 0
4.–5. Stelle   = Kennzahl des Landkreises oder der kreisfreien Stadt
6.–9. Stelle   = Verbandsschlüssel
10.–12. Stelle = Gemeindekennzahl
```

## Mögliche Challenges
- Matching Issues
- Datenqualität und -Vollständigkeit

## Network Analyse
Berechnung der kürzesten Laufdistanz von einer Adresse bis zu einer Apotheke. Möglicher Indikator für Kommunen: Mittelwert der Laufdistanzen in einer Gemeinde oder Postleitzahl
Benötigte Daten:
- Straßennetz als Shapefile (Quelle: Openstreetmap)
- Punktkoordinaten von Apotheken (Quelle: Openstreetmap)
- Punktkoordinaten von Adressen (Quelle: Amtliche Liegenschaftskarten, INSPIRE)
R packages:
- sf und sfnetworks
- Vignettte für "sfnetwork": https://cran.r-project.org/web/packages/sfnetworks/vignettes/sfn04_routing.html

## Overpass Query for Germany
[out:csv( ::id, name, ::center, ::lat, ::lon, "addr:city", "addr:street", "addr:housenumber", "addr:postcode", "opening_hours")];
area["ISO3166-1"="DE"]->.searchArea;
(
  node["amenity"="pharmacy"](area.searchArea);
  way["amenity"="pharmacy"](area.searchArea);
  relation["amenity"="pharmacy"](area.searchArea);
  node["healthcare" = "pharmacy"](area.searchArea);
  way["healthcare" = "pharmacy"](area.searchArea);
  relation["healthcare" = "pharmacy"](area.searchArea);
);
out center;

## Mögliche weitere Analysen

### Apothekensterben
- Um zu schauen, welche Regionen besonders betroffen von "Apothekensterben" sind, haben wir einen Datensatz mit geschlossenen Apotheken aus OSM gezogen. 
- Files: disused_pharmacy.csv (data) und disused_pharmacy.txt (benutzte query)
- Es sind ca. 1000 Apotheken Deutschlandweit im Datensatz. 
- Als Einschränkung wurde direkt angemerkt, dass die Datenqualität schwierig ist, weil es nicht klar ist, wann die Apotheke geschlossen wurde (teilw. wohl historische Apotheken, teilw. kürzlich geschlossene, teilw. sind sie nur umgezogen). 
- Analyse tbd


### Distanz zur nächsten Apotheke basierend auf Bevölkerungs-Raster
- Ziel: einen weiteren Indikator schaffen für den Zugang zu Apotheken, der die Laufdistanz der Bevölkerung zur nächstgelegenen Apotheke abbildet. 
- Idee: Wir berechnen pro Kommune die Distanz verschiedener Punkte innerhalb der Kommunen (welche einen Wohnsitz-Proxy darstellen) zur nächstgelegenen Apotheke. Die Distanz-Berechnung könnte Luftlinie sein oder alternativ über eine Straßennetz-Distanz-Berechnung (Netzwerkanalyse mit sfnetworks). 
- Vorgehen: 
- (1) Daten vom Mikrozensus über Bevölkerungsdichte: Der Mikrozensus 2011 stellt Daten als CSV zur Verfügung, in denen Deutschland in ein Grid mit 100m Kantenlänge eingeteilt wird und pro Gridzelle die Anzahl der dort lebenden Personen angegeben wird (https://www.zensus2011.de/DE/Home/Aktuelles/DemografischeGrunddaten.html > Download-Tabelle "Bevölkerung im 100 Meter-Gitter" im CSV-Format (zip, 105MB, nicht barrierefrei), Achtung die CSV hat 1,3 GB). 
- (2) Für jede Gridzelle in der mind. 1 Person lebt, nehmen wir den Centerpoint (berechnet aus den 4 Eckpunkten) und berechnen davon die Distanz zur nächstgelegenen Apotheke. 
- (3) Damit haben wir für jede Gridzelle folgende Informationen: In welcher Kommune liegt die Zelle, wie viele Personen liegen darin, was ist die Distanz zur nächsten Apotheke. Daraus berechnen wir für jede Kommune eine gewichtete durchschnittliche Distanz der dort lebenden Personen zu der für sie nächstgelegenen Apotheke.

