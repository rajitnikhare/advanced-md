'''
Created on Jan 11, 2019

@author: Rajit
'''
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig, show

def plotGraphForDayVsCommit(data):
    day=[]
    commit_count=[]
    for key, value in data.items():
            day.append(key)
            commit_count.append(value)
        
    plt.plot(day, commit_count, color='orange')    
    plt.xlabel('Commit Count')
    plt.ylabel('Days')
    plt.title('Day Vs Commit')
    #show();
    savefig('DayVsCommit.png',bbox_inches='tight')
    ### might need to wait for plot to download before copying
    

