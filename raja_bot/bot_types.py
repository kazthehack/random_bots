class Location:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class GameImage:
    def __init__(self, url, height, width, x, y):
        self._url = url
        self._height = height
        self._width = width
        self._location = Location(x, y)

    @property
    def url(self):
        return self._url

    @property
    def x(self):
        return self._location.x

    @property
    def y(self):
        return self._location.y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height


class Elements:
    current = "temp.png"

    da_quest_giver = Location(1099, 542)
    da_quest_choice_1 = Location(1662, 616)
    da_quest_loc = Location(1640, 140)

    auto_attack = Location(1328, 752)

    card_image = GameImage("card.png", 406, 288, 815, 419)

    tik_purchase = GameImage("tik_purchase.png", 61, 191 ,1261, 808)
    tik_item = GameImage("tik_item.png", 90, 230, 1422, 807)

    menu_x = GameImage("menu_x.png",62, 60, 1807, 52)

    ex_loc = Location(1323,852)