from inp import day1

def setupdata(data):
    return data.split("\n")

def increasingcount(data):
    ic = 0
    for i in range(len(data)-1):
        if int(data[i]) < int(data[i+1]):
            ic += 1
    return ic


if __name__ == '__main__':
    print(increasingcount(setupdata(day1)))
        
