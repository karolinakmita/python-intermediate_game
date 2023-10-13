class Dragon:
    """
    >>> dragon1 = Dragon('Wawelski')
    >>> print(dragon1.name)
    Wawelski
    >>> dragon1.change_position(10, 20)
    (10, 20)
    >>> dragon1.move(10, 0, 0, 20)
    (0, 40)
    >>> dragon1.move(10, 15, 0, 0)
    (5, 40)
    >>> dragon1.move(0, 15, 5, 0)
    (20, 35)
    >>> dragon1.move(0, 0, 0, 5)
    (20, 40)
    """
    def __init__(self, name, x = 1, y = 2):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return self.name

    def change_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        return self.x, self.y

    def move(self, left=0, right=0, up=0, down=0):
        self.x = self.x - left + right
        self.y = self.y + down - up
        return self.x, self.y

