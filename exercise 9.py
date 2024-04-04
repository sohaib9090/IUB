def create_new_list(list1, list2):
    new_list = []
    # Adding odd numbers from list1 to the new list
    for num in list1:
        if num % 2 != 0:
            new_list.append(num)
    # Adding even numbers from list2 to the new list
    for num in list2:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

# Testing
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

new_list = create_new_list(list1, list2)
print("New List:", new_list)
