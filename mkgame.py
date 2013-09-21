import svgcuts

UNIT = 'in'

def ring(pts, l) :
	for i in range(0, len(pts)) :
		j = (i + 1) % len(pts)
		l.add_line(svgcuts.Line(pts[i], pts[j]))
	return l

def road() :
	return ring([
		svgcuts.Point(0.0, 0.0),
		svgcuts.Point(1.75, 0.0),
		svgcuts.Point(1.75, 0.125),
		svgcuts.Point(0.0, 0.125)
	], svgcuts.Layer(1.75, 0.125, unit=UNIT))

def wall() :
	pts = []
	for x,y in zip([i * 0.125 for i in range(15)], [(i % 2) * 0.125 + .3 for i in range(15)]) :
		pts.append(svgcuts.Point(x, y))
	pts.append(svgcuts.Point(1.75, 0.125))
	pts.append(svgcuts.Point(0.0, 0.125))

	return ring(pts, svgcuts.Layer(1.75, 0.425, unit=UNIT))

#w = wall()
#w.write('wall.svg')
