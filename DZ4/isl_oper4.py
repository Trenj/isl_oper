import numpy as np
from scipy.optimize import linprog

# --- Исходные данные ---
delta1, delta2 = 4, 5

# L1, L2, L3
# L1 = 2x1 + x2 - 3x3
# L2 = x1 + 3x2 - 2x3
# L3 = -x1 + 2x2 + 4x3

print("Исходные критерии:")
print("L1 = 2x1 +  x2 - 3x3")
print("L2 =  x1 + 3x2 - 2x3")
print("L3 = -x1 + 2x2 + 4x3")
print(f"Весовые коэффициенты: δ1={delta1}, δ2={delta2}")

# Комбинированная функция: F = δ1*L1 + δ2*L2 + L3
c = np.array([12, 21, -18])  # коэффициенты для F(x)

print("\nКомбинированная функция:")
print("F(x) = 12x1 + 21x2 - 18x3 -> max")

# --- Ограничения ---
# SciPy linprog решает задачу минимизации, поэтому F(x) -> max эквивалентно -F(x) -> min
c_linprog = -c

# Ограничения в форме A_ub * x <= b_ub
A_ub = [
    [-1, -3, -2],   # x1 + 3x2 + 2x3 >= 1  → -x1 -3x2 -2x3 <= -1
    [ 2, -1,  1],   # 2x1 - x2 + x3 <= 16
    [ 1,  2,  0],   # x1 + 2x2 <= 24
]
b_ub = [-1, 16, 24]

# Границы переменных
bounds = [(0, None), (0, None), (0, None)]

print("\nОграничения:")
print("1) x1 + 3x2 + 2x3 >= 1")
print("2) 2x1 - x2 + x3 <= 16")
print("3) x1 + 2x2 <= 24")
print("4) x1, x2, x3 >= 0")

# --- Решение задачи ---
result = linprog(c_linprog, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

print("\nРезультат оптимизации:")
if result.success:
    x1, x2, x3 = result.x
    print(f"Оптимальное решение: x1={x1:.4f}, x2={x2:.4f}, x3={x3:.4f}")
    print(f"Значение целевой функции F(x) = {-result.fun:.4f}")
else:
    print("Решение не найдено:", result.message)
