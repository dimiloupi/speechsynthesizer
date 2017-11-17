import os
import SimpleAudio as SA
import argparse
from nltk.corpus import cmudict
import re
import nltk
from datetime import date
from nltk.tokenize import word_tokenize, sent_tokenize


### NOTE: DO NOT CHANGE ANY OF THE EXISITING ARGUMENTS
parser = argparse.ArgumentParser(
    description='A basic text-to-speech app that synthesises an input phrase using monophone unit selection.')
parser.add_argument('--monophones', default="monophones", help="Folder containing monophone wavs")
parser.add_argument('--play', '-p', action="store_true", default=False, help="Play the output audio")
parser.add_argument('--outfile', '-o', action="store", dest="outfile", type=str, help="Save the output audio to a file",
                    default=None)
parser.add_argument('phrase', nargs=1, help="The phrase to be synthesised")

# Arguments for extensions
parser.add_argument('--spell', '-s', action="store_true", default=False,
                    help="Spell the phrase instead of pronouncing it")
parser.add_argument('--volume', '-v', default=None, type=float,
                    help="A float between 0.0 and 1.0 representing the desired volume")

args = parser.parse_args()

print args.monophones



# TASK1 A- normalize-remove/filter punctuation and make lower case characters

class Synth(object):
    def __init__(self, wav_folder):
        self.phones = {}
        self.get_wavs(wav_folder)


    def normalize(self, target_phrase):
        normalized_phrase = target_phrase.lower()
        tokens = [word for sent in sent_tokenize(normalized_phrase) for word in word_tokenize(sent)]
        words1= filter(lambda word: word not in './,;:?-!()[]', tokens)
        return words1


    def get_wavs(self, wav_folder):#just read the waves
        for root, dirs, files in os.walk(wav_folder, topdown=False):
            for file in files:
                x = SA.Audio()
                x.load(wav_folder + '/' + file)
                y = file.split('.')[0]
                phones[y] = x

    def concatenate(self, phone_list):
        conc_list = []
        for element in phone_list:
            if element in phones:
                print phones
        #         conc_list.append(phones[element].data)
        # return np.concatenate(conc_list)





#TASK1 B- Convert word sequence to phone sequence by using cmudict
    def get_phone_seq(self, phrase):
        x = RegxpTokenizer[]

        cmu_entries = nltk.corpus.cmudict.dict()
        #for every word in phrase find the phone of the word in cmudict and replace it in a new list. Raise error if the phoneme
        #can not be found.
        #apo to dictionary exo [u'R', u'OW1'] prepei na fugoun oi arithmoi kai na ginei lower      phone_list = []
        for word in phrase:
            if word in cmu_entries:
                phone_list.extend(cmu_entries[word[0]])
                phone_list = [word.lower() for word[0] in phone_list]






                # phone_list = [word.lower() for word in phone_list]
                # phone_list = [phone_list.append[word] for word in phone_list if not word[-1].isdigit]
            else:
                print " Error : Word {} not found in dictionary" .format(word)
            print phone_list


#extension A
#extension B
#extension C
    def get_spell(self, phrase):
        d=nltk.corpus.cmudict.dict()
        characters=[]
        #for every word in the phrase
        for word in phrase:
            spell_list=[]
            #split the word and save it to an empty list
            w1= word.split("")
            spell_list.append(w1)
            #for every character in the spelling list
            for x in spell_list:
                #if character in list add it into characters list
                if x in d:
                    characters.append(x)
                #else print error message
                else:
                    print"Error: Letter {} not found in dictionary".format(x)
        return characters


#extension D
    #def transform_num2words(self,phrase):






#Task1 C- save the output wav file by using the simpleaudio file
# QUESTION Should I transform  s.data into np.arrays to make code functional?
if __name__ == "__main__":
    S = Synth(wav_folder=args.monophones)
    # out is the Audio object which will become your output
    # you need to modify out.data to produce the correct synthesis
    out = SA.Audio(rate=16000)
    target_phrase = S.normalize(args.phrase[0])
    phone_list = S.get_phone_seq(target_phrase)
    #print phone_list
    #out.data = S.concatenate(phone_list)
    #out.play()
    print out.data, type(out.data)





    #print phone_dictionary
    #print output_norm

    #set out.data = concantenation of waveforms(np.arrays)
    #phone_seq = get_phone_seq(args.phrase[0])
    #p=np.array(phone_list)
    #spectral components/ Fourier transform
    #s=np.fft.fft(p)
    #p = np.concatenate((p, np.sin((2 * np.pi * f / sampling_rate) * np.arange(total_tone_time * sampling_rate) + phase)))
    #phase += 2 * np.pi * f * total_tone_time
    #phase %= 2 * np.pi
    #play the file
    #p.play()
    #save the file
    #p.save()
