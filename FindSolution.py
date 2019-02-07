'''
Created on Jan 11, 2019

@author: Rajit
'''
import json
import datetime
from JsonToSqlLite import SolutionToDbJob, clean
from awscli.customizations.emr.constants import TRUE
from PlotGraph import plotGraphForDayVsCommit



def add(day,freq,counter):
    
    if day in counter:
        counter[day] = counter[day] + freq
    else:
        counter[day] = freq
    
            
def findDayOfMaximumCommit():
    counter = dict()
    
    dayMap = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
    
    with open('punch_card.json') as json_file:  
        data = json.load(json_file)
        for p in data:
            add(p[0],p[2],counter)
    highest = 0
    dayIndex=0
    dataForGraph = dict()
    for key, value in counter.items():
        dataForGraph[dayMap[key]]=value
        if(highest<value):
            highest = value
            dayIndex = key
   
    
    plotGraphForDayVsCommit(dataForGraph);
    clean("B");
    SolutionToDbJob("findDayOfMaximumCommit", highest, dayMap[dayIndex])
    print("The day with the maximum commit count is " +dayMap[dayIndex] + " and the commit count is "+ str(highest))
    return TRUE


def findTheWeekWithMaxCommit():
    
    now = datetime.datetime.now()
    numberofWeek = datetime.date(now.year,now.month,now.day).isocalendar()[1]
    numberofWeeka=numberofWeek;
    
    arr = [] 
    with open('participation.json') as json_file:  
        data = json.load(json_file)
        for p in data['all']:
            arr.append(p)
         
    while(numberofWeek!=0):
        del arr[-1]
        numberofWeek=numberofWeek-1;
    
    max_commit = max(arr)
    weeknmuber=[]
    for i in range(len(arr)):
        if(max_commit==arr[i]):
            weeknmuber.append(i);
    k=0
    output =""
    clean("A");
    for i in range(len(weeknmuber)):
        k = weeknmuber[i]+1+numberofWeeka
        output+=("The number of week of maximum number of commit="+ str(k) +"\n")
        SolutionToDbJob("findTheWeekWithMaxCommit",k,"")
        print(output)
    return TRUE;


