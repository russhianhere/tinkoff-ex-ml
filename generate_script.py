import generate
import argparse

parser = argparse.ArgumentParser(description='Генерация текста')

parser.add_argument('--length', action='store', type=int, dest='length', help='Количество генерируемых слов', default=100)
parser.add_argument('--seed', action='store', dest='seed', help='Первое слово', default=False)

args = parser.parse_args()

Gen = generate.Generate(args.length, args.seed)

Gen.fill()
