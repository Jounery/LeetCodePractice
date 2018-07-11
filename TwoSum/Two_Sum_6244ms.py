#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def addup(num, target):
	for index1, i in enumerate(num):
		for index2, j in enumerate(num[index1+1:]):
			if i+j == target:
				return index1, index1+index2+1