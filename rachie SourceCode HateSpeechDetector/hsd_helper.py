import re
import string


import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import warnings
import pickle

warnings.filterwarnings('ignore')


# label1 = Negative
# label 0 = Normal

def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', text)


def clean_text(text):
    delete_dict = {sp_character: '' for sp_character in string.punctuation}
    delete_dict[' '] = ' '
    table = str.maketrans(delete_dict)
    text1 = text.translate(table)
    textArr = text1.split()
    text2 = ' '.join([w for w in textArr if (not w.isdigit() and (not w.isdigit() and len(w) > 3))])

    return text2.lower()


def text_sentiment(text):
    maxlen = 50
    cutoff = 0.5
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    model = load_model("sentiment.h5")
    text_pd = pd.DataFrame({'tweet': text})

    text_pd['tweet'] = text_pd['tweet'].apply(remove_emoji)
    text_pd['tweet'] = text_pd['tweet'].apply(clean_text)

    f_test = np.array(tokenizer.texts_to_sequences(text_pd['tweet'].tolist()))
    f_test = pad_sequences(f_test, padding='post', maxlen=maxlen)

    # predict on actual test data
    predictions = model.predict(f_test)
    print(str(predictions))

    text_pd['pred_sentiment'] = predictions
    text_pd['pred_sentiment'] = np.where((text_pd.pred_sentiment >= cutoff), 1, text_pd.pred_sentiment)
    text_pd['pred_sentiment'] = np.where((text_pd.pred_sentiment < cutoff), 0, text_pd.pred_sentiment)

    print(str(text_pd['pred_sentiment'].tolist()))

    pred_sentiment = text_pd['pred_sentiment'].tolist()
    indexes = [i for i, value in enumerate(pred_sentiment) if value == 1]

    negative_text = [value for i, value in enumerate(text) if i in indexes]
    print(negative_text)

    if len(negative_text) == 0:
        Status = ["No Hate  Speech Detected"]
        return Status

    else:
        return negative_text

# text_sentiment(['fuck you obama , you black ass, why are  you so black, black ass nigga',
#                 'fuck you obama , you black ass, why are  you so black, black ass nigga',
#                 'mocked obama for being black',
#                 ])

