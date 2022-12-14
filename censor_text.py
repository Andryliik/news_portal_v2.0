text = "Весёлые игрушки, занудные побрикушки, нелепая редиска, Алкоголик"

UNWANTED_WORDS = ['зануд', 'нелеп', 'редис', 'алког',]

def censor(text):
        text_good = []
        up_world = text.split()
        word_text = text.lower()
        word_text = word_text.split()
        for word in UNWANTED_WORDS:
            for index, words in enumerate(word_text):
                if word == words[:5]:
                    word_text[index] = f'{words[:1]}{len(words) * "*"}'
                    text_good = word_text
        for index, up in enumerate(text_good):
            text_good[index] = f'{}'

        text_good = " ".join(text_good)
        return print(text_good)


censor(text)