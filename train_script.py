import train

handle = open("data.txt", "r")
data = handle.read()

Train = train.TrainML()

Train.fit(data)
