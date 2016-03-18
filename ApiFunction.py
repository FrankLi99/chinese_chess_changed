__author__ = 'lenovo'


class Api:
    @staticmethod
    def pix_to_position((pix_x, pix_y)):
        x = -1
        y = -1
        for i in range(9):
            if (pix_x <= (8 + 41 * i + 20 +20)) and (pix_x > (8 + 41 * i - 20+20)):
                x = i
                break
        for j in range(11):
            if (pix_y <= (7+41*j+20+20)) and (pix_y > (7+41*j-20+20)):
                y = j
                break
        return (x, y)

    @staticmethod
    def is_exist_r(x1, x2, y, world):
        count = 0
        if x1 < x2:
            for i in range(x1+1, x2):
                if world.AllPosition[i][y] is not None:
                    count = (count + 1)
            return count
        else:
            for i in range(x2+1, x1):
                if world.AllPosition[i][y] is not None:
                    count = (count + 1)
            return count

    @staticmethod
    def is_exist_l(y1, y2, x, world):
        count = 0
        if y1 < y2:
            for i in range(y1+1, y2):
                if world.AllPosition[x][i] is not None:
                    count = (count + 1)
            return count
        else:
            for i in range(y2+1, y1):
                if world.AllPosition[x][i] is not None:
                    count = (count + 1)
            return count

    @staticmethod
    def is_exist_p(x, y, world):
        if world.AllPosition[x][y] is None:
            return 0
        else:
            return 1



