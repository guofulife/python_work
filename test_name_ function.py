# -*- coding: utf-8 -*-
import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
#����name_function.py
	def test_first_last_name(self):
#�ܹ���ȷ�ش�����Janis Joplin������������
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
unittest.main()