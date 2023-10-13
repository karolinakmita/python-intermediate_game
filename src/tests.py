import unittest
from src.dragon_class import Dragon
from random import seed

seed(0)


class DragonTest(unittest.TestCase):

    def test_init_dragon_name(self):
        dragon = Dragon("Wawelski")
        self.assertEquals(dragon.name, 'Wawelski')

    def test_new_position(self):
        dragon1 = Dragon("Wawelski")
        self.assertEquals(dragon1.change_position(10, 20), (10, 20))
        self.assertEquals(dragon1.move(10, 0, 0, 20), (0, 40))
        self.assertEquals(dragon1.move(10, 15, 0, 0), (5, 40))
        self.assertEquals(dragon1.move(0, 15, 5, 0), (20, 35))
        self.assertEquals(dragon1.move(0, 0, 0, 5), (20, 40))

    def test_dragon_demage(self):
        dragon1 = Dragon("Wawelski")
        dragon1.dragon_demage(10)
        self.assertEquals(dragon1.lifepoints, 89)
        dragon1.dragon_demage(20)
        self.assertEquals(dragon1.lifepoints, 69)
        dragon1.dragon_demage(30)
        self.assertEquals(dragon1.lifepoints, 39)
        dragon1.dragon_demage(40)
        self.assertEquals(dragon1.lifepoints, 0)
        dragon1.dragon_demage(50)
        self.assertEquals(dragon1.lifepoints, 0)

