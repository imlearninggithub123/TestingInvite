list = []
while True:
      try:
            i = int(input())
            list.append(i)
      except ValueError:
            break
for k in range(len(list)):
      bigvalue = list[0]
      bigindex = 0
      count = 0
      for i in range(len(list)-k):
            if list[i] > bigvalue:
                  bigvalue = list[i]
                  bigindex = i
                  count += 1
      if count == len(list)-1-k:
            break
      list[bigindex], list[len(list)-1-k] = list[len(list)-1-k], list[bigindex]

print(list)