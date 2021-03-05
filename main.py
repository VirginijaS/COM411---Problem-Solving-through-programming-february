#Program that displays a menu and allows the user to either see a nice message, calculate areas of rectangle or triangle or display a time table for a number.

print("Please choose and option from the menu:\n1-Nice mesage\n2-Area of a rectangle\n3-Area of triangle\n4-Times table")

option = int(input())

if option == 1:
  print("Today will be a good day!")
elif option == 2:
  print("Enter the lenght of rectangle:")
  l = int(input())
  print("Enter the witdth of rectangle")
  w = int(input())
  area = w*1
  print("The area of this rectangle was {}".format(area))
elif option == 3:
  print("Enter the base of triangle:")
  base = float(input())
  print("Enter the height of the triangle")
  height = float(input())
  area = 0.5*base*height
  print("the area of this triangle was {:.2f}".format(area))
elif option == 4:
  print("What number would you like to see time table for?")
  n = int(input())
  for i in range(1,11,1):
    print("{}x{} = ".format(n,i*i))
else:
  print("There is no such option. Go to specsavers!")