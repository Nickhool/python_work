__Author__ = "noduez"

# 10-3 访客
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)