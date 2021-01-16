import operator

expression=["+","*", "5","2","10"]
ops = {"+": operator.add, "-": operator.sub,"*":operator.mul, "/":operator.truediv}

def preflix(expressions):

    operator_1 = []
    list_of_num = []

    for element in expressions:
        print(element)
        if(element=="+"):
            #operator_1 == "+"
            operator_1.append("+")
        elif(element=="-"):
            #operator_1  == "-"
            operator_1.append("-")
        elif (element == "*"):
            operator_1.append("*")
            #operator_1  == "*"
        elif (element == "/"):
            #operator_1  == "/"
            operator_1.append("/")
        else:
            list_of_num.append(int(element))

    list_of_num = sorted(list_of_num)
    operator_1 = sorted(operator_1)
    print(operator_1)
    print(list_of_num)
    print(len(list_of_num))

    if(len(list_of_num)==len(operator_1)+1 & len(list_of_num)==2):
        return ops[operator_1[len(operator_1) - 1]](list_of_num[len(list_of_num) - 1],
                                                    list_of_num[len(list_of_num) - 2])
    elif(len(list_of_num)==len(operator_1)+1 & len(list_of_num)==3):
        first_num = ops[operator_1[len(operator_1) - 2]](list_of_num[len(list_of_num) - 3], list_of_num[len(list_of_num) - 2])

        return ops[operator_1[len(operator_1)-1]](first_num, list_of_num[len(list_of_num) - 1] )
    else:
        return


print(preflix(expression))