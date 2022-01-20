## How to calculate power of number using recursion ?

def power(base , exp):
  #for unintentional cases
  assert exp>=0 and int(exp) == exp ,"Exponent should be positive integer only "
  # exp=0 and 1 for stopping criteria and base condition
  if exp==0:
    return 1
  elif exp ==1:
    return base 
   # main logic for power calculation 
  else:
    return base * power(base , exp-1)
    
