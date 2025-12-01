# В классической погоне Том бежит за Джерри, поскольку Джерри съел любимую еду Тома.
# Джерри бежит со скоростью X метров в секунду, пока Том гонится за ним со скоростью
# Y метров в секунду. Начальное расстояние между ними S.Определите,
# сможет ли Том поймать Джерри. Если да, то за сколько секунд. 

import os

# code begins
clear = lambda: os.system('cls')
clear()

tom = int(input("Tom's speed (m/s): "))
jerry = int(input("Jerry's speed (m/s): "))
distance = int(input("Distance (m): "))

def result_of_race(pers1, pers2, distance):
    if pers1 > pers2:
        speed_closer = pers1 - pers2
        time_closer = distance/ speed_closer
        return print('Movement towards convergence. Tom will catch Jerry in ', time_closer, 'sec!')
    else:
        speed_farther = pers2 - pers1
        print('Movement towards divergence.')
        number = input('Write number of function:\n' +
                           '1) What is the distance between the persons in _ seconds?\n' + 
                           '2) In how many seconds will the distance between them be _ m?\n')
        match number:
            case "1":
                seconds = int(input("Seconds: "))
                print("In", seconds, "seconds there will be", speed_farther*seconds  ,"m between the persons.")
            case "2":
                dist = int(input("Distance: "))
                print("After", dist/speed_farther ,"seconds, there will be a distance of", dist, "m between the persons.")
            case _:
                print("Function not found")
    
result_of_race(tom, jerry, distance)