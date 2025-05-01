import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

def inside_integral(f,x,y):
    return y <= f(x)

def monte_carlo_simulation(f, a, b, num_experiments):
    
    points = [(random.uniform(a,b), random.uniform(0,f(b))) for _ in range(num_experiments)]

    inside_points = [point for point in points if inside_integral(f, point[0], point[1])]

    area = (b - a) * f(b) * len(inside_points) / num_experiments
    return area 

result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)
print("Приблизний результат: ", monte_carlo_simulation(f,a,b,5000))

samples = [100, 1000, 10000, 100000, 1000000, 10000000]

for num_experiments in samples:
    print(f"Приблизний результат для {num_experiments} експериментів: ", monte_carlo_simulation(f,a,b,num_experiments))