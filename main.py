#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 20:33:23 2018

@author: fasih
"""
from magic import Spell
from RPG_Battle import Person,bcolors
from inventory import Item

# Create black Magic
fire = Spell("Fire",10,100,"black")
thunder = Spell("Thunder",10,100,"black")
meteor = Spell("Metor",20,200,"black")
blazzerd = Spell("Blazzerd",10,100,"black")
quake = Spell("Quake",14,140,"black")
#some White Magic
cure = Spell("Cure",12,120,"White")
cura = Spell("Cura",18,200,'White')



#creating Inventory
potion = Item("Potion",'potion','heals 50 HP',50)
hipotion = Item("Hi Potion",'potion','heals 100 HP',100)
superpotion = Item("Mega Potion",'potion','heals 500 HP',500)
elixer = Item("Elixer",'elixer','Fully restore one person HP',99999)
HiElixer = Item("Mega elixer",'elixer','Fully restore all charactors Hp/Mp',99999)
granade = Item("Grenade",'attack','deals 500 damage point',500)

player_magic = [fire,thunder,blazzerd,meteor,cure,cura]
player_item = [{'item':potion,'quantity':15},{'item':hipotion,'quantity':5},
               {'item':superpotion,'quantity':3},{'item':elixer,'quantity':5},
               {'item':HiElixer,'quantity':1},{'item':granade,'quantity':2}]
#creating Charactar
player = Person(460,65,60,34,player_magic, player_item)
enemy = Person(1200,65,45,25,[],[])

running = True
print(bcolors.FAIL + bcolors.BOLD + "ENEMY ATTACKS" + bcolors.ENDC)
while running:
    print("===========================================")
    player.chooseAction()
    index = int(input("Choose action:")) - 1
    
    if index == 0 :
        dmg = player.generateDamage()
        enemy.takeDamage(dmg)
        print("You attack for",dmg,"points of Damage.")
    elif index ==1:
        player.chooseMagic()
        magicChoice = int(input("Choose magic:"))-1
        if magicChoice == -1:
            continue
        #generate magic damage
        spell = player.magic[magicChoice]
        magicDamage = spell.generate_damage()
        
        currentMP = player.getMp()
        if spell.cost > currentMP:
            print(bcolors.FAIL+"Not enough MP"+bcolors.ENDC)
            continue
        
        
        
        if spell.Type == 'White':
            player.heal(magicDamage)
            print(bcolors.OKGREEN+spell.name+' heals for',str(magicDamage),'HP.',bcolors.ENDC)
        elif spell.Type == 'black':
            enemy.takeDamage(magicDamage)
            print(bcolors.OKBLUE+"\n" + spell.name +" deals",str(magicDamage),"points of Damage"+bcolors.ENDC)
                  
        
        player.reduceMp(spell.cost)
        
    elif index == 2:
        player.chooseItem()
        itemChoice = int(input('Choose Item:███████████████████')) - 1
        
        if itemChoice == -1:
            continue
        
        item = player.item[itemChoice]['item']
        
        if player.item[itemChoice]['quantity'] == 0:
            print(bcolors.FAIL+'\n'+'None left....'+bcolors.ENDC)
            continue
        player.item[itemChoice]['quantity'] -= 1
        if item.type == 'potion': 
            player.heal(item.prop)
            print(bcolors.OKGREEN+'\n'+item.name,'heals for',str(item.prop),'HP'+bcolors.ENDC)
        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN+'\n'+'Fully restores player MP/HP.'+bcolors.ENDC)
        elif item.type == 'attack':
            enemy.takeDamage(item.prop)
            print(bcolors.FAIL+'\n'+'Enemy takes',item.prop,'points of damage'+bcolors.ENDC)
            
    enemyDmg = enemy.generateDamage()
    player.takeDamage(enemyDmg)
    print("Enemy attacked for",enemyDmg,"points.")    
    print("---------------------------")
    print("Enemey HP:",bcolors.FAIL+str(enemy.getHp())+"/"+str(enemy.getMaxHp())+bcolors.ENDC+'\n')
    print("Player HP:",bcolors.OKGREEN+str(player.getHp())+"/"+str(player.getMaxHp())+bcolors.ENDC)
    print("Your MP:",bcolors.OKBLUE+str(player.getMp())+'/'+str(player.getMaxMp())+bcolors.ENDC)
    
    
    
    
    if enemy.getHp()==0:
        running=False
        print(bcolors.OKGREEN+"You won!"+bcolors.ENDC)
    elif player.getHp() ==0:
        running = False
        print(bcolors.FAIL+"You lose!"+bcolors.ENDC)