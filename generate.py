import random
import numpy as np
from Life import Life
from distance import totaldis

origincoor = [[0,0,0],[0,0,10],[0,0,20],[0,0,30],[0,0,40],[0,0,50]]
targetcoor = [[3000,2000,4000,5000],[1000,5000,2000,4000]]
ThreatRadius = 300
TurnRadius = 100
ReconTime = 5
Velocity = 50


def findzero(a,i):
    for jj in range(3):
        if a[3*(i-1)+jj] == 0:
            return 3*(i-1) + jj
    return None

def findrepeat(a,index,UAV,l):
    for m in range(3*(UAV-1),index):
        if a[m] == l:
            return False
    return True

def checklegal(chrome,TargetNum):
    length = len(chrome)
    checksum = 0
    sum = 0
    for i in range(TargetNum):
        checksum = checksum + i + 1
    for j in range(length):
        sum = sum + chrome[j]
    if sum == checksum * 10101:
        return True
    else:
        return False

'''
基因编码方式：
两行：第一行任务(数字含义：recon 1~99，combat 100~9900, verify 10000~990000)，第二行角度（0~360）
N列：N为无人机数量，排列顺序：reconUAV, unionUAV, combatUAV
'''
def newchrome(chrome:list,ReconNum:int,UnionNum:int,CombatNum:int,TargetNum:int):
    for j in range(TargetNum):
        flag = 0
        while flag == 0:
            k = np.random.randint(1, ReconNum+UnionNum+1)
            angle = random.randint(1, 360)
            if findzero(chrome[0], k) != None:
                if findrepeat(chrome[0], findzero(chrome[0], k), k, j + 1):
                    a = findzero(chrome[0], k)
                    chrome[0][a] = j + 1
                    chrome[1][a] = angle
                    flag = 1
    for j in range(TargetNum):
        flag = 0
        while flag == 0:
            k = np.random.randint(ReconNum+1, ReconNum+UnionNum+CombatNum+1)
            angle = random.randint(1, 360)
            if findzero(chrome[0], k) != None:
                if findrepeat(chrome[0], findzero(chrome[0], k), k, j + 1):
                    a = findzero(chrome[0], k)
                    chrome[0][a] = (j + 1) * 100
                    chrome[1][a] = angle
                    flag = 1
    for j in range(TargetNum):
        flag = 0
        while flag == 0:
            k = np.random.randint(1, ReconNum+UnionNum+1)
            angle = random.randint(1, 360)
            if findzero(chrome[0], k) != None:
                if findrepeat(chrome[0], findzero(chrome[0], k), k, j + 1):
                    a = findzero(chrome[0], k)
                    chrome[0][a] = (j + 1) * 10000
                    chrome[1][a] = angle
                    flag = 1
    return chrome

'''
以下都是测试用代码
'''
lives = []

for i in range(10):
                  ###############################待修改生成函数##################################
    chrome = [[0 for _ in range(18)] for _ in range(2)]
    chrome = newchrome(chrome, 2, 2, 2, 4)
    #score = totaldis(chrome,origincoor,targetcoor,ThreatRadius,TurnRadius,ReconTime,Velocity)
                  ###############################待修改生成函数##################################
                  #Life两个参数，一个是序列gene，一个是这个序列的初始适应度值（score）
                  # 因为适应度值越大，越可能被选择，所以一开始种群里的所有基因都被初始化为-1
    life = Life(chrome)#,score)
                  #把生成的这个基因序列life填进种群集合里
    lives.append(life)

print(lives[1].gene)
print(lives[2].gene)
print(checklegal(lives[1].gene[0],4))
print(checklegal(lives[2].gene[0],4))

index1 = 9
index2 = 17
#index2 = 17
tempGene1 = [[],[]]
tempGene2 = [[],[]]
tempGene1[0] = lives[1].gene[0][index1:index2]                      #交叉的基因片段
tempGene1[1] = lives[1].gene[1][index1:index2]
tempGene2[0] = lives[2].gene[0][index1:index2]                      #交叉的基因片段
tempGene2[1] = lives[2].gene[1][index1:index2]
lives[1].gene[0][index1:index2] = tempGene2[0]
lives[1].gene[1][index1:index2] = tempGene2[1]
lives[2].gene[0][index1:index2] = tempGene1[0]
lives[2].gene[1][index1:index2] = tempGene1[1]


print(lives[1].gene)
print(lives[2].gene)
print(checklegal(lives[1].gene[0],4))
print(checklegal(lives[2].gene[0],4))
