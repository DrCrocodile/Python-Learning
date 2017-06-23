my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)
print "Whatever you input, like %r, %r, and %r, I will print" % ('pig', 'shit', 'damn')
print "Whatever you input, like %s, %s, and %s, I will print" % ('pig', 'shit', 'damn')

print "He's %d centimeters tall." % round(my_height * 2.54)