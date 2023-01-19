from flask import Flask, render_template, request
import pied_poker as pp
import numpy as np
 
with open('SW_pokerstreaming/p1.txt') as f:
        p1 = f.read().split()
with open('SW_pokerstreaming/p2.txt') as f:
        p2 = f.read().split()
with open('SW_pokerstreaming/p3.txt') as f:
        p3 = f.read().split()
with open('SW_pokerstreaming/community.txt') as f:
        community = f.read().split()
with open('SW_pokerstreaming/names.txt') as f:
        names = f.read().split()
with open('SW_pokerstreaming/money.txt') as f:
        money= f.read().split()
with open('SW_pokerstreaming/bets.txt') as f:
        money= f.read().split()
    
pcommunity=[]
for i in community:
        if(i!='c'):
            pcommunity.append(pp.Card(i))
odds=[]
if(p1[0]!='c' and p1[1]!='c'):
        pp1=pp.Player(names[0],pp.Card.of(p1[0],p1[1]))
        pp2=pp.Player(names[1],pp.Card.of(p2[0],p2[1]))
        pp3=pp.Player(names[2],pp.Card.of(p3[0],p3[1]))

        legit_players=[]
        pn=0
        if(int(money[0])>0):
            legit_players.append(pp1)
            pn=pn+1
        if(int(money[1])>0):
            legit_players.append(pp2)
            pn=pn+1
        if(int(money[2])>0):
            legit_players.append(pp3)
            pn=pn+1
        
        simulator = pp.PokerRoundSimulator(pcommunity, legit_players,pn)
        num_simulations = 10000
        simulation_result = simulator.simulate(n=num_simulations, n_jobs=1)
        
        for i in range (0,pn):
            odds.append(simulation_result.probability_of(pp.PlayerWins(legit_players[i])).__percent_str__)
            odds[i]=str(round(float(odds[i][0:-2])))
              
            print(odds)
        
            
else:
        odds[0]="unknown"
        odds[1]="unknown"
        odds[2]="unknown"
