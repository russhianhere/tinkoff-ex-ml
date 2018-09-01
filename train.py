import pickle

class TrainML:


    def fit(self, text):

        d = {}

        text = self.cleantext(text)
        word_array = text.split()

        for index, word in enumerate(word_array):

            try:
                next_word = word_array[index+1]
            except IndexError:
                break

            d[word] = d.get(word,{})

            if next_word in d[word]:
                d[word][next_word] += 1
            else:
                d[word][next_word] = 1

        self.save_obj(d, "trained_dict")
        print (d)



    def cleantext(self, text):

        needclean = "!@#$,.?:;"

        for char in needclean:
            text = text.replace(char,"")
        text = text.lower()
        return text

    def save_obj(self, obj, name ):
        with open('trained_data/'+ name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
