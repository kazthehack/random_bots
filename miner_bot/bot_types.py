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
    # menu_x = GameImage("menu_x.png",62, 60, 1807, 52)

    box_loc = Location(888,1103)
    center_loc = Location(530, 1450)

    m1 = Location(400,750)
    m2 = Location(900,750)
    m3 = Location(400,1350)
    m4 = Location(900,1350)
    m5 = Location(400,1950)
    m6 = Location(900,1950)

    craft_btn = Location(400,2320)
    exit_btn = Location(1000,150)
    exit_window = Location(970,1090)