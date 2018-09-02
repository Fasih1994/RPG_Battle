#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 20:08:17 2018

@author: fasih
"""
import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
        self.BOLD = ''
        self.UNDERLINE = ''
        
class Person:
    def __init__(self,hp,mp,atk,df,magic, item):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp 
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+10
        self.df = df
        self.magic = magic
        self.item = item
        self.actions = ["Attack","Magic",'Item']
    
    def generateDamage(self):
        return random.randrange(self.atkl, self.atkh)
    
    def takeDamage(self,dmg):
        self.hp -= dmg
        if self.hp<0:
            self.hp = 0
        return self.hp

    def heal(self,dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    
    def getHp(self):
        return self.hp
    
    def getMaxHp(self):
        return self.maxhp
    
    def getMp(self):
        return self.mp
    
    def getMaxMp(self):
        return self.maxmp
    
    def reduceMp(self,cost):
        self.mp -= cost
    
    def chooseAction(self):
        i = 1
        print("\nAction")
        for item in self.actions:
            print('   '+str(i)+':',item)
            i+=1
   
    def chooseMagic(self):
        i=1
        print("\nMagic")
        for spell in self.magic:
            print('   '+str(i)+':', spell.name,"(cost:",str(spell.cost)+")")
            i+=1
        
    def chooseItem(self):
        i=1
        print('\nItem')
        for item in self.item:
            print('   '+str(i)+':',item['item'].name, ':',item['item'].description,'(x',item["quantity"],')')
            i+=1