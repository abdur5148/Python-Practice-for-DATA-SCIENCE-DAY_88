def puzzle(head, leg):
    for i in range(head+1):
        j = head-i
        if 2*i+4*j == leg:
            return i, j


head = 35
leg = 94
Solved = puzzle(head, leg)
print(Solved)
