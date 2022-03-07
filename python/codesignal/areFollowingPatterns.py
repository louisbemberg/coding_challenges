# my sol
def solution(strings, patterns):
    # Basic guard clauses
    if not strings or not patterns: return False
    if len(strings) != len(patterns): return False
    
    # Create maps for both patterns and strings
    dic1 = {}
    dic2 = {}
    
    # the lengths of strings and patterns are guaranteed to be the same thanks to guard clause
    for i, string in enumerate(strings):
        if string in dic1:
            dic1[string].append(i)
        else:
            dic1[string] = [i]
    
    for i, pattern in enumerate(patterns):
        if pattern in dic2:
            dic2[pattern].append(i)
        else:
            dic2[pattern] = [i]
    
    # if we don't have the same amount of unique patterns as amount of unique strings it must be false
    string_keys = dic1.keys()
    pattern_keys = dic2.keys()
    
    if len(string_keys) != len(pattern_keys): return False
    
    for string_key, pattern_key in zip(string_keys, pattern_keys):
        if len(dic1[string_key]) != len(dic2[pattern_key]): return False
        
        if sorted(dic1[string_key]) != sorted(dic2[pattern_key]): return False
    
    return True

# My refactored but still not optimal sol:

# Optimal sol:
def solution(strings, patterns):
    d = {}
    for i, j in zip(strings, patterns):
        if i in d and d[i] != j:
            return False
        d[i] = j
    return len(d) == len(set(d.values()))

        