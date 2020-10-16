from typeBird import HomeBird
from typeBird import WildBird


class Chicken(HomeBird):
    def __init__(self):
        super().__init__()
        self.name = "Курица"
        self.egg = 4

    def get_name(self):
        return self.name

    def get_eggs(self):
        return self.egg

    def is_home_bird(self):
        return self.home_bird


class Goose(HomeBird):
    def __init__(self):
        super().__init__()
        self.name = "Гусь"
        self.egg = 2

    def get_name(self):
        return self.name

    def get_eggs(self):
        return self.egg

    def is_home_bird(self):
        return self.home_bird
#
#
class Sparrow(WildBird):
    def __init__(self):
        super().__init__()
        self.name = "Воробей"

    def get_name(self):
        return self.name

    def is_home_bird(self):
        return self.home_bird

class Dove(WildBird):
    def __init__(self):
        super().__init__()
        self.name = "Голубь"

    def get_name(self):
        return self.name

    def is_home_bird(self):
        return self.home_bird
