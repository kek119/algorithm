import time
import pandas as pd
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

sizes = [10000, 50000, 100000, 200000, 300000, 400000, 500000]
results = []

best_times = []
worst_times = []
avg_times = []

for n in sizes:
    # Найкращий випадок (вже відсортований)
    best_arr = list(range(1, n + 1))
    start = time.time()
    insertion_sort(best_arr.copy())
    best_time = time.time() - start

    # Найгірший випадок (спадання)
    worst_arr = list(range(n, 0, -1))
    start = time.time()
    insertion_sort(worst_arr.copy())
    worst_time = time.time() - start

    # Середній випадок (рандом)
    avg_arr = [random.randint(1, n) for _ in range(n)]
    start = time.time()
    insertion_sort(avg_arr.copy())
    avg_time = time.time() - start

    results.append({
        "Розмір масиву": n,
        "Найкращий випадок (сек)": round(best_time, 6),
        "Найгірший випадок (сек)": round(worst_time, 6),
        "Середній випадок (сек)": round(avg_time, 6),
    })

    best_times.append(best_time)
    worst_times.append(worst_time)
    avg_times.append(avg_time)

# Вивід таблиці
df = pd.DataFrame(results)
print(df)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(sizes, best_times, 'go--', label='Найкращий випадок (O(n))')
plt.plot(sizes, avg_times, 'bo--', label='Середній випадок (~O(n²))')
plt.plot(sizes, worst_times, 'ro-', label='Найгірший випадок (O(n²))')

plt.title('Час виконання сортування методом вставок')
plt.xlabel('Розмір масиву')
plt.ylabel('Час виконання (секунди)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



