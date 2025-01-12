import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
yonler = ["left"]
window = t.Screen()
def random_walk():


    for _ in range(360):
        tim.color(random.choice(colours))
        tim.circle(80)
        tim.left(10)
    window.exitonclick()


    
if __name__ == '__main__':
    random_walk()

