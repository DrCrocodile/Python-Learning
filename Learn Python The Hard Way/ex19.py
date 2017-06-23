def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)

def patients_count(in_count,new_count,charge_count):
	print "You have %d patients right now in the hospital." % in_count
	print "You have %d new patients today!" % new_count
	print "You have %d patients charged today!" % charge_count
	print "Now you have %d patients." % (in_count + new_count - charge_count)
	
patients_count(int(raw_input("How many patients do you have now?: ")),
	int(raw_input("How many new patients?: ")),int(raw_input(
	"How many patients got charged today?: ")))
	
print "give it number"
patients_count(20,5,3)

print "use variables"
patients_count(amount_of_cheese,amount_of_crackers,amount_of_cheese)

