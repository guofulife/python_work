# -*- coding: utf-8 -*-
import json
# �����ݼ��ص�һ���б���
filename = 'population_json.json'
with open(filename) as f:
	pop_data = json.load(f)
# ��ӡÿ������2010����˿�����
for pop_dict in pop_data:
	if pop_dict['Year'] == '1987':
		country_name = pop_dict['Country Name']
		population = pop_dict['Value']
		print(country_name + ": " + population)
