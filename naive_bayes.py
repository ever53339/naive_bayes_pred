import pandas as pd
import numpy as np

HEADERS = ['win', 'clusterid', 'gamemode', 'gametype']
HEADERS.extend([f'hero{i}' for i in range(1, 114)]) 

train_df = pd.read_csv('../data/UCI2016/dota2Train.csv',
                       names=HEADERS
                       )

cond_df = train_df[train_df['win'] == 1]

test_df = pd.read_csv('../data/UCI2016/dota2Test.csv',
                      names=HEADERS)

prior_win = train_df[train_df['win'] == 1].shape[0] / train_df.shape[0]



print(prior_win)
def compute_freq(col):
    total = train_df.shape[0]

def pred(lineups):
    mult, cond_mult = 1, 1
    for i, hero in enumerate(lineups):
        idx = i + 1
        # col_name = f'hero(i)'
        cond_mult *= cond_df[cond_df[f'hero{idx}'] == hero].shape[0] / cond_df.shape[0]
        mult *= train_df[train_df[f'hero{idx}'] == hero].shape[0] / train_df.shape[0]

    return cond_mult * prior_win / mult

l = [0 for i in range(113)]
pos = np.random.choice(113, 10, replace=False)
for i in range(5):
    l[pos[i]] = 1

for i in range(5, 10):
    l[pos[i]] = -1

print(pred(l))
