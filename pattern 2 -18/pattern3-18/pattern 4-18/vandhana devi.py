from turtle import*
color("black")
pensize(5)
begin_fill()
for i in range(12):
    right(30)
    for i in range(4):
        forward(90)
        right(90)
    color("blue")
    end_fill()
