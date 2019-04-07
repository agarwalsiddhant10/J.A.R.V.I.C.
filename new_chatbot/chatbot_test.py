import torch
from torch.jit import script, trace
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import csv
import random
import re
import os
import unicodedata
import codecs
from io import open
import itertools
import math
import pickle

from preprocessing.utils import loadPrepareData, batch2TrainData
from chatbot_class import chatbot

PAD_token = 0  # Used for padding short sentences
SOS_token = 1  # Start-of-sentence token
EOS_token = 2  # End-of-sentence token

MAX_LENGTH = 40
USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")


save_dir = "data/"
voc, pairs = loadPrepareData("imput.txt", "my_corpus", "preprocessing/data/input.txt", save_dir)
# Print some pairs to validate
print("\npairs:")
for pair in pairs[:10]:
    print(pair)

C = chatbot(voc = voc, model_name = "new_model", corpus_name = 'my_corpus')
C.train(voc=voc, pairs = pairs, learning_rate = 0.0001, n_iterations = 1000,print_every = 1, save_every=100)
C.chat()
s = C.chat_output(voc = voc, input_str = "Hi")
print(s)