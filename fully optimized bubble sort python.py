list = []
while True:
      try:
            i = int(input('Enter sth: '))
            list.append(i)
      except ValueError:
            break
#From here we can optimize the algorithm by 2 ways: 1. Letting the inner loop stop at (len(list) - k)th position ; 2. Stop the outer loop immediately if there is no swap
for k in range(len(list)):
      swap = 0
      for i in range(len(list)-k-1):
            if list[i] > list[i+1]:
                  a = list[i]
                  b = list[i+1]
                  list[i+1] = a
                  list[i] = b
                  swap = 1
            if swap == 0:
                  break
print(list)