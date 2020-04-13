'''
Реалізувати програму, в якій кожен з алгоритмів сортування оформити як окрему
функцію. Проілюструвати механізм використання параметрів різних типів. Забезпечити
підрахунок числа необхідних порівнянь, числа обмінів і часу роботи кожної функції,
сформувавши функції оцінки ефективності методів сортування. Підготувати єдині для
всіх алгоритмів тестові вихідні дані:
 • згенерована послідовність псевдовипадкових чисел, достатня для оцінки
 швидкості роботи алгоритму сортування (близько 100000 цілих чисел);
 • вихідна послідовність псевдовипадкових чисел, відсортована будь-яким методом
 в порядку зростання;
 • вихідна послідовність псевдовипадкових чисел, відсортована будь-яким методом
 в порядку за спаданням;
 • забезпечити програмну можливість вибору введення вихідних даних з клавіатури
 до 30 вихідних чисел.
 Для програми привести лістинг з результати роботи:
 • вихідний масив (вивести на екран для випадку введення вихідних даних з
 клавіатури);
 • відсортований масив (для випадку введення вихідних даних з клавіатури один
 екземпляр відсортованого масиву вивести на екран);
 • показники функції оцінки ефективності методів сортування (вивести на екран).
 Виконати сортування масиву цілих чисел Ai,i = 0,N −1 в порядку зростання / за спаданням елементів.

Найпростіші алгоритми сортування:
 • сортування бульбашкою (bubble sort);
 • сортування вибором (selection sort);
 • сортування вставками (insertion sort).
'''

from random import randint
from time import time


def my_int_input(text_def):  # функція вводу цілих чисел
    while True:
        try:
            input_num_def = int(input(text_def))
            break
        except ValueError:
            print('only digit')
    return input_num_def


def bubble_sort(list_def, in_order_of_growth_def=True):  # бульбашкове сортування
    number_of_comparisons_def = 0  # кількість порівнянь
    number_of_exchanges_def = 0  # кількість обмінів
    for i_def in range(len(list_def) - 1):  # зовнішній цикл
        for j_def in range(len(list_def) - i_def - 1):  # внутрішній цикл
            if list_def[j_def] > list_def[j_def + 1]:  # якщо настуступний елемент менше, то елементи міняються
                list_def[j_def + 1], list_def[j_def] = list_def[j_def], list_def[j_def + 1]
                number_of_exchanges_def += 2
            number_of_comparisons_def += 1
    if not in_order_of_growth_def:  # перевірка чи сортувати за спаданням
        list_def.reverse()  # якщо так, то просто перевертає список, бо мені не хотілось вставляти ще 3 функції
    number_of_comparisons_def += 1
    return number_of_comparisons_def, number_of_exchanges_def, list_def


def selection_sort(list_def, in_order_of_growth_def=True):  # сортування вибором
    number_of_comparisons_def = 0  # кількість порівнянь
    number_of_exchanges_def = 0  # кількість обмінів
    for i_def in range(len(list_def)):  # зовнішній цикл
        index_of_minimum_def = i_def  # індекс мінімального елементу
        for j_def in range(i_def + 1, len(list_def)):  # внутрішній цикл для пошуку мінімального елементу
            if list_def[j_def] < list_def[index_of_minimum_def]:
                index_of_minimum_def = j_def
            number_of_comparisons_def += 1
        list_def[i_def], list_def[index_of_minimum_def] = list_def[index_of_minimum_def], list_def[
            i_def]  # обмін елементів. Мінімальний залишається зліва
        number_of_exchanges_def += 2
    if not in_order_of_growth_def:  # перевірка чи сортувати за спаданням
        list_def.reverse()  # якщо так, то просто перевертає список, бо мені не хотілось вставляти ще 3 функції
    number_of_comparisons_def += 1
    return number_of_comparisons_def, number_of_exchanges_def, list_def


def insertion_sort(list_def, in_order_of_growth_def=True):  # сортування вставками
    number_of_comparisons_def = 0  # кількість порівнянь
    number_of_exchanges_def = 0  # кількість обмінів
    for i_def in range(len(list_def)):  # зовнішній цикл
        key_def = list_def[i_def]  # буфер, тимчасова комірка для зберігання елементу
        j_def = i_def
        while (list_def[j_def - 1] > key_def) and (j_def > 0):  # внутрішній цикл для пошуку місця, куди вставити
            # елемент та зсуву елементів, що поруч того місця
            list_def[j_def] = list_def[j_def - 1]
            j_def = j_def - 1
            number_of_comparisons_def += 2
            number_of_exchanges_def += 1
        number_of_comparisons_def += 2
        list_def[j_def] = key_def  # призначення комірці значення від буферу
        number_of_exchanges_def += 2
    if not in_order_of_growth_def:  # перевірка чи сортувати за спаданням
        list_def.reverse()  # якщо так, то просто перевертає список, бо мені не хотілось вставляти ще 3 функції
    number_of_comparisons_def += 1
    return number_of_comparisons_def, number_of_exchanges_def, list_def


quesh = input("Введіть \"yes\", якщо хочете ввести значення масиву з клавіатури: ")
if "yes" == quesh:
    while True:  # ручне введення списку
        stop = my_int_input("Введіть кількість значень (до 30): ")
        if stop >= 30:
            print("Забагато значень!")
            continue
        break
    a = []
    for i in range(stop):
        a.append(my_int_input(f"Введіть знечення під індексом {i}: "))
    print(f"Список: {a}")
else:  # генерація рандмного списку
    a = []
    dovgina = 1000  # довжина рандомного списку
    for i in range(dovgina):
        a.append(randint(1, 99))

print("\n• сортування бульбашкою (bubble sort) в порядку зростання:")
tic = time()  # запам'ятамо час старту
number_of_comparisons, number_of_exchanges, sorted_a = bubble_sort(a.copy(), in_order_of_growth_def=True)
toc = time()  # запам'ятамо час фінішу
# print(f"Відсортований список: {sorted_a}")
print(f"Число порівнянь: {number_of_comparisons}")
print(f"Число обмінів: {number_of_exchanges}")
print(f"Час роботи функції: {toc - tic}")

print("\n• сортування бульбашкою (bubble sort) за спаданням елементів:")
tic = time()  # запам'ятамо час старту
number_of_comparisons, number_of_exchanges, sorted_a = bubble_sort(a.copy(), in_order_of_growth_def=False)
toc = time()  # запам'ятамо час фінішу
# print(f"Відсортований список: {sorted_a}")
print(f"Число порівнянь: {number_of_comparisons}")
print(f"Число обмінів: {number_of_exchanges}")
print(f"Час роботи функції: {toc - tic}")

print("\n• сортування вибором (selection sort) в порядку зростання:")
tic = time()  # запам'ятамо час старту
number_of_comparisons, number_of_exchanges, sorted_a = selection_sort(a.copy())
toc = time()  # запам'ятамо час фінішу
# print(f"Відсортований список: {sorted_a}")
print(f"Число порівнянь: {number_of_comparisons}")
print(f"Число обмінів: {number_of_exchanges}")
print(f"Час роботи функції: {toc - tic}")

print("\n• сортування вибором (selection sort) за спаданням елементів:")
tic = time()  # запам'ятамо час старту
number_of_comparisons, number_of_exchanges, sorted_a = selection_sort(a.copy(), in_order_of_growth_def=False)
toc = time()  # запам'ятамо час фінішу
# print(f"Відсортований список: {sorted_a}")
print(f"Число порівнянь: {number_of_comparisons}")
print(f"Число обмінів: {number_of_exchanges}")
print(f"Час роботи функції: {toc - tic}")

print("\n• сортування вставками (insertion sort) в порядку зростання:")
tic = time()  # запам'ятамо час старту
number_of_comparisons, number_of_exchanges, sorted_a = insertion_sort(a.copy())
toc = time()  # запам'ятамо час фінішу
# print(f"Відсортований список: {sorted_a}")
print(f"Число порівнянь: {number_of_comparisons}")
print(f"Число обмінів: {number_of_exchanges}")
print(f"Час роботи функції: {toc - tic}")

print("\n• сортування вставками (insertion sort) за спаданням елементів:")
tic = time()  # запам'ятамо час старту
number_of_comparisons, number_of_exchanges, sorted_a = insertion_sort(a.copy(), in_order_of_growth_def=False)
toc = time()  # запам'ятамо час фінішу
# print(f"Відсортований список: {sorted_a}")
print(f"Число порівнянь: {number_of_comparisons}")
print(f"Число обмінів: {number_of_exchanges}")
print(f"Час роботи функції: {toc - tic}")
if "yes" == quesh:
    print(f"Відсортований список: {sorted_a}")
