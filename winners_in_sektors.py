import pandas as pd
import sektors_stats


def calculate_winner(my_wheels_df, list_random_wheels_dfs):

    print('')
def change_dicts_for_dfs(model):
    my_wheels_df = model.my_wheels_as_df

    '''list3 of list10 of dict33'''
    avg_scores_win_nums_in_sektor_randoms = model.avg_score_wins_num_in_randoms_sektor
    list_of_random_dfs_avg_scores_win_nums_in_sektor_randoms = change_single_dict_for_df(avg_scores_win_nums_in_sektor_randoms, my_wheels_df)
    print('')

    '''list3 of list10 of dict33'''
    len_win_nums_in_sektor_randoms = model.len_win_nums_in_randoms_sektor


    '''list3 of dict33'''
    avg_score_win_nums_in_sektor_my_wheels = model.avg_score_wins_num_in_sektor
    '''list3 of dict33'''
    len_win_nums_in_sektor_my_wheels = model.len_win_nums_in_sektor
    print('')



def change_single_dict_for_df(avg_scores_win_nums_in_sektor_randoms, my_wheels_df):
    list_of_df = []
    for element in avg_scores_win_nums_in_sektor_randoms:
        df = pd.DataFrame(element)
        list_of_df.append(df)
        # df.set_index(my_wheels_df.index, inplace=True)
    return list_of_df

