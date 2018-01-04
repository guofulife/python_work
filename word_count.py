# -*- coding: utf-8 -*-
def count_words(filename):
#����һ���ļ����°������ٸ�����
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
# �����ļ����°������ٸ�����
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) +" words.")
filename = 'guest_book.txt'
count_words(filename)
filenames = ['guest_book.txt', 'programming.txt', 'moby_dick.txt', 'pi_digits.txt']
for filename in filenames:
	count_words(filename)
