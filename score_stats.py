import pandas as pd

def get_df_score_for_df_wheels(df):
    columns = ['count', 'score', 'len_winning_count', 'avarage_score_per_number']
    df_score = pd.DataFrame(index=df.index, columns=columns)
    df_score['count'] = df.sum(axis=1)
    df_score['count'] = df_score['count'].astype(int)
    # tu mogę wsadzić random df i obliczy len_winning_count i ev for random df
    for num in range(len(df)):
        sum_of_wheel = df.iloc[num].sum()
        value_1_36 = sum_of_wheel/36
        list_of_wheel_count = df.iloc[num].tolist()
        list_of_winning_count = [num for num in list_of_wheel_count if num > value_1_36]
        len_of_winning_counts = len(list_of_winning_count)
        sum_list_of_winning_count = sum(list_of_winning_count)
        ev = calculate_ev(len_of_winning_counts-1, sum_list_of_winning_count, sum_of_wheel)

        df_score['score'].iloc[num] = ev
        df_score['len_winning_count'].iloc[num] = len_of_winning_counts
        df_score['avarage_score_per_number'].iloc[num] = ev/len_of_winning_counts
    return df_score

def get_df_list_score_for_list_df_random_wheels(list_of_random_df):
    list_of_random_wheels_scores = []
    for wheel_df in list_of_random_df:
        df_score_for = get_df_score_for_df_wheels(wheel_df)
        list_of_random_wheels_scores.append(df_score_for)
    return list_of_random_wheels_scores

def calculate_ev(sektor, max_sum_sektor, number_of_spins):
    number_of_lost_spins = number_of_spins - max_sum_sektor
    total_win = max_sum_sektor * 35
    total_loose =  number_of_lost_spins * (sektor+1)
    diff_total_win_loose = total_win - total_loose
    additional_loose = sektor * max_sum_sektor
    diff_total_win_loose = diff_total_win_loose - additional_loose

    obrot = number_of_spins * (sektor+1)
    ev = diff_total_win_loose/obrot
    print('')
    return ev

