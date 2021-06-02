def Interpretor(code, entrees = None):
    if entrees != None :
            entrees = entrees.split(" ")
            for input in entrees:
                input = int(input)
    code = [char for char in code]
    i = 0
    array = [i]
    l = 0
    while len(code)>i:
        print(i,array)
        print(code[i])
        if code[i] == '-' :
            array[l] = array[l] - 1
        if code[i] == '+' :
            array[l] = array[l] + 1
        if code[i] == '[' :
            limit = code.index(']')
            codeInIteration = []
            h = i + 1
            while h < limit :
                codeInIteration.append(code[h])
                h = h + 1
            print(codeInIteration)
            e = 0
            while array[l] != 0 :
                if codeInIteration[e] == '-' :
                    array[l] = array[l] - 1
                if codeInIteration[e] == '+' :
                    array[l] = array[l] + 1
                if codeInIteration[e] == '<' :
                    l = l - 1
                if codeInIteration[e] == '>' :
                    l = l + 1
                e = e + 1
                if  e == len(codeInIteration)  :
                    e = 0
            i = i + (limit - (i))
            print(str(i) + '+' + '(' + str(limit) + '+' +  str(h) + ')')
        if code[i] == '<' :
            l = l - 1
        if code[i] == '>' :
            l = l + 1
        if code[i] == ',' :
            array[l] = entrees[i]
            pop(i)
        if code[i] == '.' :
            print('int -> {} char/ASCII -> {}'.format(array[l],chr(array[l])))
        i = i + 1
Interpretor("+++[-].")
