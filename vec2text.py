import pandas as pd
import numpy as np

df = pd.read_pickle('./dataset/testData.pkl')
captions = df['Captions'].values
ids = df['ID'].values

id2word_dict = dict(np.load('./dictionary/id2Word.npy'))
word2Id_dict = dict(np.load('./dictionary/word2Id.npy'))

print(len(captions))
caption = []
idx = []
for i in range(len(captions)):
    # caption[i]
    line = ""
    for k in captions[i]:
        line += id2word_dict[k] + " "
    # print(line)
    caption.append(line)
    idx.append(ids[i])
    # print(len(caption[image_path[i]]))

# print(caption.keys())
# print(caption[0])
# print(len(caption))
d = {'ID': idx, 'Captions': caption}
df = pd.DataFrame(d)
print(df.head())
df.to_pickle('./test_raw_text.pkl')