def solution(crypt, solution):
    # convert solution to dictionary , and convert strings to int
    solution2 = {}
    for pair in solution:
        solution2[pair[0]] = pair[1]
    
    d1 = [solution2[x] for x in crypt[0]]
    d2 = [solution2[x] for x in crypt[1]]
    d3 = [solution2[x] for x in crypt[2]]
    
    if (d1[0] == '0' and len(d1) >= 2) or (d2[0] == '0' and len(d2) >= 2) or (d3[0] == '0' and len(d3) >= 2) :
        return False
    else:
        return int(''.join(d1)) + int(''.join(d2)) == int(''.join(d3))
    





sol = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]

solution(['TEN', 'TWO', 'ONE'], sol)

