import math
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

def gold(d = .375) :
	r = d / 2.0
	n = 40
	phi = math.pi * 2
	pts = [svgcuts.Point(r + math.sin(phi * i / float(n)) * r, r + math.cos(phi * i / float(n)) * r) for i in range(n)]
	return ring_e(pts)

def iron(d = .375) :
	m = d / .8
	pts = [svgcuts.Point(x * m, y * m) for (x,y) in [
		(0.1, 0.0),
		(0.7, 0.0),
		(0.8, 0.4),
		(0.75, 0.43),
		(0.5, 0.38),
		(0.3, 0.38),
		(0.05, 0.43),
		(0.0, 0.4)
	]]
	return ring_e(pts)

def clay(d = .375) :
	m = d / .8
	pts = [svgcuts.Point(x * m, y * m) for (x,y) in [
		(0.0, 0.0),
		(0.8, 0.0),
		(0.8, 0.43),
		(0.0, 0.43)
	]]
	return ring_e(pts)

def stone(d = .375) :
	m = d / .8
	pts = [svgcuts.Point(x * m, y * m) for (x,y) in [
		(0.0, 0.0),
		(0.8, 0.0),
		(0.8, 0.8),
		(0.0, 0.8)
	]]
	return ring_e(pts)

def ore(d = .375) :
	m = d / .8
	pts = [svgcuts.Point(x * m, y * m) for (x,y) in [
		(0.0, .2),
		(.1,  .1),
		(.2,.2),
		(.4,0.0),
		(.6,.2),
		(.8,.2),
		(.7, .4),
		(.5, .55),
		(.67, .7),
		(.5, .85),
		(.3, .7),
		(.1, .77),
		(0.0,.6),
		(.1, .4),
		(0.0,.3)
	]]
	return ring_e(pts)

def bread(d = .375) :
	m = d / .9
	pts = [svgcuts.Point(x * m, y * m) for (x,y) in [
		(0.05, 0.28),
		(0.12, 0.18),
		(0.26, 0.1),
		(0.3, 0.15),
		(0.4, 0.05),
		(0.5, 0.06),
		(0.58, 0.14),
		(0.62, 0.1),
		(0.72, 0.05),
		(0.8, 0.1),
		(0.81, 0.13),
		(0.88, 0.14),
		(0.92, 0.2),
		(0.92, 0.3),
		(0.87, 0.43),
		(0.75, 0.5),
		(0.18, 0.5),
		(0.08, 0.4)
	]]
	return ring_e(pts)

def wood(d = .375) :
	m = d / .85
	pts = [svgcuts.Point(x * m - .05, y * m - .05) for (x,y) in [
		(.05, .3),
		(.15, .3),
		(.15, .05),
		(.32, .2),
		(.4, .1),
		(.63, .3),
		(.7, .2),
		(.9, .4),
		(.7, .6),
		(.63, .5),
		(.4, .7),
		(.32, .6),
		(.15, .75),
		(.15, .5),
		(.05, .5)

	]]
	return ring_e(pts)


def sheep(d = .375) :
	m = d / .85
	pts = [svgcuts.Point(y * m - .05, x * m) for (x,y) in [
		(0, .3),
		(.05, .2),
		(.18, .2),
		(.22, .25),
		(.3, .14),
		(.35, .1),
		(.46, .18),
		(.6, .06),
		(.73, .09),
		(.8, .2),
		(.88, .2),
		(.88, .27),
		(.8, .28),
		(.8, .38),
		(.77, .47),
		(.75, .53),
		(.75, .8),
		(.65, .8),
		(.65, .53),
		(.57, .5),
		(.52, .44),
		(.5, .5),
		(.42, .54),
		(.42, .8),
		(.33, .8),
		(.33, .54),
		(.25, .5),
		(.23, .43),
		(.15, .48),
		(.06, .48),
		(0, .4)
	]]
	return ring_e(pts)

### units

def ballista(d = .575) :
	m = d / .8
	pts = [svgcuts.Point(x * m, y * m) for (x,y) in [
		(.05, .1),
		(.52, .05),
		(.6,.3),
		(.7, .33),
		(.78, .5),
		(.75, .55),
		(.75, .65),
		(.7,.65),
		(.72, .65),
		(.76, .70),
		(.61, .7),
		(.63, .66),
		(.3, .66),
		(.31, .7),
		(.25, .74),
		(.17, .7),
		(.19, .66),
		(.14, .66),
		(.14, .6),
		(.43, .18),
		(.05,.18)
	]]
	return ring_e(pts)

def soldier(d = .575) :
	m = d / .95
	pts = [svgcuts.Point(x * m, y * m) for (x,y) in [
		(0.0, .3),
		(0.2, .2),
		(.56, .2),
		(.56, 0.0),
		(.65, 0.0),
		(.65, .24),
		(.95, .24),
		(.95, .36),
		(.65, .36),
		(.65, .56),
		(.56, .56),
		(.56, .4),
		(.2, .4)
	]]
	return ring_e(pts)

def craftsman(d = .575) :
	m = d / .8
	pts = [svgcuts.Point(x * m, y * m) for (x,y) in [
		(.2, 0.0),
		(.4, .2),
		(.4, .3),
		(.8, .3),
		(.8, .48),
		(.4, .48),
		(.4, .7),
		(0.0, .7),
		(.0, .2)
	]]
	return ring_e(pts)

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
place(lambda: gold(d=.25), 10)
place(lambda: gold(), 10)
place(lambda: iron(d=.25), 10)
place(lambda: iron(), 10)
place(lambda: clay(d=.25), 10)
place(lambda: clay(), 10)
place(lambda: stone(d=.25), 10)
place(lambda: stone(), 10)
place(lambda: ore(d=.25), 10)
place(lambda: ore(), 10)
place(lambda: bread(d=.25), 10)
place(lambda: bread(), 10)
place(lambda: wood(d=.25), 10)
place(lambda: wood(), 10)
place(lambda: sheep(d=.25), 10)
place(lambda: sheep(), 10)
place(road, 10)
place(wall, 10)
place(village, 10)

place(ballista, 5)
place(soldier, 5)
place(craftsman, 5)

while to_place :
	to_place = make_board().pack(to_place)

for i in range(len(boards)) :
	fn = 'board%03d.svg' % i
	print 'writing %s' % fn
	boards[i].write(fn)
