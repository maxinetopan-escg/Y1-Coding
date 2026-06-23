from turtle import *            	

class Polygon():
 def draw(self,sides):
  penup()
  goto(0,0)
  pendown()

  begin_fill()
  fillcolor("Purple")

  for  c in range(sides): 
   forward(100)
   left(360/sides) 
 
  end_fill()
 
shape=Polygon() 
shape.draw(8)
input()