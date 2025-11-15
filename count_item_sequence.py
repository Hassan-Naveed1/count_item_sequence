def count(sequence,item):

  count = 0
  for i in range(len(sequence)):
    if item == sequence[i]:
      count = count + 1

  
  
  
  return count 




print(count([1,2,1,1],1))