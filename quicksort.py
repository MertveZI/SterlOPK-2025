# Задача «Быстрая сортировка» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г

def quick_sort(array):
    """ Получает на фход несортированный массив. Сортирует его по алогритму Хоара. """

    length = len(array)

    # Проверяем, что длина массива больше 1
    if length > 1: 

        # Выбираем опорный элемент(здесь - средний)
        base = array[length // 2]
        
        # Разделяем массив на три части:
        left = [x for x in array if x < base] # 1. Элементы меньше опорного
        middle = [x for x in array if x == base] # 2. Элементы равные опорному
        right = [x for x in array if x > base] # 3. Элементы больше опорного
        
        # Рекурсивно применяем quicksort к левой и правой частям
        array = quick_sort(left) + middle + quick_sort(right)

# Пример использования
if __name__ == "__main__": # Проверка на импортированность
    # Приветственное сообщение и снятие данных
    array = list(map(int, input('\n Программа сортировки слиянием\
                                \n Введите массив через запятую: ').replace(' ', '').split(',')))
    quick_sort(array)
    print('Отсортированнный массив: ', array) # Вывод ответа
else:
    print('Скрипт импортирован!') # Вывод сообщения об импортированности скрипта