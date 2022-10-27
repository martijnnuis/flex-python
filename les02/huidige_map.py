import os

mapnaam = input("welke naam wil je voor je map? ")

lengte_mapnaam = len(mapnaam)
if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("de map " + mapnaam + " is gemaakt!")
else:
    print("je hebt geen mapnaam ingevoerd")