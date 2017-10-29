Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> import random
>>> t.shape("turtle")
>>> t.speed(8)
>>> t.up()
>>> t.goto(200,200)
>>> t.down()
>>> t.pensize(3)
>>> t.goto(-200,200)
>>> t.goto(-200,-200)
>>> t.goto(200,-200)
>>> t.goto(200,200)
>>> t.up()
>>> t.home()
>>> a=random.randint(0,359)
>>> t.setheading(a)
>>> while -200 < t.xcor() < 200 and -200 < t.ycor() < 200: 
	t.fd(3)
	while True:
		b=t.heading()
		if 0<b<45 or 135<b<180 or 225<b<270:
			if -200 < t.xcor() < 200 :
				t.setheading(360-b)
				t.foward(3)
				while -200 < t.xcor() < 200 and -200 < t.ycor() < 200:
					t.foward(3)
			else:
				t.setheading(180-b)
				t.foward(3)
				while -200 < t.xcor() < 200 and -200 < t.ycor() < 200:
					t.foward(3)
		if 45<b<135 or 270<b<315:
			if -200 < t.xcor() < 200 :
				t.setheading(360-b)
				t.foward(3)
				while -200 < t.xcor() < 200 and -200 < t.ycor() < 200:
					t.foward(3)
			else:
				t.setheading(540-b)
				t.foward(3)
				while -200 < t.xcor() < 200 and -200 < t.ycor() < 200:
					t.foward(3)
		if 180<b<225 or 315<b<360:
			if -200 < t.xcor() < 200 :
				t.setheading(360-b)
				t.foward(3)
				while -200 < t.xcor() < 200 and -200 < t.ycor() < 200:
					t.foward(3)
			else:
				t.setheading(540-b)
				t.foward(3)
				while -200 < t.xcor() < 200 and -200 < t.ycor() < 200:
					t.foward(3)
		if a == 0 or a == 45 or a == 90 or a == 135 or a == 180 or a == 225 or a == 270 or a == 315 or a == 360:
			t.left(180)
			t.foward(3)
			while -200 < t.xcor() < 200 and -200 < t.ycor() < 200:
				t.foward(3)
