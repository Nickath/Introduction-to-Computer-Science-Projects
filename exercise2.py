#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from collections import defaultdict
import operator
import requests
import sys
import json
import time
from itertools import groupby
 
 
if __name__ == "__main__":
    date = time.strftime("%d-%m-%Y")
    # date = '22-01-2016'
    allnumbers = [];
    maxlist = [0]*30;
    data = requests.get('http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%(date)).json()['draws']
    for results in data['draw']:
        allnumbers+=(results['results']) #storing all the 'results' from the json file to array res

    numbersfrequency = [0]*81

    for i,val in enumerate(allnumbers):#estimating the maxlist
        numbersfrequency[val] += 1;
    numbersfrequency1 = numbersfrequency[:];#copy our array in order to use it but not make changes to the original one
    counter = 0;
    max_number_old = 0;
    newlist =[];
    helpcounter =0;
    otherlist = [];
    print('Most appeared numbers in Kino ');
    while(counter < 7):
        max_number = max(numbersfrequency1);
        max_position =  numbersfrequency1.index(max(numbersfrequency1));
        maxlist[counter] = max_position;
        if(max_number_old != max_number):
           helpcounter =0;
           newlist.append(maxlist[counter])
           numbersfrequency1[max_position] = 0;
        else:
           helpcounter +=1;
           numbersfrequency1[max_position] = 0;
           newlist.pop()
           for i  in xrange(helpcounter,-1,-1):
               otherlist.extend([maxlist[counter - i]])
           newlist.append(otherlist)   
           otherlist = []
        if(counter == 6):
            counter += 1;
            max_number_old = max_number;
            max_number = max(numbersfrequency1);
            max_position = numbersfrequency1.index(max(numbersfrequency1));
            maxlist[counter] = max_position;


            if(max_number_old != max_number):
                break;
            else:
                helpcounter +=1;
                numbersfrequency1[max_position] = 0;
                
                newlist.pop()
                for i  in xrange(helpcounter,-1,-1):
                   otherlist.extend([maxlist[counter - i]])
                newlist.append(otherlist)  

                otherlist = []
                while(max_number_old == max_number):
                      
                      
                      max_number_old = max_number
                      max_number = max(numbersfrequency1);
                      max_position = numbersfrequency1.index(max(numbersfrequency1));
                      maxlist[counter] = max_position;
                    
                      if(max_number_old == max_number):

                        numbersfrequency1[max_position] = 0;
                      
                        newlist.pop()
                        for i  in xrange(helpcounter,-1,-1):
                           otherlist.extend([maxlist[counter - i]])
                        newlist.append(otherlist)   
                        otherlist = []

                      else:
                            break;
                      counter +=1
                      helpcounter +=1;
        max_number_old = max_number;  
        counter += 1;
  
    print(newlist);#printing the max list



#estimating the min list
    
    minlist = [0]*30;
    otherlist = []
    counter = 0;
    helpcounter=0;
    newlist=[];
    numbersfrequency[0] = 10000;
    min_number_old =10000;

    print('\nLess appeared numbers in Kino ');
    
    while(counter < 7):
        min_number = min(numbersfrequency);
        min_position =  numbersfrequency.index(min(numbersfrequency));
        minlist[counter] = min_position;

        if(min_number_old != min_number):
           helpcounter =0;
           newlist.append(minlist[counter])
           numbersfrequency[min_position] = 10000;
        else:
           helpcounter +=1;
           numbersfrequency[min_position] = 10000;
           newlist.pop()
           for i  in xrange(helpcounter,-1,-1):
               otherlist.extend([minlist[counter - i]])
           newlist.append(otherlist) 

        min_number_old = min_number;
        otherlist = [];
        if(counter == 6):
            counter += 1;
            min_number_old = min_number;
            min_number = min(numbersfrequency);
            min_position = numbersfrequency.index(min(numbersfrequency));
            minlist[counter] = min_position;
            

            if(min_number_old != min_number):
                break;
            else:
                while(min_number_old == min_number):
                      counter +=1
                      helpcounter +=1;
                      min_number_old = min_number
                      min_number = min(numbersfrequency);
                      min_position = numbersfrequency.index(min(numbersfrequency));
                      minlist[counter] = min_position;
                      if(min_number_old == min_number):

                        numbersfrequency[min_position] = 0;
                        

                        newlist.pop()
                        for i  in xrange(helpcounter+1,0,-1):
                           otherlist.extend([minlist[counter - i]])
                        newlist.append(otherlist)   
                        otherlist = []
                        counter +=1;
                      else:
                            break;
                


        counter += 1;
    print(newlist);

