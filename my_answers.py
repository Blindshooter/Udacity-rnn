
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []

    for i in range(len(series) - window_size):
        X.append(series[i : i + window_size])
        y.append(series[i + window_size])     

# reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    model = Sequential()  # Creating model
    model.add(LSTM(5, input_shape = (window_size,1)))  # Adding LSTM layer with 5 units
    model.add(Dense(1, activation=None))   # Adding fully connected module with 1 unit


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    unique_set = set(list(text))

    #print(unique_set)
###
#{'o', 'f', '4', 'é', 'r', 'k', '@', '&', ';', '?', 'â', 'à', '0', 'y', '5', 't', ' ', '8', '2', '%', '/', "'", 'e', ':', 'z', '*', 'd', 'p', 'h', '3', '$', '1', ')', 'v', 'x', 'è', 'n', '.', 'c', 'u', 'w', 'i', 'g', 'q', 'b', '9', ',', 'm', 'a', '(', 's', '6', '"', 'l', 'j', '7', '-', '!'}
###
# remove as many non-english characters and character sequences as you can 

# from rubrick 
# punctuation includes [' ', '!', ',', '.', ':', ';', '?'] 
    punctuation = set([' ', '!', ',', '.', ':', ';', '?'])
    remove_chars = unique_set.difference(punctuation)

    # remove as many non-english characters and character sequences as you can 
    import string
    alphabet = set(list(string.ascii_lowercase))
    remove_chars = ''.join(sorted(list(remove_chars.difference(alphabet))))
    #print(remove_chars) 

# re library makes in easier to replace characters
    import re
    text = re.sub(remove_chars, " ", text)

# shorten any extra dead space created above
    text = text.replace('  ',' ')

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    for i in range(0, len(text) - window_size, step_size):
        inputs.append(text[i : i + window_size]) 
        outputs.append(text[i + window_size])
    

    
    return inputs,outputs
