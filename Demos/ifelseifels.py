print("What is your name")
n = input()
#print("do you have a dog? (typ True or False")
#dog = input
#bool is boolean database - only stores True/False


if len(n) > 9:
  print("You have a very looooong name!")
  print("your name contains {} letters".format(len(n)))
elif len (n) > 6:
 print("Your name is a bit long. Consider a nickname")
elif len(n) < 3:
  print("You name is veeery short")
else:
  print("Your name is quite okay")
print("This is the END of program!")