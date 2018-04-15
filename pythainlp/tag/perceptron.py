# -*- coding: utf-8 -*-
from __future__ import absolute_import,division,unicode_literals
import six
import sys
if six.PY2:
	print("Thai sentiment in pythainlp. Not support python 2.7")
	sys.exit(0)
import os
import pythainlp
import nltk.tag
import dill
def orchid_data():
	templates_dir = os.path.join(os.path.dirname(pythainlp.__file__), 'corpus')
	template_file = os.path.join(templates_dir, 'pt_tagger_1.dill')
	with open(template_file,'rb') as handle:
		model = dill.load(handle)
	return model
def tag(text,corpus):
	"""
	รับค่าเป็น ''list'' คืนค่าเป็น ''list'' เช่น [('ข้อความ', 'ชนิดคำ')]"""
	if corpus=='orchid':
		tagger = orchid_data()
		return tagger.tag(text)