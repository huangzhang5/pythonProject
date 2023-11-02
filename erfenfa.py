# # def equation(x):
# #     return x**3 - 2*x - 5
# #
# # def binary_search(a, b, error):
# #     while abs(b - a) > error:
# #         mid = (a + b) / 2
# #         if equation(mid) == 0:
# #             return mid
# #         elif equation(a) * equation(mid) < 0:
# #             b = mid
# #         else:
# #             a = mid
# #     return (a + b) / 2
# #
# # # 设置初始区间和误差
# # a = 2
# # b = 3
# # error = 0.5 * 10**(-3)
# #
# # # 调用二分法求解根
# # root = binary_search(a, b, error)
# #
# # print("方程的根为:", root)
# # #
# import math
#
# def f(x):
#     return x**3 + 6*x**2 - 8
#
# def phi_1(x):
#     return x**3 + 6*x**2 + x - 8
#
# def phi_2(x):
#     return math.sqrt(8 / (x + 6))
#
# def phi_3(x):
#     return math.sqrt((8 - x**3) / 6)
#
# def simple_iteration(phi, x0, epsilon=1e-6, max_iterations=100):
#     x = x0
#     iterations = 0
#     while abs(f(x)) > epsilon and iterations < max_iterations:
#         x = phi(x)
#         iterations += 1
#     return x, iterations
#
# # 使用迭代函数 phi_1 进行计算
# root_1, iterations_1 = simple_iteration(phi_1, 1)
# print("Root using phi_1:", root_1)
# print("Iterations using phi_1:", iterations_1)
#
# # 使用迭代函数 phi_2 进行计算
# root_2, iterations_2 = simple_iteration(phi_2, 1)
# print("Root using phi_2:", root_2)
# print("Iterations using phi_2:", iterations_2)
#
# # 使用迭代函数 phi_3 进行计算
# root_3, iterations_3 = simple_iteration(phi_3, 1)
# print("Root using phi_3:", root_3)
# print("Iterations using phi_3:", iterations_3)


import math


def f(x):
    return math.cos(x) - x * math.exp(x)


def f_prime(x):
    return -math.sin(x) - (x + 1) * math.exp(x)


def newton_method(x0, epsilon):
    x = x0

    while True:
        fx = f(x)
        fpx = f_prime(x)

        x_next = x - fx / fpx

        if abs(x_next - x) < epsilon:
            break

        x = x_next

    return x


x0 = 0
epsilon = 1e-6

root = newton_method(x0, epsilon)
print("方程的最小正根为:", root)

