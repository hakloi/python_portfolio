# constatnt time - It means the time taken will stay the same, regardless of how 
# big the hash table is.

import os
from time import sleep
import uuid

# code begins
clear = lambda: os.system('cls')
clear()


def get_page(url):
    if cache.get(url):
        return cache[url] 
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

# def get_data_from_server():
    

def user_search():
    user = input("Search Engine: ")
    i = 0;
    url = uuid.uuid4()
    while (i < 3):
        print(". . .")
        sleep(0.5)
        i+=1
    print("There is your page!")
    my_list = [user, url]
    return {"user": user, "url": url}

cache = {}

my_list = user_search()

cache.update(my_list)
print(cache)

