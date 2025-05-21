l = [3,2,1,-3,2,15]

def s(local: list) -> list:
    for j in range(len(local)):
        for i in range(1, len(local)):
            if local[i] < local[i-1]:
                temp = local[i - 1]
                local[i - 1] = local[i]
                local[i] = temp
    return local

print(s(l))
