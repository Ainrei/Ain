import time 
import tracemalloc
from multiprocessing import Pool #параллельные вычисления на нескольких процессорах


def proc_comb(d, o, g, c, a, t):  
    x1 = 100 * d + 10 * o + g  
    x2 = 100 * c + 10 * a + t  
    x3 = x1 + x2  
    return (x1, x2, x3) 

def generate_comb():  # Создает все возможные комбинации из шести цифр, каждая из которых может принимать значения от 1 до 3.
    for d in [1,2,3]:
        for o in [1,2,3]:
            for g in [1,2,3]:
                for c in [1,2,3]:
                    for a in [1,2,3]:
                        for t in [1,2,3]:
                            yield (d, o, g, c, a, t) # Возвращает по одной комбинации за раз при каждой итерации, что снижает потребление памяти, так как в памяти хранится только текущая комбинация

def main():
    # отслеживание памяти
    tracemalloc.start()

    # начало выполнения
    start_time = time.time()

    #2 процессора
    with Pool(processes=2) as pool:
        
        results = pool.starmap(proc_comb, generate_comb())

    # окончание выполнения
    end_time = time.time()
  
    #V памяти+пиковое значение
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
  
    for result in results:
        print(f'x1: {result[0]}, x2: {result[1]}, x3: {result[2]}')

    print(f"Время выполнения: {end_time - start_time:.2f} сек")
    print(f"Использованный объем памяти: {current / (1024 * 1024):.2f} МБ; Пиковое значение объема памяти: {peak / (1024 * 1024):.2f} МБ")
main()
