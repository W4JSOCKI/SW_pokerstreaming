from flask import Flask, render_template, request
import pied_poker as pp
import numpy as np

app = Flask(__name__,template_folder='templates', static_folder='static')
@app.route('/')
def index():
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
    
    
    pcommunity=[]
    for i in community:
        if(i!='c'):
            pcommunity.append(pp.Card(i))

    if(p1[0]!='c' and p1[1]!='c'):
        pp1=pp.Player(names[0],pp.Card.of(p1[0],p1[1]))
        pp2=pp.Player(names[1],pp.Card.of(p2[0],p2[1]))
        pp3=pp.Player(names[2],pp.Card.of(p3[0],p3[1]))
        simulator = pp.PokerRoundSimulator(pcommunity, [pp1, pp2, pp3],3)
        num_simulations = 10000
        simulation_result = simulator.simulate(n=num_simulations, n_jobs=1)
        p1odds= simulation_result.probability_of(pp.PlayerWins(pp1)).__percent_str__
        p2odds= simulation_result.probability_of(pp.PlayerWins(pp2)).__percent_str__
        p3odds= simulation_result.probability_of(pp.PlayerWins(pp3)).__percent_str__
        p1odds=str(round(float(p1odds[0:-2])))
        p2odds=str(round(float(p2odds[0:-2])))
        p3odds=str(round(float(p3odds[0:-2])))
        
    else:
        p1odds="unknown"
        p2odds="unknown"
        p3odds="unknown"


    odds=[p1odds,p2odds,p3odds]
    return render_template('index.html', p1=p1, p2=p2, community=community, p3=p3,names=names,odds=odds)



if __name__ == '__main__':
    app.run(debug=True)