# Bublle sort
def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1): # means the number of comparison is decreasing progressly
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list
 
def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j= i - 1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j = j-1
    return my_list

print(selection_sort([4,2,6,5,1,3]))
alist = [4, 3, 1, 2, 5]

print(bubble_sort(alist))
print(insertion_sort([4,2,6,5,1,3]))
        
        