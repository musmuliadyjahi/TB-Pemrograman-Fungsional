import matplotlib.pyplot as plt
import time

def doffy(dmgList):
    asd = []
    for i in range(len(dmgList)):
        a = ("Attack " + str(i+1))
        asd.append(a)
    plt.figure(num=None, figsize=(10,6))
    plt.bar(asd, dmgList)
    total = str(sum(dmgList))
    li = str(dmgList)
    plt.figtext(.02, .02, "Total dmg = " + total +"\n"+ li)
    plt.show()

def bigMom(dmgList):
    asd = []
    for i in range(len(dmgList)):
        a = ("Attack " + str(i+1))
        asd.append(a)
    plt.figure(num=None, figsize=(10,6))
    plt.bar(asd, dmgList)
    total = str(sum(dmgList))
    li = str(dmgList)
    plt.figtext(.02, .02, "Total dmg = " + total +"\n"+ li)
    plt.show()

def pacifista(dmgList):
    asd = []
    for i in range(len(dmgList)):
        a = ("Attack " + str(i+1))
        asd.append(a)
    plt.figure(num=None, figsize=(10,6))
    plt.bar(asd, dmgList)
    total = str(sum(dmgList))
    li = str(dmgList)
    plt.figtext(.02, .02, "Total dmg = " + total +"\n"+ li)
    plt.show()

def crocodile(dmgList):
    asd = []
    for i in range(len(dmgList)):
        a = ("Attack " + str(i+1))
        asd.append(a)
    plt.figure(num=None, figsize=(10,6))
    plt.bar(asd, dmgList)
    total = str(sum(dmgList))
    li = str(dmgList)
    plt.figtext(.02, .02, "Total dmg = " + total +"\n"+ li)
    plt.show()

def kizaru(dmgList):
    asd = []
    for i in range(len(dmgList)):
        a = ("Attack " + str(i+1))
        asd.append(a)
    plt.figure(num=None, figsize=(10,6))
    plt.bar(asd, dmgList)
    total = str(sum(dmgList))
    li = str(dmgList)
    plt.figtext(.02, .02, "Total dmg = " + total +"\n"+ li)
    plt.show()