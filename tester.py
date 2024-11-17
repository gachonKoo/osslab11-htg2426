import geo.utils as utils

# Calculate the length of the hypotenuse (c) when a=3 and b=4
a, b = 3, 4
c = utils.pythagoras(a, b)
print('c =', c)

# Calculate the area of a circle with radius r = 10
r = 10
area = utils.circle(r)
print('area =', area)