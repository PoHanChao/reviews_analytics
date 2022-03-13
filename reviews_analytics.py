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
print(len(data))
print(data[0]) #印出第一個選項，從0 開始
