#While loop (and also FOR loop) can be used to have a repetition of a procedure in our code

print("How many time to print the symbol?")
x = int(input()) #x=3

#i is a counter - it keeps track of how many times we went through the loop.
i = 0;

while i < x: # condition for repeating the code - as long as i lower than x
  print("\u27BD")
  i = i + 1   #new value of the counter is more than it used to be

print("We left the loop")