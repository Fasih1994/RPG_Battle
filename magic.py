#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 17:07:31 2018

@author: fasih
"""
import random
class Spell:
    def __init__(self, name, cost, dmg,Type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.Type = Type
    
    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
    