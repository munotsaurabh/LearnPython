friends = {"Virat", "rohit", "bhuvi", "Jaddu"}
guests = {"ishant", "ajinkya", "virat", "jaddu", "Ashwin"}

frinds_lower = {f.lower() for f in friends}
guests_lower = {g.lower() for g in guests}

invited = {name.title() for name in frinds_lower.intersection(guests_lower)}

print (invited)