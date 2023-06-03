[out:csv( "de:regionalschluessel", name, total, nodes, ways, relations )];

//All areas with regional key (German: "Regionalschlüssel") starting with 057
area["de:regionalschluessel"~"^01061.*"];

// Count the pharmacies in each area
foreach->.regio(
  // Collect all Nodes, Ways and Relations wth amenity=pharmacy in the current area
  ( node(area.regio)[amenity=pharmacy];
    way(area.regio)[amenity=pharmacy];
    rel(area.regio)[amenity=pharmacy];);
  
  make count "de:regionalschluessel" = regio.set(t[ "de:regionalschluessel"]),
             name = regio.set(t["name"]),
             total = count(nodes) + count(ways) + count(relations),
             nodes = count(nodes),
             ways = count(ways),
             relations = count(relations);
  out;
);
