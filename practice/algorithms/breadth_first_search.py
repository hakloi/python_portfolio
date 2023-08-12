from collections import deque
import os 

# code begins
clear = lambda: os.system('cls')
clear()


def person_is_seller(name): 
    return name[-1] == 's'

graph = {}
graph["violett"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = ["miles"]
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  

    while search_queue:
        person = search_queue.popleft()

        if not person in searched: 
            if person_is_seller(person):
                print("It's him -", person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person) 

    return False

search('violett')