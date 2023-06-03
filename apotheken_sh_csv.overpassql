[out:csv( ::id, name, ::center, ::lat, ::lon, "addr:city", "addr:street", "addr:housenumber", "addr:postcode", "opening_hours")];
area["de:regionalschluessel"~"^01.*"]->.searchArea;
(
  node["amenity"="pharmacy"](area.searchArea);
  way["amenity"="pharmacy"](area.searchArea);
  relation["amenity"="pharmacy"](area.searchArea);
  node["healthcare" = "pharmacy"](area.searchArea);
  way["healthcare" = "pharmacy"](area.searchArea);
  relation["healthcare" = "pharmacy"](area.searchArea);
);
out center;
