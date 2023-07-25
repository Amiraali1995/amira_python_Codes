##exercise
#area of the giving shape height is 5 , length is 4, find the area of triangle , square , circle , and the space of area
PI= 3.14
r=2         # half of the radius 
height=int(input("Enter the height value: "))
print("*******************")
length=int(input("Enter the length: "))
print("*******************")
triangle= 0.5*length*height   #formula of triangle
square=length*length  #formula of square 
circle=(PI*r**2)     #formula of circle
space_area=triangle+square-circle      #space area
print ("The space of area is ",space_area,".cm")