data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))  
		#如果要加上進度的話 
		#但是每一次print的速度很慢
		#所以我們每讀一千筆再回報一次
#print('There are',len(data), 'reviews in total')
#print(data[0]) #印出第一個選項，從0 開始

sum_len = 0
for i in data:
	sum_len += len(i)
print('Average review length is', sum_len/len(data))

new = []  #如果要去算有多少的留言少於一百個字元的方式
for i in data:
	if len(i) < 100:
		new.append(d)
print(len(new))

good = []  #如果要去算有多少的留言有good
for i in data:
	if 'good' in d:  #是非題的格式
		good.append(d)
print(len(good))


