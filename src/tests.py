import unittest
from src.dragon_class import Dragon


class DragonInitTest(unittest.TestCase):

    def test_init_dragon_name(self):
        dragon = Dragon("Wawelski")
        self.assertEquals(dragon.name, 'Wawelski')
