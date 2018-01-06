from swampy.TurtleWorld import *
from random import randint


class Wanderer(Turtle):
    def __init__(self, world, speed=1, clumsiness=60, color='red'):
        Turtle.__init__(self, world)
        self.delay = 0
        self.speed = speed
        self.clumsiness = clumsiness
        self.color = color

        # move to the starting position
        self.pu() 
        self.rt(randint(0,360))
        self.bk(150)

#why is this necessary??
    def step(self):
        """step is invoked by TurtleWorld on every Wobbler, once
        per time step."""
        self.wander()


    def wander(self):
        self.lt(randint(-90,90))
        self.fd(10)
        #self.check_boundary()


    def check_boundary(self):
        # i think the boundary is at 200 for this world.
        if self.x<300 and self.x>-300 and self.y<300 and self.y>-300:
            pass
        else:
            self.undo ()

    def other_turtles(self):
        return [animal for animal in self.world.animals if animal is not self]
        

if __name__ == '__main__':
    # create TurtleWorld
    world = TurtleWorld()
    world.delay = .01
    world.setup_run()

    # make three Wobblers with different speed and clumsiness attributes
    colors = ['orange', 'green', 'purple' ]
    i = 2.0
    for color in colors:
        t = Wanderer(world, i, i*30, color)
        i + 1

    world.mainloop()
