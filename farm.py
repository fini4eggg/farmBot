class Farm:
    def __init__(self):
        pass

    def get_eggs(self, bird):
        if bird.home_bird(self):
            print(f"У птицы {bird.get_name()} {bird.get_eggs()} яиц")
        else:
            print(f"У птицы {bird.get_name()} нет яиц")