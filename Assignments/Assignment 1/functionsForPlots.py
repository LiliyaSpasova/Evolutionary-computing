import fitnesses

def countOnesInPopulation(population):
    res=0
    for p in population:
        res+=fitnesses.calcFitnessOnes(p)
    return res

def countMembersOfSchemata(population):
    fitnessOnes=[]
    fitnessZeros=[]
    res=0
    for p in population:
        if(p[0]=='1'):
            res+=1
            fitnessOnes.append(fitnesses.calcFitnessOnes(p))
        else:
            fitnessZeros.append(fitnesses.calcFitnessOnes(p))
    
    return (res,fitnessOnes,fitnessZeros)

def getDataForDecisionPlot(firsParent,secondParent,firstWinner,secondWinner):
    correct=0
    errors=0
    for (p1,p2,w1,w2) in zip (firsParent,secondParent,firstWinner,secondWinner):
        if p1!=p2:
            if w1=='0' and w2=='0': 
                errors+=1
            elif w1=='1' and w2=='1': 
                correct+=1
    return (correct,errors)

