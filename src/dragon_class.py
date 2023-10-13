class Dragon:
    """
    >>> dragon1 = Dragon('Wawelski')
    >>> print(dragon1.name)
    Wawelski
    """
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

