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
# ll.display()  

def isPalindrome(s):
    # new = ""
    # for ch in s.lower():
    #     if ch.isalpha():
    #         new += ch
     
    # if new == new[::-1]:
    #     return True
    # else:
    #     return False

    filtered = [ch.lower() for ch in s if ch.isalnum()]

    return filtered == filtered[::-1]
        
        
        
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))