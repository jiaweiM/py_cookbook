class Mario:
    def move(self):
        print("I am moving")


class Muchroom:
    def eat_shroom(self):
        print("Now I am big")


class BigMario(Mario, Muchroom):
    pass
