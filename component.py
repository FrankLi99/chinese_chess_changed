__author__ = 'lenovo'
from world import *
from ApiFunction import *


class Player(object):
    def __init__(self, id, (x, y), image, world, color, image_chosen):
        self.id = id
        self.x = x
        self.y = y
        self.image_chosen = image_chosen
        self.image = image
        self.world = world
        self.color = color
        self.flag_chosen = 0

    def render(self, surface):
        if self.flag_chosen == 0:
            surface.blit(self.image, self.world.PixPosition[self.x][self.y])
        elif self.flag_chosen == 1:
            surface.blit(self.image, self.world.PixPosition[self.x][self.y])
            surface.blit(self.image_chosen, self.world.PixPosition[self.x][self.y])

    def dispose(self):
        self.world.del_player(self)

    def eat(self, player_another):
        if self.satisfy_rule(player_another.x, player_another.y) and not player_another.color == self.color:
            if self.satisfy_rule_color(player_another.x, player_another.y):
                self.world.AllPosition[self.x][self.y] = None
                self.x = player_another.x
                self.y = player_another.y
                player_another.dispose()
                self.world.AllPosition[player_another.x][player_another.y] = self
                return 1
            else:
                return 0
        else:
            return 0

    def move(self, x, y):
        if self.satisfy_rule(x, y) and self.satisfy_rule_color(x, y):
            self.world.AllPosition[self.x][self.y] = None
            self.x = x
            self.y = y
            self.world.AllPosition[x][y] = self
            return 1
        else:
            return 0

    def change_position(self, x, y):
        if self.world.AllPosition[x][y] is None:
            result = self.move(x, y)
        else:
            result = self.eat(self.world.AllPosition[x][y])
        if not result:
            print "you can't do that!"

    def satisfy_rule(self, x, y):
        return 1

    def satisfy_rule_color(self, x, y):
        return 1

    def plot(self):
        pass


class PlayerHorse(Player):
    def __init__(self, id, (x, y), image, world, color, image_chosen):
        Player.__init__(self, id, (x, y), image, world, color, image_chosen)

    def satisfy_rule(self, x, y):
        if abs(self.x - x) == 1:
            if self.y - y == 2:
                if self.world.AllPosition[self.x][self.y-1] is None:
                    return 1
                else:
                    return 0
            elif y - self.y == 2:
                if self.world.AllPosition[self.x][self.y+1] is None:
                    return 1
                else:
                    return 0
            else:
                return 0
        elif abs(self.y - y) == 1:
            if self.x - x == 2:
                if self.world.AllPosition[self.x-1][self.y] is None:
                    return 1
                else:
                    return 0
            if x - self.x == 2:
                if self.world.AllPosition[self.x+1][self.y] is None:
                    return 1
                else:
                    return 0
            else:
                return 0
        elif self.x == x and self.y == y:
            return 1
        else:
            return 0


class PlayerCar(Player):
    def __init__(self, id, (x, y), image, world, color, image_chosen):
        Player.__init__(self, id, (x, y), image, world, color, image_chosen)

    def satisfy_rule(self, x, y):
        if self.x == x:
            return Api.is_exist_l(y, self.y, x, self.world) == 0
        elif self.y == y:
            return Api.is_exist_r(x, self.x, y, self.world) == 0
        elif self.x == x and self.y == y:
            return 1
        else:
            return 0


class PlayerRanker(Player):
    def __init__(self, id, (x, y), image, world, color, image_chosen):
        Player.__init__(self, id, (x, y), image, world, color, image_chosen)

    def satisfy_rule(self, x, y):
        if (abs(y - self.y) == 1) or (abs(x - self.x) == 1):
            if not ((abs(y - self.y) == 1) and (abs(x - self.x) == 1)):
                return 1
        elif self.x == x and self.y == y:
            return 1
        else:
            return 0

    def satisfy_rule_color(self, x, y):
        if self.color == "red":
            if y >= self.y:
                return 1
            else:
                return 0
        elif self.color == "black":
            if y <= self.y:
                return 1
            else:
                return 0


class PlayerGuard(Player):
    def __init__(self, id, (x, y), image, world, color, image_chosen):
        Player.__init__(self, id, (x, y), image, world, color, image_chosen)

    def satisfy_rule(self, x, y):
        if abs(self.x - x) == 1:
            if abs(self.y - y) == 1:
                return 1
            else:
                return 0
        elif self.x == x and self.y == y:
            return 1
        else:
            return 0

    def satisfy_rule_color(self, x, y):
        if self.color == "red":
            if (x >= 3) and (x <= 5) and (y <= 2):
                return 1
            else:
                return 0
        elif self.color == "black":
            if (x >= 3) and (x <= 5) and (y >= 7):
                return 1
            else:
                return 0


class PlayerMinister(Player):
    def __init__(self, id, (x, y), image, world, color, image_chosen):
        Player.__init__(self, id, (x, y), image, world, color, image_chosen)

    def satisfy_rule(self, x, y):
        if self.x - x == 2 and self.y - y == 2:
            if self.world.AllPosition[x+1][y+1] is None:
                return 1
            else:
                return 0
        elif self.x - x == 2 and self.y - y == -2:
            if self.world.AllPosition[x+1][y-1] is None:
                return 1
            else:
                return 0
        elif self.x - x == -2 and self.y - y == 2:
            if self.world.AllPosition[x-1][y+1] is None:
                return 1
            else:
                return 0
        elif self.x - x == -2 and self.y - y == -2:
            if self.world.AllPosition[x-1][y-1] is None:
                return 1
            else:
                return 0
        elif self.x == x and self.y == y:
            return 1
        else:
            return 0

    def satisfy_rule_color(self, x, y):
        if self.color == "red":
            if y <= 4:
                return 1
            else:
                return 0
        elif self.color == "black":
            if y >= 5:
                return 1
            else:
                return 0


class PlayerBox(Player):
    def __init__(self, id, (x, y), image, world, color, image_chosen):
        Player.__init__(self, id, (x, y), image, world, color, image_chosen)

    def satisfy_rule(self, x, y):
        if (abs(y - self.y) == 1) or (abs(x - self.x) == 1):
            if not ((abs(y - self.y) == 1) and (abs(x - self.x) == 1)):
                return 1
        elif self.x == x and self.y == y:
            return 1
        else:
            return 0

    def satisfy_rule_color(self, x, y):
        if self.color == "red":
            if (x >= 3) and (x <= 5) and (y <= 2):
                return 1
            else:
                return 0
        elif self.color == "black":
            if (x >= 3) and (x <= 5) and (y >= 7):
                return 1
            else:
                return 0


class PlayerFire(Player):
    def __init__(self, id, (x, y), image, world, color, image_chosen):
        Player.__init__(self, id, (x, y), image, world, color, image_chosen)

    def satisfy_rule(self, x, y):
        if self.x == x:
            return Api.is_exist_l(y, self.y, x, self.world) == 0
        elif self.y == y:
            return Api.is_exist_r(x, self.x, y, self.world) == 0
        elif self.x == x and self.y == y:
            return 1
        else:
            return 0

    def eat(self, player_another):
        flag_eat = 0
        if not player_another.color == self.color:
            if self.x == player_another.x:
                if Api.is_exist_l(player_another.y, self.y, self.x, self.world) == 1:
                    flag_eat = 1
            elif self.y == player_another.y:
                if Api.is_exist_r(player_another.x, self.x, self.y, self.world) == 1:
                    flag_eat = 1
        if flag_eat:
            self.world.AllPosition[self.x][self.y] = None
            self.x = player_another.x
            self.y = player_another.y
            player_another.dispose()
            self.world.AllPosition[player_another.x][player_another.y] = self
            return 1
        else:
            return 0







