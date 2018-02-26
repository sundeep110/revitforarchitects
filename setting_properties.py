filteredElementCollector = FilteredElementCollector(doc)
walls = filteredElementCollector.OfClass(Wall)
for wall in walls:
	for parameter in wall.Parameters:
		if parameter.Definition.Name == 'Comments':
			print 'Before changing - ', parameter.AsString()
			t = Transaction(doc)
			t.Start('Chaning the Comments for wall')
			parameter.Set('I am wall ' + wall.Name)
			t.Commit()
			print 'After changing - '  , parameter.AsString()
