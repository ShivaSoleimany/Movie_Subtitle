import pysrt

from tqdm import tqdm
from loguru import logger

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

from pymongo import MongoClient


def time_to_elapsed_time(time):
    #function to convert the start time and end time to 
    #objects that can be encoded and are unique for each subtitle line
    return time.hour*3600 + time.minute*60 + time.second

class Subtitle:

    def __init__(self, file_path):
        self.subs = pysrt.open(file_path)
        self.words = []
        self.stems = []
        self.movie_name = file_path.split('/')[-1]

    def stemmize(self, words):
        stemmer = PorterStemmer()
        stems = list(map(stemmer.stem, words))

        return stems


    def tokenize(self, sub_line):
        logger.info('Tokenizing subtite...')
        words = word_tokenize(sub_line.text)

        return words

    def sub_to_mongo(self):

        logger.info('Creating database')
        self.conn = MongoClient()
        self.db = self.conn.difficult_words
        self.col = self.db.subtitle

        for sub in tqdm(self.subs):
            words = self.tokenize(sub)
            stems = self.stemmize(words)
            start = time_to_elapsed_time(sub.start.to_time())
            end = time_to_elapsed_time(sub.end.to_time())
            doc = dict(
                movie=self.movie_name,
                text=sub.text,
                start=start,
                end=end,
                tokens=words,
                stems=stems
                )

            #add a doc for this subtitle line to our collection,
            #update it if a doc with same name and start and end time already exists
            self.col.update_one(
                dict(movie=self.movie_name, start=start, end=end),
                {
                    "$set":doc
                },
                upsert = True
            )


if __name__ =='__main__':
    from src.data import DATA_DIR
    from collections import Counter

    sub_file_path = f'{DATA_DIR}/subtitles/Interstellar-English.srt'
    sub = Subtitle(sub_file_path)
    sub.sub_to_mongo()
    #sub.tokenize()
    #print(Counter(sub.words).most_common(10))