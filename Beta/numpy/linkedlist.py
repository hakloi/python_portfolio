# class Node:
#     def __init__(self, data):
#         self.data = data #значение узла (число, строка)
#         self.next = None #ссылка на следующий узел в списке
        
# # node = Node(5)  Узел с данными 5, next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None  #начальный узел (голова списка)

#     def append(self, data):
#         new_node = Node(data) #создаём новый узел с переданными данными
        
#         #если список пуст (head = None)
#         if not self.head: 
#             self.head = new_node #то новый узел становится головой списка
#             return
        
#         # если список не пуст:
#         current = self.head  #начинаем с головы списка
#         while current.next:  #проходим по узлам до последнего
#             current = current.next  #переходим к следующему узлу
#         current.next = new_node  #присоединяем новый узел к последнему узлу

#     def display(self):
#         elements = [] #создаем лист для фиксации переменных
#         current = self.head #начинаем с головы
#         while current: #пока не достигнем None продолжаем...
#             elements.append(current.data) #...добавлять элементы
#             current = current.next # обновление переменной, чтобы двигаться 
#         print(elements) #печатаем полученный результат

# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# # ll.display()  

# def isPalindrome(s):
    # new = ""
    # for ch in s.lower():
    #     if ch.isalpha():
    #         new += ch
     
    # if new == new[::-1]:
    #     return True
    # else:
    #     return False

#     filtered = [ch.lower() for ch in s if ch.isalnum()]

#     return filtered == filtered[::-1]
        
        
        
# s = "A man, a plan, a canal: Panama"
# print(isPalindrome(s))

# import numpy as np


# def make_board(n):
#     a = np.zeros((n, n), dtype="int8")
#     a[0::2, 0::2] = 1 
#     a[1::2, 1::2] = 1
#     return a


# print(make_board(4))

# [[1 0 1 0]
#  [0 1 0 1]
#  [1 0 1 0]
#  [0 1 0 1]]

# import numpy as np

# def snake(w, h, direction='H'):
#     a = np.arange(1, (w * h) + 1, dtype="int16")
#     if direction == 'V':
#         a = a.reshape((w, h)).T
#         a[:, 1::2] = a[::-1, 1::2]
#         return a
    
#     if direction == 'H':
#         a = a.reshape((h, w))
#         a[1::2] = a[1::2, ::-1]

#     return a


# # print(snake(5, 3))
# print(snake(5, 3, direction='V'))

# [[ 1  2  3  4  5]
#  [10  9  8  7  6]
#  [11 12 13 14 15]]

# [[ 1  6  7 12 13]
#  [ 2  5  8 11 14]
#  [ 3  4  9 10 15]]