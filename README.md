This is a project for finding the hard words in movie subtitles in order to facilitate learning English with movies. 

**Running the code**

You can use this project at this [address](https://github.com/garain/Word-Difficulty-Prediction).



**Dataset**

The used dataset is WordDifficulty.csv from Kaggle. The I_Zscore column values have been scaled to [0,10] range in order to make them consistant with the user level. The new scaled dataset is saved as word_difficulty.csv.

**Word Difficulty**

The difficulty of each word is determined based on the I_Zscore of that word in the word_difficulty dataset. If the word or its root does not exist in the dataset, the difficulty of the word is predicted based on a trained model. 
The model is based on a paper [[1]](#1) published in ieee and their This site was built using [GitHub repository](https://github.com/garain/Word-Difficulty-Prediction).



## References
<a id="1">[1]</a> 
Word Difficulty Prediction Using Convolutional Neural Networks, A. Basu, A. Garain and S. K. Naskar (2019). TENCON 2019 - 2019 IEEE Region 10 Conference (TENCON), Kochi, India, 2019, pp. 1109-1112.