#returns the length of the longest digit
def getmaxlen(n1, n2):
    if len(n1) > len(n2):
      return len(n1)
    return len(n2)

#returns the amount of spaces asked for
def getspaces(n):
  result = ''
  i = 0
  while i < n:
    result += ' '
    i += 1
  return result

#returns error message if list is invalid
def validate(list):
  for op in list:
    if not op[0].isdigit() or not op[2].isdigit():
      return "Error: Numbers must only contain digits."
    if op[3] > 4:
      return "Error: Numbers cannot be more than four digits."
    if op[1] != '+' and op[1] != '-':
      return "Error: Operator must be '+' or '-'."
  return None