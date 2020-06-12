#this is some datasci stuff hehe

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from ibm_watson import SpeechToTextV1
from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

csv_path = 'https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv'
df = pd.read_csv(csv_path)

x = df[['Name']]
print(x)
