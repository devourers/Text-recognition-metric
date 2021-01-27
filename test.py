#prerequisite is that text boxes are recognising one word at a time
'''RECALL'''
def getRecall(gtbox, detboxes):
    a = list(gtbox)
    b = []
    for box in detboxes:
        for i in range(len(box)):
            b.append(box[i])
    numOfBoxes = len(detboxes)
    totalCount = 0
    for i in range(len(a)):
        if i < len(b):
            if a[i] == b[i]:
                totalCount += 1
    
    return (totalCount - (numOfBoxes - 1))/len(a)


'''PERCISION'''

def getPercision(gtbox, detboxes):
    return 0

print(getRecall("abcdef", ["abc","def"]))