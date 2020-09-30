from utils import getmaxlen, getspaces, validate


def arithmetic_arranger(problems, showresults=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    # split of every problem with the length of longest digit
    oplist = [(x[0], x[1], x[2], getmaxlen(x[0], x[2]))
              for x in (x.split() for x in problems)]
    
    error = validate(oplist)
    if error:
        return error

    result = ''
    separator = '    '

    # adding 1st numbers of every operation to result
    i = 0
    for op in oplist:
        result += '{}{}'.format(getspaces(op[3] - len(op[0]) + 2), op[0])
        if i < len(oplist) - 1:
            result += separator
        else:
            result += '\n'
        i += 1

    # adding symbol and 2nd numbers of every operation to result
    i = 0
    for op in oplist:
        result += '{} {}{}'.format(op[1], getspaces(op[3] - len(op[2])), op[2])
        if i < len(oplist) - 1:
            result += separator
        else:
            result += '\n'
        i += 1

    # adding dashes to result
    i = 0
    for op in oplist:
        for x in range(op[3] + 2):
            result += '-'
        if i < len(oplist) - 1:
            result += separator
        i += 1

    if showresults:
        # adding results to result
        result += '\n'
        i = 0
        for op in oplist:
            opresult = str(eval(problems[i]))
            result += '{}{}'.format(getspaces(op[3] - len(opresult) + 2), opresult)
            if i < len(oplist) - 1:
                result += separator
            i += 1

    return result
