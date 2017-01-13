import sklearn as sk
import pandas as pd

class Dummy:
    
    def __init__(self,data=[]):
        self.data = data
        
    def addition(self,x,y):
        return x+y
