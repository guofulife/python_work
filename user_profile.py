# -*- coding: utf-8 -*-
def build_profile(first, last, **user_info):
#����һ���ֵ䣬���а�������֪�����й��û���һ��
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)
