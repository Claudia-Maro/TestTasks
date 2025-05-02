answer = input("Введите числа через запятую:").strip()

if not answer:
    print("Вы ничего не ввели")
    exit()

numbers = []
for item in answer.split(','):
    item = item.strip()
    if not item:
        continue
    try:
        num = int(item)
        numbers.append(num)
    except ValueError:
        print(f"Ошибка:'{item}' не являеться целым числом, пропускаем")

if not numbers:
    print("Нет корректных чисел для обработки")
    exit()

# Ммксимум и минимум 
if numbers:
     print("Максимальное число:", max(numbers))
     print("Минимальное число:", min(numbers))

# Вывод чётных чисел
even_numbers = [num for num in numbers if num % 2 == 0]
print("Четные числа:", even_numbers)

# Функция сортировки вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

sorted_numbers = insertion_sort(numbers.copy())
print("Отсортированный список:", sorted_numbers) 