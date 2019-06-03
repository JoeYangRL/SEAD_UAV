#This is the code for solving SEAD problem 
import random
import math
import Tkinter
from GA import GA

class SEAD(object):
	"""docstring for SEAD"""
	def __init__(self, aLifeCount=100,aMaxMissionnum=3):
		self.MaxMissionNum=aMaxMissionnum
		self.lifecount=aLifeCount
		self.ga=GA(aCrossRate=0.7, 
			aMutationRate=0.02, 
			aLifeCount=self.lifecount, 
			aGeneLength= self.MaxMissionNum*len(self.uavs), #Limit the max times of a uav's mission
			aMatchFun = self.matchFun())


	def shortest_distance(q0,q1)
		path = dubins.shortest_path(q0, q1, turning_radius)
		configurations, _ = path.sample_many(step_size)	
		xs=[]
		ys=[]
		zs=[]
		dist=0
		for i in range(0,len(configurations)):
		    xs.append(configurations[i][0])
		    ys.append(configurations[i][1])
		    zs.append(configurations[i][2])
		    if(i>=1):
			x1=numpy.array([configurations[i][0]-configurations[i-1][0],configurations[i][1]-configurations[i-1][1]])
			dist+=math.hypot(x1[0],x1[1])
	        return dist


	def function():
		pass


	def matchFun():

def main():
    print('this message is from main function')


if __name__ == '__main__':
    main()
    # print(__name__)		
		

		
