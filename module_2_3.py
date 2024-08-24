my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
new_list = []
number = 0
while  number < len(my_list):
    if my_list[number] > 0 :
        new_list.append(my_list[number])
        number += 1
    elif my_list[number] == 0:
       number +=1
    elif my_list[number] <= -1 :
        break

print(new_list)
