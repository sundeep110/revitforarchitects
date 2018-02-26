filteredElementCollector = FilteredElementCollector(doc)
walls = filteredElementCollector.OfClass(Wall)
for wall in walls:
  for parameter in wall.Parameters:
    print parameter.Definition.Name, parameter.AsValueString()
