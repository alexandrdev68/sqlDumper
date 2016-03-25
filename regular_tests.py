#!/usr/bin/env python
# -*- coding: utf-8  -*-

import re

pattern = '^INSERT'

pattern_obj = re.compile(pattern)

print(pattern_obj.match("INSERT INTO `aquiring_transactions` VALUES (1,'5062997118','M2400073281'),(2,'5063658603','M2400073192'),(3,'5064711976','005-0243182'),(4,'5064779145','005-0229967'),(5,'5064781741','005-0229990')"))