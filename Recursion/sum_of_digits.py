def sum_of_digits(n):
  assert n>= 0 and int(n)==n, "Not applicable for negative and non integers"
  if n in [0,1]:
    return n
  else:
    return sum_of_digits(n//10) + n%10
  
  
print(sum_of_digits(18))
