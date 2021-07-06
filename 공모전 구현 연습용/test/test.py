answer = open('answer.txt', 'r')
answer_list = []
while True:
    line = answer.readline()
    answer_list.append(list(line.split(",")))
    if not line: 
        break
answer.close()
print(answer_list)