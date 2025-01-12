import turtle
global aci 
global kenar_sayisi 

def draw_square():
    window = turtle.Screen()


    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    aci = 120
    kenar_sayisi = 3
   
    while True:
        if kenar_sayisi == 6:
            brad.forward(100)
            break
        for _ in range(0,kenar_sayisi):       
            brad.forward(100)
            brad.right(aci)
            brad.forward(100)
        kenar_sayisi = kenar_sayisi + 1
        aci= aci -30
    window.exitonclick()


draw_square()
