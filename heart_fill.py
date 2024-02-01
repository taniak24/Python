import turtle

#draw heart function
def draw_heart():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('red')
    turtle.left(140)
    turtle.forward(224)
    
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()

#write text
def write_message():
    turtle.penup()
    turtle.goto(-190, -15)
    turtle.pendown()
    turtle.color('black')
    turtle.write("WILL YOU BE MY VALENTINE,", font=("Arial", 20, "normal")) #upper line
    
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    turtle.color('black')
    turtle.write("BOB?", font=("Arial", 20, "normal")) #second line

def main(): 
    turtle.title("<3")
    turtle.speed(1)
    turtle.bgcolor('white') #set background color
    draw_heart()
    write_message()
    turtle.done()

#?
if __name__ == "__main__":
    main()