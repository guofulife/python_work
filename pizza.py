# -*- coding: utf-8 -*-
def make_pizza(size, *toppings):
#����Ҫ�����ı���
	print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)