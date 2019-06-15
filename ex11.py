a = 'bootcamp'
print("1-" + a[2]) 
print("2- " + a[-1])    
print("3- " + a[0 : 5])
print("4 -" + a[ : -2])
def odd_values_string(a):
  result = "" 
  for i in range(len(a)):
    if i % 2 == 0:
      result = result + a[i]
  return result
print("5- " + odd_values_string(a))

def odd_values_string(a):
  result = "" 
  for i in range(len(a)):
    if i % 2 == 1:
      result = result + a[i]
  return result
print("6- " + odd_values_string(a))
print("7- " + a[:: -1])
print("8- " + a[-2 :: -2])
print("9-" , len(a))