class Line:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def is_point_satisfy(self, x, y):
        """Проверка: принадлежит ли точка полуплоскости Ax+By+C <= 0"""
        return self.A * x + self.B * y + self.C <= 1e-9  # небольшой допуск


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def intersect(line1, line2):
    """
    Пересечение двух прямых:
        A1*x + B1*y + C1 = 0
        A2*x + B2*y + C2 = 0
    """
    A1, B1, C1 = line1.A, line1.B, line1.C
    A2, B2, C2 = line2.A, line2.B, line2.C

    det = A1 * B2 - A2 * B1
    if abs(det) < 1e-9:
        return None  # прямые параллельны или совпадают

    x = (B1 * C2 - B2 * C1) / det
    y = (C1 * A2 - C2 * A1) / det
    return Point(x, y)


def main():
    lines = []
    print("Введите коэффициенты 8 прямых (A B C):")
    for i in range(8):
        A, B, C = map(float, input().split())
        lines.append(Line(A, B, C))

    feasible_points = []

    # пересечение каждой пары
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            p = intersect(lines[i], lines[j])
            if p is None:
                continue

            # проверяем, удовлетворяет ли точка всем неравенствам
            if all(line.is_point_satisfy(p.x, p.y) for line in lines):
                feasible_points.append(p)

    print("\nПодходящие точки пересечений (внутри области):")
    for p in feasible_points:
        print(f"({p.x:.3f}, {p.y:.3f})")


if __name__ == "__main__":
    main()
