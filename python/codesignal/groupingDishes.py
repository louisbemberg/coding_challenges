## my solution

def solution(dishes):
    from collections import defaultdict
    dct = defaultdict(list)
    
    # creating a map of ingredient => dishes
    for dish in dishes:
        for ingredient in dish[1:]:
            dct[ingredient].append(dish[0])
            
    output = []
    
    for key, value in dct.items():
        # retain only ingredients that belong to more than one dish
        if len(value) >= 2:
            arr = [key]
            arr.extend(sorted(value))
            output.append(arr)
            
    return sorted(output)


## better solution

def solution(dishes):
    # create empty map
    dct = {}
    for dish in dishes:
        # get dish name AND remove it from the list so only ingredients left
        dish_name = dish.pop(0)
        # iterate over remaining ingredients
        for ingred in dish:
            # get logic that either adds to an existing array or creates one
            D[ingred] = D.get(ingred, []) + [dish_name]
    # comprehension to take care of all the steps at once
    return sorted([i] + sorted(v) for i, v in D.items() if len(v) > 1)