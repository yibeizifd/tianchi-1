# -*- coding: utf-8 -*- 

import time
import gzip
import fileinput

# 提取出所有user_id
def func_user():
	user = []
	a = 0
	for line in gzip.open("../uid_iid.txt.gz"):
		# print a
		a = 0
		c = line.split(' ')[0]
		for i in range(len(user)):
			if (user[i]==c):
				a = 1
				break
		if(a==0):
			user.append(line.split(' ')[0])

	print len(user)
	file = open("user_feature.txt","w")
	for i in range(len(user)):
		file.write(user[i])
		file.write('\n')

# 基本特征统计
def func_feature_1(date):
	endtime=time.mktime(time.strptime('2014-'+date,'%Y-%m-%d-%H'))
	user_dict = {}
	user_item = {}
	user_category = {}
	user = []
	f = open("user_feature.txt","r")
	for i in range(10000):
		user.append(f.readline().strip())
	f.close()
	# a = [0 for x in range(0, len(user))] '''购买数'''
	# b = [0 for x in range(0, len(user))] '''购买种类数'''
	# c = [0 for x in range(0, len(user))] '''点击数'''
	# d = [0 for x in range(0, len(user))] '''点击种类数'''
	# e = [0 for x in range(0, len(user))] '''收藏数'''
	# f = [0 for x in range(0, len(user))] '''收藏种类数'''
	# g = [0 for x in range(0, len(user))] '''添加购物车数'''
	# h = [0 for x in range(0, len(user))] '''添加购物车种类数'''
	# i = [0 for x in range(0, len(user))] '''购买商品标识数'''
	# j = [0 for x in range(0, len(user))] '''点击商品标识数'''
	# k = [0 for x in range(0, len(user))] '''收藏商品标识数'''
	# l = [0 for x in range(0, len(user))] '''添加购物车商品标识数'''
	
	for i in range(len(user)):
		# print user[i]
		user_dict[user[i]]=[0 for x in range(0,8)] 
		# user_item[user[i]]=[[],[],[],[]] 
		# user_category[user[i]]=[[],[],[],[]] 

	for line in gzip.open("../uid_iid.txt.gz"):
		(uid, iid, ict) = line.strip().split("\t")[0].split(" ")
		action_category = []
		for action in line.strip().split("\t")[1].split(" "):
			# print action.split(",")[0]
			# print int(time.mktime(time.strptime('2014-'+action.split(",")[0],'%Y-%m-%d-%H')))
			if(time.mktime(time.strptime('2014-'+action.split(",")[0],'%Y-%m-%d-%H'))<endtime):
				action_category.append(action.split(",")[1])
		# print action_category
		a = [0 for x in range(0,4)]
		for j in action_category:
			if j=="1":
				a[0] += 1
			elif j=="2":
				a[1] += 1
			elif j=="3":
				a[2] += 1
			elif j=="4":
				a[3] += 1
		user_dict[uid][0] += a[0]
		# print user_dict[uid][0]
		user_dict[uid][2] += a[1]
		# print user_dict[uid][3]
		user_dict[uid][4] += a[2]
		user_dict[uid][6] += a[3]
		if a[0] != 0 :
			user_dict[uid][1] += 1
			# print user_dict[uid][1]
		if a[1] != 0 :
			user_dict[uid][3] += 1
		if a[2] != 0 :
			user_dict[uid][5] += 1
		if a[3] != 0 :
			user_dict[uid][7] += 1 

	file = open("user_feature"+date+".txt","w")
	for i in range(len(user)):
		file.write(user[i])
		for j in range(0,8):
			file.write('\t'+str(user_dict[user[i]][j]))
		file.write('\n')
	file.close()

date = raw_input("date: ")
func_feature_1(date)

# func_user()