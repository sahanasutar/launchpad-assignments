def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list  
duplicate = [2, 4, 10, 20, 5, 2, 20, 4,33,92,4,5,81] 
print(Remove(duplicate))