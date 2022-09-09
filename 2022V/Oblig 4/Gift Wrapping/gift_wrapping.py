""" !!! Oppgave skrevet sammen med Konrad Simsø og Jørgen Norås !!! """

from math import sqrt


def getConvexHull(points_input):
    points = []
    for i in points_input:
        if i not in points:
            points.append(i)

    polygon = []
    p0 = min(points)
    points_copy = points.copy()
    points_copy.pop(points_copy.index(p0))

    polygon.append(p0)

    if len(points) < 2:
        return [p0, p0]
    elif len(points) < 3:
        return [points[0], points[1], points[0]]

    x1, y1 = points_copy[0][0], points_copy[0][1]
    points_copy.pop(points_copy.index([x1, y1]))

    while True:
        while len(points_copy) > 0:
            for x2, y2 in points_copy:
                res = calculate_side(p0[0], p0[1], x1, y1, x2, y2)

                if res == 0:  # =0 på linje
                    if check_length(p0[0], p0[1], x1, y1) <= check_length(p0[0], p0[1], x2, y2):
                        x1, y1 = x2, y2
                        points_copy.pop(points_copy.index(x2, y2))
                elif res < 0:  # til høyre
                    x1, y1, = (
                        x2,
                        y2,
                    )
                    points_copy.pop(points_copy.index([x2, y2]))
                else:  # større enn null
                    points_copy.pop(points_copy.index([x2, y2]))

        p0 = [x1, y1]
        if polygon[0] == p0:
            return polygon
        polygon.append(p0)
        points_copy = points.copy()
        points_copy.pop(points_copy.index(p0))
        x1, y1 = points_copy[0][0], points_copy[0][1]
        points_copy.pop(points_copy.index([x1, y1]))


def calculate_side(y0, x0, y1, x1, y2, x2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)


def check_length(x1, y1, x2, y2):
    print(x1, y1, x2, y2)
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def main():
    data = [[1, 2.4], [2.5, 2], [1.5, 34.5], [5.5, 6], [6, 2.4], [5.5, 9]]
    fasit = [[2.5, 2.0], [6.0, 2.4], [5.5, 9.0], [1.5, 34.5], [1.0, 2.4]]

    trial = getConvexHull(data)

    print(fasit)
    print(trial)


if __name__ == "__main__":
    main()
