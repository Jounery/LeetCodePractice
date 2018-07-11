#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def addup(num, target):
	my_dict = dict()
	for i in range(len(nums)):
		x = target - nums[i]
		if nums[i] in my_dict:
			return my_dict.get(nums[i]), i
		else:
			my_dict[x]=i