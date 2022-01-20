def convert(s: str, numRows: int) -> str:
    # Guard Clause
    if numRows == 1:
        return s

    output = ""
    # jump size
    jump = 2 * numRows - 2
    # Loop for each row
    for i in range(0, numRows):
        # Loop for each character in the row
        for j in range(i, len(s), jump):
            output += s[j]
            if i != 0 and i != numRows - 1 and (j + jump - 2 * i) < len(s):
                output += s[j + jump - 2 * i]
    return output