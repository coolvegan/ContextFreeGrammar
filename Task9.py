def palindromTest(text):
  lenStr = len(text)
  if(lenStr<2):
    return False
  stack = []
  odd = lenStr % 2 != 0
  for i in range(0,int(lenStr/2),1):
    stack.append(text[i])
  start=int(lenStr/2)
  for z in range(int(lenStr/2)+(1 if odd else 0),lenStr):
    if(text[z]!=stack.pop()):
      return False
  return True
print(palindromTest('aaabbaaa'))
