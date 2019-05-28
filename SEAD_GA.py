#This is the code for solving SEAD problem 
import random
import math
import Tkinter
from GA import GA

class SEAD(object):
	"""docstring for SEAD"""
	def __init__(self, aLifeCount=100,aMaxMissionnum=3):
		self.MaxMissionNum=aMaxMissionnum;
		self.lifecount=aLifeCount
		self.ga=GA(aCrossRate=0.7, 
			aMutationRate=0.02, 
			aLifeCount=self.lifecount, 
			aGeneLength= MaxMissionNum*len(self.uavs), #Limit the max times of a uav's mission
			aMatchFun = self.matchFun())


	def shortest_distance(q0,q1)

	def function():
		pass


	def matchFun():

def main():
    print('this message is from main function')


if __name__ == '__main__':
    main()
    # print(__name__)		
		

		