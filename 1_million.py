message = []
with open('reviews.txt','r',encoding='utf-8') as f :
    for i in f:
        message.append(i)

count_number = {}
for i in message:
    i = i.split(' ')
    for j in i:
        if j not in count_number:
            count_number[j] = 1
        else:
            count_number[j] += 1

while True:
    word = input('請輸入您要查詢的字: ')
    if word not in count_number:
        print('沒有{}這個字喔'.format(word))
    elif word == 'q':
        print('感謝使用!')
        break
    else:
        print('{}出現過的次數為{}次'.format(word,count_number[word]))


with open('output.txt','w',encoding='utf-8') as f :
    for i in count_number:
        f.write(i + ',' + str(count_number[i]) + '\n')

with open('output.csv','w',encoding='utf-8') as f :
    for i in count_number:
        f.write(i + ',' + str(count_number[i]) + '\n')

print('存取完畢')



