# Wegweiser Kommune: Neue Indikatoren auf Basis von Mapping Data

## Challenge
Name des Teams: Daten für die Gesellschaft

**1.	Was ist das Ziel eurer Forschung? Oder: Was ist das gesellschaftliche Problem, was ihr mit eurem Projekt bearbeitet? Was ist die Wirkung, die ihr erreichen wollt?**

Im Wegweiser Kommune reichern wir Daten aus der Amtlichen Statistik mit spannenden Indikatoren aus anderen Datenquellen an und bieten sie visuell in Dashboards und Berichten aufbereitet auf Gemeindeebene als Hilfestellung zur Planung kommunaler Räume an.
 
**2.	Was versprecht ihr euch von der Diskussion im Datendialog?**

Während des Datendialogs möchten wir wenig reden und viel coden: Wir möchten mit den Freiwilligen von CorrelAid e.V. einen Prototyp entwickeln. Unsere Idee ist, die Indikatoren der wohnungsnahen Grundversorgung (kommunale Infrastruktur) weiterzuentwickeln, indem Daten von Kartendienstleistern als Grundlage für die Indikatorberechnung genutzt werden. In Frage kommen die Google Places API und die Open Street Map API, wobei letzteres lizenzrechtlich einfacher einzubinden wäre, ggf. aber auf Grund fehlender Einträge nicht hinreichend valide ist. Der Prototyp soll sich zunächst für die Abfrage von Daten zu Apotheken gebaut werden, perspektivisch jedoch auf andere Einrichtungen (Schulen, Bibliotheken, Arztpraxen, etc.) ausgeweitet werden.  

-	Path 1: Google Maps
o	Abfrage der Daten zu Apotheken über Google Places API 
o	Abgleich der Daten mit Apothekenregister und Beurteilung Datenvalidität
o	Zuordnung der Apotheken zur Geometrie des Wegweiser Kommunen Portals (Apotheke zu Kommune)
o	Berechnung von Indikatoren „Anzahl der Apotheken in Kommune“, „Entfernung der nächsten Apotheke zum Ortskern“, etc.

-	Path 2: Open Street Maps
o	Abfrage der Daten zu Apotheken über Open Street Maps API
o	Abgleich der Daten mit Apothekenregister und Beurteilung Datenvalidität
o	Zuordnung der Apotheken zur Geometrie des Wegweiser Kommunen Portals (Apotheke zu Kommune)
o	Berechnung von Indikatoren „Anzahl der Apotheken in Kommune“, „Entfernung der nächsten Apotheke zum Ortskern“, etc.
 
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
- [Geometrie zu Kommunen](https://opendata-esri-de.opendata.arcgis.com/datasets/esri-de-content::vg250-gemeindegrenzen/about) (! Originäre Shapefiles nicht lizenziert für die Herausgabe!)
- Apothekenregisterdaten (Stichprobe mit 100 Kommunen)

## Product Backlog Items

o	Abfrage der Daten zu Kommunen über Wegweiser Kommune API

o	Path 1: Google Maps
 - Abfrage der Daten zu Apotheken über Google Places API 
 - Abgleich der Daten mit Apothekenregister und Beurteilung Datenvalidität

o	Path 2: Open Street Maps
 - Abfrage der Daten zu Apotheken über Open Street Maps API
 - Abgleich der Daten mit Apothekenregister und Beurteilung Datenvalidität
o	Zuordnung der Apotheken zur Geometrie des Wegweiser Kommunen Portals (Apotheke zu Kommune)
o	Berechnung von Indikatoren „Anzahl der Apotheken in Kommune“, „Entfernung der nächsten Apotheke zum Ortskern“, etc.

## Mögliche Challenges
- Matching Issues
- Datenqualität und -Vollständigkeit
