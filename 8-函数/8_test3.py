__Author__ = "noduez"

#8-9 魔术师
def show_magicians(magicians):
   """Print the name of each magician in the list."""
   for magician in magicians:
       print(magician.title())
magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

#8-10 了不起的魔术师
great_magicians = []
def make_great(magicians):
    for magician in magicians:
        magician = 'the Great ' + magician
        great_magicians.append(magician)
# make_great(magicians)
# print(great_magicians)

#8-11 不变的魔术师
make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
