__Author__ = "noduez"

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        #10-9 沉默的猫和狗
        pass
        # print("  Sorry, I can't find that file.")