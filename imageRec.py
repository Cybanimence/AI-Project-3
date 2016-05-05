import numpy as np
import cv2
import sys        

def load_image(filename):
        return cv2.imread(filename,0)

def main():
        if len(sys.argv) < 2:
                print "Error: Please specify a 100x100 pixel image file"
                return
        trainDat = []
        trainLabels = []
        testDat = []
        for i in range(2,10):
                trainDat.append(load_image("Data/01/0"+str(i)+".jpg"))
                trainLabels.append(1.0)
                trainDat.append(load_image("Data/02/0"+str(i)+".jpg"))
                trainLabels.append(2.0)
                trainDat.append(load_image("Data/03/0"+str(i)+".jpg"))
                trainLabels.append(3.0)
                trainDat.append(load_image("Data/04/0"+str(i)+".jpg"))
                trainLabels.append(4.0)
                trainDat.append(load_image("Data/05/0"+str(i)+".jpg"))
                trainLabels.append(5.0)
        for i in range(10,72):
                trainDat.append(load_image("Data/01/"+str(i)+".jpg"))
                trainLabels.append(1.0)
                trainDat.append(load_image("Data/02/"+str(i)+".jpg"))
                trainLabels.append(2.0)
                trainDat.append(load_image("Data/03/"+str(i)+".jpg"))
                trainLabels.append(3.0)
                trainDat.append(load_image("Data/04/"+str(i)+".jpg"))
                trainLabels.append(4.0)
                trainDat.append(load_image("Data/05/"+str(i)+".jpg"))
                trainLabels.append(5.0)

        testDat = [load_image(sys.argv[1])]
        train = np.array(trainDat).reshape(-1,(100*100)).astype(np.float32)
        trainLabels = np.array(trainLabels).astype(np.float32)
        test = np.array(testDat).reshape(-1,(100*100)).astype(np.float32)
        testLabels = trainLabels.copy()

        knn = cv2.KNearest()
        knn.train(train,trainLabels)
        ret,result,neighbours,dist = knn.find_nearest(test,k=5)
        pic =  result[0][0]

        if pic == 1:
                print "It's a smile!"
        elif pic == 2:
                print "It's a hat!"
        elif pic == 3:
                print "It's a pound sign!"
        elif pic == 4:
                print "It's a heart!"
        elif pic == 5:
                print "It's a dollar sign!"
        else:
                print "I have no idea what that is a picture of or how the picture provided an alternative output which led to here."

main()
