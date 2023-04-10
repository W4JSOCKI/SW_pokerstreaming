from flask import Flask, render_template, request
import pied_poker as pp
import numpy as np

app = Flask(__name__,template_folder='templates', static_folder='static')
@app.route('/')
def index():


    with open('texts/p1.txt') as f:
        p1 = f.read().split()
    with open('texts/p2.txt') as f:
        p2 = f.read().split()
    with open('texts/p3.txt') as f:
        p3 = f.read().split()
    with open('texts/community.txt') as f:
        community = f.read().split()
    with open('texts/names.txt') as f:
        names = f.read().split()
    with open('texts/money.txt') as f:
        money= f.read().split()
    with open('texts/bets.txt') as f:
        bets= f.read().split()
    

    
    intbets=[]
    intmoney=[]
    uncovered_cards=0
    pcommunity=[]
    for i in community:
        if(i!='c'):
            pcommunity.append(pp.Card(i))
            uncovered_cards+=1
    odds=[]
    if(p1[0]!='c' and p1[1]!='c'):

        
        for i in bets:
            intbets.append(int(i))

        with open("texts/bets.txt", "w") as file:  
            for i in range(3):
                intbets[i]+=1000
                bets[i]=str(intbets[i]) 
                intmoney.append(int(money[i]))
            file.write(' '.join(bets))


        pp1=pp.Player(names[0],pp.Card.of(p1[0],p1[1]))
        pp2=pp.Player(names[1],pp.Card.of(p2[0],p2[1]))
        pp3=pp.Player(names[2],pp.Card.of(p3[0],p3[1]))

        legit_players=[]
        pn=0
        if(int(money[0])>0):
            legit_players.append(pp1)
            pn=pn+1
        else:
            p1=['c','c']
        if(int(money[1])>0):
            legit_players.append(pp2)
            pn=pn+1
        else:
            p2=['c','c']
        if(int(money[2])>0):
            legit_players.append(pp3)
            pn=pn+1
        else:
            p3=['c','c']
        
        simulator = pp.PokerRoundSimulator(pcommunity, legit_players,pn)
        num_simulations = 10000
        simulation_result = simulator.simulate(n=num_simulations, n_jobs=1)
        
        for i in range (0,pn):
            odds.append(simulation_result.probability_of(pp.PlayerWins(legit_players[i])).__percent_str__)
            odds[i]=str(round(float(odds[i][0:-2])))
      
        
            
    else:
        odds[0]="unknown"
        odds[1]="unknown"
        odds[2]="unknown"

    if (uncovered_cards==5 and intbets[0]>=4000):
        for i in range(3):
            intmoney[i]-=intbets[i]
            if(odds[i]=="100"):
                intmoney[i]+=3*intbets[i]
            money[i]=str(intmoney[i])
            bets[i]="0"
            intbets[i]=0
        with open("texts/money.txt", "w") as file:  
            file.write(' '.join(money))
        with open("texts/bets.txt", "w") as file:  
            file.write(' '.join(bets))
            
        
 


    
    return render_template('index.html', p1=p1, p2=p2, community=community, p3=p3,names=names,odds=odds,money=money,bets=bets)



if __name__ == '__main__':
    app.run(debug=True)