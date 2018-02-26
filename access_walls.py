filteredElementCollector = FilteredElementCollector(doc)
walls = filteredElementCollector.OfClass(Wall)
for wall in walls:
  print wall.Name, wall.Id
