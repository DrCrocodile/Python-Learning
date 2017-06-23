tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#print "Look at \a"
#print "Look at\b"

print '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print "I have two names: %r \nand %s" % ("Luse\t\"abc\"fu", "I'd \t\"rather\"")

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,
		