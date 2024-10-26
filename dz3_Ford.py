import time
import tracemalloc
from itertools import permutations

def solve_ford(): # Запуск замера времени и отслеживания памяти
    start_time = time.time()
    tracemalloc.start()
    
    D = 5 # Фиксируем D = 5, так как оно задано по условию
    for O in range(10):  # Перебираем возможные значения для O, исключая D
        if O == D: continue

        for N, A, L, G, E, R, B, T in permutations([i for i in range(10) if i not in {D, O}], 8): # Перебираем уникальные цифры для остальных букв N, A, L, G, E, R, B, T
            DONALD = D * 100000 + O * 10000 + N * 1000 + A * 100 + L * 10 + D
            GERALD = G * 100000 + E * 10000 + R * 1000 + A * 100 + L * 10 + D
            ROBERT = R * 100000 + O * 10000 + B * 1000 + E * 100 + R * 10 + T

            if DONALD + GERALD == ROBERT: # Проверяем, выполняется ли уравнение
                print(f"Решение: DONALD = {DONALD}, GERALD = {GERALD}, ROBERT = {ROBERT}")
                print(f"D={D}, O={O}, N={N}, A={A}, L={L}, G={G}, E={E}, R={R}, B={B}, T={T}")
                
                current, peak = tracemalloc.get_traced_memory()  # Останавливаем измерение памяти
                tracemalloc.stop()
                
                print(f"Время выполнения: {time.time() - start_time:.2f} секунд") # Выводим время выполнения и объем памяти
                print(f"Текущий объем памяти: {current / (1024 * 1024):.2f} МБ; Пиковый объем памяти: {peak / (1024 * 1024):.2f} МБ")
                return # Остановка системы после нахождения реш-я
    
    print("Решение не найдено")

solve_ford()
