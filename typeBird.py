from bird import Bird


class HomeBird(Bird):
    def __init__(self):
        super().__init__()
        self.home_bird = True


class WildBird(Bird):
    def __init__(self):
        super().__init__()
        self.home_bird = False
