import random
import svgcuts

UNIT = 'in'


def ring(pts, l) :
	for i in range(0, len(pts)) :
		j = (i + 1) % len(pts)
		l.add_line(svgcuts.Line(pts[i], pts[j], unit=UNIT))
	return l

def ring_e(pts) :
	max_x = 0.0
	max_y = 0.0
	for p in pts :
		max_x = max(p.x, max_x)
		max_y = max(p.y, max_y)
	return ring(pts, svgcuts.Layer(max_x, max_y, unit=UNIT))

def village() :
	floor_pts = [
		svgcuts.Point(0.0, 0.0),
		svgcuts.Point(0.5, 0.0),
		svgcuts.Point(0.5, 0.5),
		svgcuts.Point(0.0, 0.5)
	]
	roof_pts = [
		svgcuts.Point(0.0, 0.0),
		svgcuts.Point(0.0, 0.5),
		svgcuts.Point(0.25, 0.25)
	]
	return [
		ring_e(floor_pts),
		ring_e(floor_pts),
		ring_e(roof_pts),
		ring_e(roof_pts)
	]

def road() :
	return ring_e([
		svgcuts.Point(0.0, 0.0),
		svgcuts.Point(1.5, 0.0),
		svgcuts.Point(1.5, 0.25),
		svgcuts.Point(0.0, 0.25)
	])

def wall() :
	pts = []
	for x,y in zip([i * 0.125 for i in range(13)], [(i % 2) * 0.125 + .3 for i in range(13)]) :
		pts.append(svgcuts.Point(x, y))
	pts.append(svgcuts.Point(1.5, 0.0))
	pts.append(svgcuts.Point(0.0, 0.0))

	return ring_e(pts)

def wheat(d=.375) :
	m = d / .8
	pts = [
		(0, .1),
		(.2, .1),
		(0, .3),
		(.2, .3),
		(.35, .1),
		(.45, .1),
		(.28, .3),
		(.47, .3),
		(.6, .1),
		(.8, .1)
	]
	pts_rev = list(pts)
	pts_rev.reverse()
	pts += [(x, y * -1) for (x,y) in pts_rev]
	pts =  [(x, y + .3) for (x, y) in pts]
	pts =  [(x * m, y * m) for (x, y) in pts]
	return ring_e([svgcuts.Point(p[0],p[1]) for p in pts])

def pegboard() :
	d = .21
	intercenter = 0.326842
	from_edge = 0.2218

	group_adj = 0.0292105

	l = svgcuts.Layer(24.0, 6.0, unit=UNIT)
	for yi in range(18) :
		y = from_edge + yi * (intercenter - group_adj) + 9 * (group_adj * (yi // 6))
		#print '%f, %f' % (y, 6.0 - y)
		r = d / 2.0
		for END in [0,1] :
			for xi in range(2, 33) :
				from_edge_x = from_edge + xi * intercenter
				if END == 0 :
					x = from_edge_x
				else :
					x = 24.0 - from_edge_x

				l.add_circle(x, y, r)

	return l


p = pegboard()
print 'writing pegboard.svg'
p.write('pegboard.svg')


boards = []
def make_board() :
	b = svgcuts.Layer(24.0, 6.0, unit=UNIT)
	boards.append(b)
	return b

to_place = []
def place(f, n) :
	global to_place
	for i in range(n) :
		made = f()
		if isinstance(made, list) :
			to_place += made
		else :
			to_place.append(made)

place(lambda: wheat(d=.25), 10)
place(lambda: wheat(), 10)
place(road, 10)
place(wall, 10)
place(village, 10)

while to_place :
	to_place = make_board().pack(to_place)

for i in range(len(boards)) :
	fn = 'board%03d.svg' % i
	print 'writing %s' % fn
	boards[i].write(fn)
