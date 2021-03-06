import numpy as np
import random
import math
import dunbins

def degtorad(angle):
    return angle / 360 * 2 * math.pi

def radtodeg(angle):
    return angle / 2 / math.pi * 360

'''
#要算旅行商问题的版本，每个无人机执行任务顺序未知
def dismatrix(UAVMission:list,UAVcoor:list,targetcoor:list,ThreatRadius:int,TurnRadius:int,ReconTime:int,Velocity:int):
    coormatrix = [[None for _ in range(4)]for _ in range(7)]
    coormatrix[0][0],coormatrix[1][0],coormatrix[2][0],coormatrix[3][0] = 0,UAVcoor[0],UAVcoor[1],UAVcoor[2]
    coormatrix[4][0],coormatrix[5][0],coormatrix[6][0] = UAVcoor[0],UAVcoor[1],UAVcoor[2]
    for i in range(len(UAVMission[0])):
        if UAVMission[0][i] < 100 or UAVMission[0][i] >= 10000:
            if UAVMission[0][i] < 100:
                target = UAVMission[0][i]
            else:
                target = int(UAVMission[0][i] / 10000)
            coormatrix[0][i+1] = target
            inangle = UAVMission[1][i]
            outangle = UAVMission[1][i] + radtodeg(Velocity * ReconTime / TheartRadius)
            coormatrix[1][i+1] = targetcoor[0][target-1] + ThreatRadius * math.cos(inangle)
            coormatrix[2][i+1] = targetcoor[1][target-1] + ThreatRadius * math.sin(inangle)
            coormatrix[3][i+1] = inangle
            coormatrix[4][i+1] = targetcoor[0][target-1] + ThreatRadius * math.cos(outangle)
            coormatrix[5][i+1] = targetcoor[0][target-1] + ThreatRadius * math.sin(outangle)
            coormatrix[6][i+1] = outangle
        else:
            target = int(UAVMission[0][i] / 100)
            coormatrix[0][i+1] = target
            coormatrix[1][i+1],coormatrix[2][i+1],coormatrix[3][i+1] = targetcoor[0][target-1],targetcoor[1][target-1],UAVMission[1][i] #角度不是弧度
            coormatrix[4][i+1],coormatrix[5][i+1],coormatrix[6][i+1] = targetcoor[0][target-1],targetcoor[1][target-1],UAVMission[1][i]
    dismatrix = [[float('inf') for _ in range(1+len(UAVMission[0]))] for _ in range(1+len(UAVMission[0]))]
    for i in range(1+len(UAVMission[0])):
        for j in range(1+len(UAVMission[0])):
            start = [coormatrix[4][i],coormatrix[5][i],coormatrix[6][i]]
            end = [coormatrix[1][j],coormatrix[2][j],coormatrix[3][j]]
            d = shortestpath(start,end,TurnRadius)
            dismatrix[i][j] = d
    return dismatrix

def totaldis(chrome:list,origincoor:list,targetcoor:list,ThreatRadius:int,TurnRadius:int,ReconTime:int,Velocity:int):
    sum = 0
    route = []
    for i in range(len(origincoor)):
        UAVMission = [chrome[0][3*i:3*i+3],chrome[1][3*i:3*i+3]]
        UAVcoor = origincoor[i]
        DisMatrix = dismatrix(UAVMission,UAVcoor,targetcoor,ThreatRadius,TurnRadius,ReconTime,Velocity)
        dis, path = DSP(DisMatrix,UAVMission)
        sum = sum + dis
        route.append(path)
    return sum,route
'''
#不用计算旅行商问题，任务顺序就是基因排列顺序
def distance(UAVMission:list,UAVcoor:list,targetcoor:list,ThreatRadius:int,TurnRadius:int,ReconTime:int,Velocity:int):
    coormatrix = [[None for _ in range(4)]for _ in range(7)]
    coormatrix[0][0],coormatrix[1][0],coormatrix[2][0],coormatrix[3][0] = 0,UAVcoor[0],UAVcoor[1],UAVcoor[2]
    coormatrix[4][0],coormatrix[5][0],coormatrix[6][0] = UAVcoor[0],UAVcoor[1],UAVcoor[2]
    for i in range(len(UAVMission[0])):
        if UAVMission[0][i] < 100 or UAVMission[0][i] >= 10000:
            if UAVMission[0][i] < 100:
                target = UAVMission[0][i]
            else:
                target = int(UAVMission[0][i] / 10000)
            coormatrix[0][i+1] = target
            inangle = UAVMission[1][i]
            outangle = UAVMission[1][i] + radtodeg(Velocity * ReconTime / ThreatRadius)
            coormatrix[1][i+1] = targetcoor[0][target-1] + ThreatRadius * math.cos(inangle)
            coormatrix[2][i+1] = targetcoor[1][target-1] + ThreatRadius * math.sin(inangle)
            coormatrix[3][i+1] = inangle
            coormatrix[4][i+1] = targetcoor[0][target-1] + ThreatRadius * math.cos(outangle)
            coormatrix[5][i+1] = targetcoor[0][target-1] + ThreatRadius * math.sin(outangle)
            coormatrix[6][i+1] = outangle
        else:
            target = int(UAVMission[0][i] / 100)
            coormatrix[0][i+1] = target
            coormatrix[1][i+1],coormatrix[2][i+1],coormatrix[3][i+1] = targetcoor[0][target-1],targetcoor[1][target-1],UAVMission[1][i] #角度不是弧度
            coormatrix[4][i+1],coormatrix[5][i+1],coormatrix[6][i+1] = targetcoor[0][target-1],targetcoor[1][target-1],UAVMission[1][i]
    dis = 0
    for i in range(len(UAVMission[0])):
        start = [coormatrix[4][i],coormatrix[5][i],coormatrix[6][i]]
        end = [coormatrix[1][i+1],coormatrix[2][i+1],coormatrix[3][i+1]]
        d = shortestpath(start,end,TurnRadius)
        dis =dis + d
    return dis

def totaldis(chrome:list,origincoor:list,targetcoor:list,ThreatRadius:int,TurnRadius:int,ReconTime:int,Velocity:int):
    sum = 0
    for i in range(len(origincoor)):
        UAVMission = [chrome[0][3*i:3*i+3],chrome[1][3*i:3*i+3]]
        UAVcoor = origincoor[i]
        d = distance(UAVMission,UAVcoor,targetcoor,ThreatRadius,TurnRadius,ReconTime,Velocity)
        sum = sum + d
    return sum

def shortestpath(q0,q1,turning_radius)
		path = dubins.shortest_path(q0, q1, turning_radius)
		configurations, _ = path.sample_many(0.5)	
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
'''
origincoor = [[0],[0],[0]]
UAVMission = [[1,200],[20,30]]
Velocity = 50
ThreatRadius = 100
ReconTime = 5
targetcoor = [[1000,500,1000],[1000,500,500]]
coormatrix = [[None for _ in range(4)]for _ in range(7)]
print(coormatrix)
coormatrix[0][0],coormatrix[1][0], coormatrix[2][0],coormatrix[3][0]= 0,origincoor[0][0],origincoor[1][0],origincoor[2][0]
print(coormatrix)

for i in range(len(UAVMission[0])):
    if UAVMission[0][i] < 100 or UAVMission[0][i] >= 10000:
        if UAVMission[0][i] < 100:
            target = UAVMission[0][i]
        else:
            target = int(UAVMission[0][i] / 10000)
        coormatrix[0][i+1] = target
        inangle = UAVMission[1][i]
        outangle = UAVMission[1][i] + radtodeg(Velocity * ReconTime / ThreatRadius)
        coormatrix[1][i+1] = targetcoor[0][target-1] + ThreatRadius * math.cos(inangle)
        coormatrix[2][i+1] = targetcoor[1][target-1] + ThreatRadius * math.sin(inangle)
        coormatrix[3][i+1] = inangle
        coormatrix[4][i+1] = targetcoor[0][target-1] + ThreatRadius * math.cos(outangle)
        coormatrix[5][i+1] = targetcoor[0][target-1] + ThreatRadius * math.sin(outangle)
        coormatrix[6][i+1] = outangle
    else:
        target = int(UAVMission[0][i] / 100)
        coormatrix[0][i+1] = target
        coormatrix[1][i+1],coormatrix[2][i+1],coormatrix[3][i+1] = targetcoor[0][target-1],targetcoor[1][target-1],UAVMission[1][i] #角度不是弧度
        coormatrix[4][i+1],coormatrix[5][i+1],coormatrix[6][i+1] = targetcoor[0][target-1],targetcoor[1][target-1],UAVMission[1][i]
print(coormatrix)
print(float('inf') + 333)
'''
