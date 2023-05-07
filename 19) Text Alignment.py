# Enter your code here. Read input from STDIN. Print output to STDOUT
thickness = int(input())
char = 'H'
#Top cone.
for i in range(thickness):
  print((char * i).rjust(thickness - 1) + char + (char * i).ljust(thickness - 1))
#Top Column
for i in range(thickness+1):
  print((char*thickness).center(thickness*2) + (char*thickness).center(thickness*6)) 
#Middle
for i in range((thickness//2)+1):
  print((char*thickness*5).center(thickness*6))
#Bottom Coloumn
for i in range(thickness+1):
  print((char*thickness).center(thickness*2) + (char*thickness).center(thickness*6)) 
#Bottom cone
for i in range(thickness-1,-1,-1):
  print(((char * i).rjust(thickness-1) + char + (char * i).ljust(thickness -1)).center(thickness*10))