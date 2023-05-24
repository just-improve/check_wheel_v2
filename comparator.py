import pandas as pd

def get_list_of_connected_my_wheel_with_randoms_wheel_dfs(my_df_wheels, random_list_dfs):
    iterations = range(len(my_df_wheels))
    my_wheel_score_with_random_scores = []
    for num in iterations:
        my_wheel_score = my_df_wheels.iloc[num]
        wheel_name = my_df_wheels.index[num]
        random_df_wheels_score = random_list_dfs[num]
        my_wheel_with_randoms = connect_my_wheel_with_random_wheels(my_wheel_score, random_df_wheels_score, wheel_name)
        my_wheel_score_with_random_scores.append(my_wheel_with_randoms)
    return my_wheel_score_with_random_scores

def connect_my_wheel_with_random_wheels(my_wheel_as_series_score, random_df_wheels, wheel_name):
    my_wheel_with_randoms = pd.concat([random_df_wheels, pd.DataFrame([my_wheel_as_series_score])], ignore_index=True)
    len_random_wheels_sektors = len(my_wheel_with_randoms) - 1
    my_wheel_with_randoms.rename(index={len_random_wheels_sektors: wheel_name}, inplace=True)
    return my_wheel_with_randoms

def get_dict_of_sektors_position_among_randoms_wheels(list_my_score_wheel_with_randoms, df_my_wheel_score):
    list_of_dicts = []
    for df_wheels in list_my_score_wheel_with_randoms:
        name_of_wheel = df_wheels.index[len(df_wheels) - 1]
        dict_of_position = {}
        for column in df_wheels.columns:
            if column == 'count':
                continue
            df_wheels = df_wheels.sort_values(column)
            row_number = df_wheels.index.get_loc(name_of_wheel)
            dict_of_position[column] = row_number
        list_of_dicts.append(dict_of_position)
    df_my_wheels_score_among_randoms = pd.DataFrame(list_of_dicts)
    df_my_wheels_score_among_randoms.set_index(df_my_wheel_score.index, inplace=True)
    return df_my_wheels_score_among_randoms