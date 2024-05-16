import math

def miniMax(curDepth,nodeIndex,maxTurn,scores,targetDepth,path):
    if curDepth==targetDepth:
        return scores[nodeIndex],path
    
    if maxTurn:
        leftScore,leftPath=miniMax(curDepth+1,nodeIndex*2,False,scores,targetDepth,path+"L->")
        rightScore,rightPath=miniMax(curDepth+1,nodeIndex*2+1,False,scores,targetDepth,path+"R->")
        if leftScore>rightScore:
            return leftScore,leftPath
        else:
            return rightScore,rightPath
        
    else:
        leftScore,leftPath=miniMax(curDepth+1,nodeIndex*2,True,scores,targetDepth,path+"L->")
        rightScore,rightPath=miniMax(curDepth+1,nodeIndex*2+1,True,scores,targetDepth,path+"R->")
        if leftScore<rightScore:
            return leftScore,leftPath
        else:
            return rightScore,rightPath
            
scores=[-1,4,2,6,-3,-5,0,7]
treeDepth=math.log(len(scores),2)
result,path=miniMax(0,0,True,scores,treeDepth,"")
print('The optimal value is:',result)
print('The path from terminal node to root node is:',path)
