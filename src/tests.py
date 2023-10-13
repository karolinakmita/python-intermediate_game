import unittest
from src.dragon_class import Dragon


class DragonInitTest(unittest.TestCase):

    def test_init_dragon_name(self):
        dragon = Dragon("Wawelski")
        self.assertEquals(dragon.name, 'Wawelski')


class DragonMoveTest(unittest.TestCase):
    dragon1 = Dragon("Wawelski")

    def test_new_position(self):
        dragon1 = Dragon("Wawelski")
        self.assertEquals(dragon1.change_position(10, 20), (10, 20))
        self.assertEquals(dragon1.move(10, 0, 0, 20), (0, 40))
        self.assertEquals(dragon1.move(10, 15, 0, 0), (5, 40))
        self.assertEquals(dragon1.move(0, 15, 5, 0), (20, 35))
        self.assertEquals(dragon1.move(0, 0, 0, 5), (20, 40))

