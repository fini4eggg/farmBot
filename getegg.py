from nameBird import Chicken
from nameBird import Sparrow
from nameBird import Goose
from nameBird import Dove
from farm import Farm

farm = Farm()
chicken = Chicken()
farm.pick_up_eggs(chicken)

goose = Goose()
farm.pick_up_eggs(goose)

dove = Dove()
farm.pick_up_eggs(dove)


sparrow = Sparrow()
farm.pick_up_eggs(sparrow)