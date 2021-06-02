def BrainF(code, entrees = None):
    code = str(code)
    if entrees != None : #make a list of integers with the inputs
        entrees = str(entrees)
        entrees = entrees.split(" ")
        for input in entrees:
            input = int(input)
    code = [char for char in code] #make a list of char with the input brainfuck code
    result = [] #the full result in ASCII
    i = 0 #number of iterations to read your code
    array = [i]# the array you're 'writing in'
    l = 0#the memory pointer index in array
    g = 0#on which iteration we are in mean on which '[]'
    while len(code)>i:
        print(i,array)
        print(code[i])
        if code[i] == '-' :
            array[l] = array[l] - 1
        if code[i] == '+' :
            array[l] = array[l] + 1
        if code[i] == '[' :
            limitsOfIterationList = [i for i,x in enumerate(code) if x==']']#index of the ']' in your code to know where to stop the iteration
            print('limitList',limitsOfIterationList)
            limitOfIteration= limitsOfIterationList[g]
            codeInIteration = []
            h = i + 1
            while h < limitOfIteration:
                codeInIteration.append(code[h])
                h = h + 1
            print(codeInIteration)
            lbis = l#to keep an eye on the original postion of the pointer to know when it's equal to 0
            e = 0
            while array[lbis] != 0 :
                if codeInIteration[e] == '-' :
                    array[l] = array[l] - 1
                if codeInIteration[e] == '+' :
                    array[l] = array[l] + 1
                if codeInIteration[e] == '<' :
                    l = l - 1
                if codeInIteration[e] == '>' :
                    l =l + 1
                e = e + 1
                if  e == len(codeInIteration)  :
                    e = 0
            i = i + (limitOfIteration-i)
            g = g + 1
        if code[i] == '<' :
            l = l - 1
        if code[i] == '>' :
            if (len(array)-1) < (l+1) :
                array.append(0)#we've to had a 0 to not be out of range 
                l = l + 1
            else : l = l + 1
        if code[i] == ',' :
            array[l] = entrees[i]
            pop(i)
        if code[i] == '.' :
            print('int -> {} char/ASCII -> {}'.format(array[l],chr(array[l])))
            result.append(chr(array[l]))
        i = i + 1
    for char in result :
        print(char,end ='')
