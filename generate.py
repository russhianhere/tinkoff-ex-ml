import random
import pickle

class Generate:


    def __init__(self,
                generate,
                length=100,
                seed=False):
        self.length = length
        self.seed = seed
        self.generate = generate


    def fill(self):
        d = self.load_obj(self.generate)
        d_list = list(d.keys())
        d_val = list(d.values())

        past_word = random.choice(d_list)

        if self.seed != False:

            past_word = self.seed

        gen_text = past_word + " "

        for i in range (0, self.length):

            try:
                key = self.weight_rand(d[past_word])

                past_words = d[past_word]
                list_words = list(past_words.keys())

                past_word = list_words[key]
                gen_text += past_word + " "

            except KeyError:
                past_word = random.choice(d_list)


        print (gen_text)

    def load_obj(self, name):
        with open('trained_data/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)


    def weight_rand(self,obj):
        obj_list = list(obj.values())
        sum = self.listsum(obj_list)
        rand_int = random.randint (1, sum)

        cnt = 0

        for i in obj_list:
            rand_int -= i
            if rand_int <= 0:
                break
            cnt += 1
        return cnt


    def listsum(self, numList):
        Sum = 0
        for i in numList:
            Sum = Sum + i
        return Sum
