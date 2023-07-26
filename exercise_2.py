#exercise 2
#* calculate total width of all tiles
   #**one black tle:5
   #**9 pair of BWs:90
   #**total width:95
#* calculate gap (one on each end):
   #**100-95=5 total gap
   #ggap/2=2.5 at each end
total_width=100
n=0
black_w=5
white_w=5

total_width=total_width- black_w

while total_width > 0:
    total_width=total_width-white_w-black_w
    n +=1
    if total_width <0:
        break
total_width = total_width+white_w+black_w
print("The gap =",total_width/2)
print("number of tails =",n*2-1)