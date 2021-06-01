def Interpretor(code, entrees = None):
    entrees = [float for float in entrees]
    code = [char for char in code]
    iteration = False
    array = [0]
    l = 0
    while len(code)>0:
        if code[0] == '-' :
            array[l] = array[l] - 1
        if code[0] == '+' :
            array[l] = array[l] + 1
        if code[0] == '[' :
            iteration = True #get all the things in the [] and do the while thing
        #if code[0] == ']' :
        #    iteration = False
        if code[0] == '<' :
            l = l - 1
        if code[0] == '>' :
            l = l + 1
        if code[0] == ',' :
            array[l] = entrees[0]
            pop(0)
        if code[0] == '.' :
            print(array[l])
