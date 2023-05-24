import numpy as np
from scipy.stats import chisquare, kstest
import pandas as pd

def make_tests(df):
    df_stats = test_chisquare(df)
    df_stats['count'] = df.sum(axis=1)
    df_stats['count'] = df_stats['count'].astype(int)
    column_order = ['count', 'pvalue', 'statystyka']; df_stats = df_stats[column_order]

    # df_stats = df_stats.sort_values('pvalue')
    return df_stats

def test_chisquare(df):

    df_stats = pd.DataFrame(index=range(len(df)), columns=['statystyka', 'pvalue'])
    for row_num in range(len(df)):
        observed_counts = df.iloc[row_num].values
        czestosci_teoretyczne = np.ones(37) / 37
        statystyka, pvalue = chisquare(observed_counts, f_exp=czestosci_teoretyczne *  df.iloc[row_num].sum())
        df_stats['statystyka'].iloc[row_num] = statystyka
        df_stats['pvalue'].iloc[row_num] = pvalue
        df_stats = df_stats.rename(index={row_num: df.index[row_num]})

    return df_stats
