import LibSort # наш модуль
import time # модуль для замера времени
import random
n = 10**4
Massiv = [random.randint(1,100000) for i in range(n)]
Massiv1 = Massiv[::]
Massiv2 = Massiv[::]
Massiv3 = Massiv[::]
Massiv4 = Massiv[::]
Start1 = time.time()
LibSort.insertion_sort(Massiv3)
Finish1 = time.time()
Res_msec = (Finish1 - Start1)*1000
print(Res_msec,'Сортировка вставками')
Start2 = time.time()
LibSort.selection_sort(Massiv2)
Finish2 = time.time()
Res_msec2 = (Finish2 - Start2)*1000
print(Res_msec2,'Сортировка выбором')
Start3 = time.time()
LibSort.bubble_sort(Massiv1)
Finish3 = time.time()
Res_msec3 = (Finish3 - Start3)*1000
print(Res_msec3,'Сортировка пузырьком')
Start3 = time.time()
LibSort.quick_sort(Massiv4)
Finish3 = time.time()
Res_msec3 = (Finish3 - Start3)*1000
print(Res_msec3,'Сортировка пузырьком')
