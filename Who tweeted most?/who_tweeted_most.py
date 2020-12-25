#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:18:10 2020

@author: cheerag
"""

def who_tweeted_most(tc_list):
    '''

    Parameters
    ----------
    tc_list : 2D list
         list of list contain user and tweeter id.

    Returns
    -------
    User with maximum tweet count.

    '''

    for tweet_names_list in tc_list:
        name_list = []
        for data in tweet_names_list:
            name_list.append(data.split()[0])
        d = {}
        for name in name_list:
            d[name] = name_list.count(name)
            
        new_dict = sorted(d.items(),key = lambda x : (x[0]))
        max_tweets_num = 0
        for t1,t2 in new_dict:
            if t2 > max_tweets_num:
                max_tweets_num = t2
        
        num_tweets = max_tweets_num
        for t1,t2 in new_dict:
            if t2 >= num_tweets:
                num_tweets = t2
                print(t1,t2)
    
    
if __name__ == "__main__":
    no_of_test_cases = int(input("Enter the number of Test Cases: "))
    test_count = 0
    tc_list = []
    while test_count < no_of_test_cases:
        num = int(input("Enter the number of each Test Case:"))
        count = 0
        tweet_names_list = []
        while count < num:
            name = str(input("Enter the name followed by the Twitter ID: "))
            tweet_names_list.append(name)
            count += 1
        tc_list.append(tweet_names_list)
        test_count += 1
        
    who_tweeted_most(tc_list)

