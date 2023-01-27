#打開reviews.txt
#讀取
#每1000筆印出留言的長度
#所有的留言長度
#留言的平均長度
#小於100的留言數
#有good的留言
#快寫法


data = []
#count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line) #把每一筆留言新增到data清單
		#count = count + 1
		#if count % 1000 == 0: #可以被1000整除，即每一千筆
			#print(len(data)) #每1000筆印出留言的長度
print(len(data)) #印出所有留言的長度
print(data[0])

#Ch.82
#查每個字出現的次數
#讓使用者輸入想查的字

wc = {} # word_count
for d in data:
	words = d.split() #預設值就是空白鍵，而且如果遇到連續空白鍵，不會計入
	for word in words:
		if word in wc:
			wc[word] += 1 # 在字典中增加新的值：wc['key'] = 'value'
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請輸入查詢的字：')
	if word == 'q':
		break
	if word in wc:
	print(wc[word])
	else:
		print('沒有這個字。')












'''
#求平均
sum = 0
for d in data:
	sum = sum + len(d)
print('留言的平均長度是',sum/len(data))



#小於100的留言數
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print (len(new))
print(new[0])
print(new[1])



#有good的留言
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'筆留言提到good。')
print(good[0]) #印出第一筆有good的留言



#「有good的留言」的快寫法
good = [d for d in data if 'good' in d]
print('一共有',len(good),'筆留言提到good。')
print(good[0]) #運算完要記得print才會有結果
#d: 運算 就是good.append(d)的d #d可以換成別的
#for d in: 變數
#data: 清單
#if 'good' in d: 條件
'''



'''
#快寫法2
bad = ['bad' in d for d in data]
print(bad[0])
#'bad' in d 也是一種運算
#通常運算只會放d，不會放其他
#快寫法比較少見
'''






