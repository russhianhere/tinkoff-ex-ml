import train
import argparse

handle = open("data.txt", "r")
data = handle.read()

parser = argparse.ArgumentParser(description='Генерация текста')

parser.add_argument('--save', action='store', dest='saveas', help='Название датасета для сохранения', default="trained_dict")

args = parser.parse_args()


Train = train.TrainML(args.saveas)

Train.fit(data)
