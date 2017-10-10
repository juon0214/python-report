Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> t.shape("turtle")
>>> angle = 80
>>> t.bgcolor("black")
>>> t.color("green)
	
SyntaxError: EOL while scanning string literal
>>> t.color("green")
>>> t.speed(0)
>>> for x in range(180):
	t.forward(x)
	t.left(angle)

	
>>> t.color("red")
>>> t.speed(0)
>>> angle = 120
>>> for x in range(200):
	t.forward(x)
	t.right(angle)

	
>>> t.right(120)
>>> t.color("blue")
>>> t.color("orange")
>>> t.forward(300)
>>> angle = 30
>>> for x in range(250):
	t.forward(x)
	t.left(angle)

	
>>> anle = 135
>>> for x in range(300):
	t.forward(x)
	t.right(angle)

	
>>> t.shape("turtle")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    t.shape("turtle")
  File "<string>", line 5, in shape
turtle.Terminator
>>> 
