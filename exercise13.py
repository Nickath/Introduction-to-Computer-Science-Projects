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
    allnumbers = [0]*32
    winningtimes = 0;
    winningdates = [0]*10;	
    winningdraws = [0]*10;
    winningresults =[[0]]*2
    drawnumber =0;
    day =1 ; #starting from 1 day , then we choose January of 2016 to take all the draws
    data = [];
    user_input = raw_input("Please enter twelve numbers separated by a single comma(,) only: ")
    input_numbers = [int(i) for i in user_input.split(',') if i.isdigit()]
    print(input_numbers);
    print('\nOk, this is gonna take little time ...\n')
    while(day <= 31):
         data = requests.get('http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s-1-2016.json'%(day)).json()['draws']
         print('\nDay:  %s-1-2016 \n'%(day))
         for results in data['draw']:
            drawnumber +=1;
            allnumbers[day]=(results['results']) #storing all the 'results' from the json file to array res 
            if((set(input_numbers)<set(allnumbers[day])) is True):
              print('Winner !')
              winningtimes +=1;
              winningdates[winningtimes] = day
              winningdraws[winningtimes] = drawnumber
         drawnumber =0;
         day +=1;
    for j in range(1,winningtimes+1,1):
        print('You won in date %s-1-2016'%(winningdates[j]));
        print('Number of draw of the day was %s\n'%(winningdraws[j]));
     
    if(winningtimes == 0):
       print('The numbers you chose did not win');
 
