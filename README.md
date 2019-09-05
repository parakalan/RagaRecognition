# RagaRecognition

Attempt to identify the *ragam* of a Carnatic Music piece.

Uses a simple kNN classifier to find the ragam. 
Direct implementation of [this](https://repositori.upf.edu/bitstream/handle/10230/33117/Gulati_ISMIR2016_time.pdf) paper.

* `python main.py` - Generate surfaces for all songs except test set.
* `python training.py` - Train all surfaces on PQ Model, create model dump.
* `python predict.py` - Run prediction for test set.