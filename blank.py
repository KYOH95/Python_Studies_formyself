

def value_list(list_1):
    result = list_1[0]
    result_list_value = list_2[0]

    for x in list_1:
        if x < result_list_value:
            result = x
    
    return result_list_value

list_1 = [1,55,23,2]
list_2 = [4,24,78,6,21]

print(value_list(list_1))
print(value_list(list_2))