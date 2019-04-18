__Author__ = "noduez"

#10-4访客名单
filename = 'guest_book.txt'
# prompt = 'please Input a name: '
# while True:
#     name = input(prompt)
#     with open(filename, 'a') as file_object:
#         file_object.write(name+'\n')

print("Enter 'quit' when you are finished.")
while True:
   name = input("\nWhat's your name? ")
   if name == 'quit':
       break
   else:
       with open(filename, 'a') as f:
           f.write(name + "\n")
       print("Hi " + name + ", you've been added to the guest book.")


