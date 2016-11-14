'''
Created on Nov 13, 2016

@author: mjw
'''

from . import Card

class Princess(Card):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.rank = 8
        
    def perform(self, action):
        pass