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

#输入一行gene
def findzero(a,i):
    for jj in range(3):
        if a[3*(i-1)+jj] == 0:
            return 3*(i-1) + jj
    return None

#输入二维gene
def wipe(a,i1,i2):
    for i in range(i1,i2):
        a[0][i], a[1][i] = 0,0
    return a

#有重复输出true, 没有重复输出false,输入gene第一行
def findrepeat(a,index,UAV=None,l=None):
    if UAV != None:
        for m in range(3*(UAV-1),index):
            if a[m] == l or a[m] == l*100 or a[m] == l*10000:
                return True
        return False
    else:
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == index:
                    return True
        return False

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
            angle = np.random.randint(1, 361)
            if findzero(chrome[0], k) != None:
                if findrepeat(chrome[0], findzero(chrome[0], k), UAV=k, l=j + 1) == False:
                    a = findzero(chrome[0], k)
                    chrome[0][a] = j + 1
                    chrome[1][a] = angle
                    flag = 1
    for j in range(TargetNum):
        flag = 0
        while flag == 0:
            k = np.random.randint(ReconNum+1, ReconNum+UnionNum+CombatNum+1)
            angle = np.random.randint(1, 361)
            if findzero(chrome[0], k) != None:
                if findrepeat(chrome[0], findzero(chrome[0], k),UAV=k, l=j + 1)== False:
                    a = findzero(chrome[0], k)
                    chrome[0][a] = (j + 1) * 100
                    chrome[1][a] = angle
                    flag = 1
    for j in range(TargetNum):
        flag = 0
        while flag == 0:
            k = np.random.randint(1, ReconNum+UnionNum+1)
            angle = np.random.randint(1, 361)
            if findzero(chrome[0], k) != None:
                if findrepeat(chrome[0], findzero(chrome[0], k),UAV=k, l=j + 1)== False:
                    a = findzero(chrome[0], k)
                    chrome[0][a] = (j + 1) * 10000
                    chrome[1][a] = angle
                    flag = 1
    return chrome

def correctchrome(chrome:list,index1,index2,TargetNum,ReconNum:int,UnionNum:int,CombatNum:int):
    stable = [chrome[0][0:index1*3],chrome[0][index2*3:]]
    for j in range(TargetNum):
        if findrepeat(stable,j+1) == False:
            flag = 0
            while flag == 0:
                k = np.random.randint(index1+1, min(index2,ReconNum+UnionNum+1))
                angle = np.random.randint(1, 361)
                if findzero(chrome[0], k) != None:
                    if findrepeat(chrome[0], findzero(chrome[0], k), k, j + 1)== False:
                        a = findzero(chrome[0], k)
                        chrome[0][a] = j + 1
                        chrome[1][a] = angle
                        flag = 1
    for j in range(TargetNum):
        if findrepeat(stable,(j+1)*100) == False:
            flag = 0
            while flag == 0:
                k = np.random.randint(max(index1,ReconNum)+1, index2+1)
                angle = np.random.randint(1, 361)
                if findzero(chrome[0], k) != None:
                    if findrepeat(chrome[0], findzero(chrome[0], k), k, j + 1)== False:
                        a = findzero(chrome[0], k)
                        chrome[0][a] = (j + 1) * 100
                        chrome[1][a] = angle
                        flag = 1
    for j in range(TargetNum):
        if findrepeat(stable, (j+1)*10000) == False:
            flag = 0
            while flag == 0:
                k = np.random.randint(index1+1, min(index2,ReconNum+UnionNum+1))
                angle = np.random.randint(1, 361)
                if findzero(chrome[0], k) != None:
                    if findrepeat(chrome[0], findzero(chrome[0], k), k, j + 1)== False:
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
index1 = np.random.randint(len(origincoor))
index2 = np.random.randint(index1+1,len(origincoor) + 1)
print(index1,index2)
tempGene1 = [[], []]
tempGene2 = [[], []]
tempGene1[0] = lives[1].gene[0][index1*3:index2*3]  # 交叉的基因片段
tempGene1[1] = lives[1].gene[1][index1*3:index2*3]
tempGene2[0] = lives[2].gene[0][index1*3:index2*3]  # 交叉的基因片段
tempGene2[1] = lives[2].gene[1][index1*3:index2*3]
lives[1].gene[0][index1*3:index2*3] = tempGene2[0]
lives[1].gene[1][index1*3:index2*3] = tempGene2[1]
lives[2].gene[0][index1*3:index2*3] = tempGene1[0]
lives[2].gene[1][index1*3:index2*3] = tempGene1[1]
print(lives[1].gene)
print(lives[2].gene)
print(checklegal(lives[1].gene[0],4))
print(checklegal(lives[2].gene[0],4))
if checklegal(lives[1].gene[0],4) == False:
    lives[1].gene = wipe(lives[1].gene, index1 * 3, index2 * 3)
    lives[1].gene = correctchrome(lives[1].gene,index1,index2,4,2,2,2)
if checklegal(lives[2].gene[0],4) == False:
    lives[2].gene = wipe(lives[2].gene, index1 * 3, index2 * 3)
    lives[2].gene = correctchrome(lives[2].gene,index1,index2,4,2,2,2)
print(lives[1].gene)
print(lives[2].gene)
print(checklegal(lives[1].gene[0],4))
print(checklegal(lives[2].gene[0],4))


