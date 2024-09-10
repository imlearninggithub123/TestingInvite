list = []
while True:
      try:
            i = int(input('Enter sth: '))
            list.append(i)
      except ValueError:
            break
for i in range(1,len(list)):
      k = 0
      while list[i-k-1] > list[i-k]:
            list[i-k-1],list[i-k] = list[i-k],list[i-k-1]
            k += 1
            if i-k == 0:
                  break
print(list)