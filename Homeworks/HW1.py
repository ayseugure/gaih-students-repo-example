#get a number from user to determine the upper number for the range in the homework
#creating two lists including respectively odd numbers and even numbers from 0 to until this number
#HW 1
maxValue= int(input("Please enter number="))
oddList, evenList=[], []

for x in range(maxValue+1):
  if x%2==1:
    oddList.append(x)
  else:  
    evenList.append(x)

print("Odd Numbers : ",oddList)
print("Even Numbers: ",evenList)
even_copy=evenList.copy()
even_copy.extend(oddList)
even_copy.sort()
print("All Numbers: ",even_copy)
