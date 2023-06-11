import pandas as pd

def get_df_sektor_stats(df):
    list_of_dict_sektors_ratio = []
    list_of_dict_of_indexes_sektors = []
    list_of_dict_len_win_numb_in_sekt = []   #trzeba pomyśleć jak to zwrócić czy jako list of dict czy jako dataframe chyba jako dataframe ponieważ później będzie możńa komparatorem porównać
    list_of_dict_avg_score_win_numbrs_in_sekt = []
    list_of_dict_sum_score_win_numbrs_in_sekt = []
    list_of_double_real_roullete_value = []
    for numd_df in range(len(df)):
        sum_df = df.iloc[numd_df].sum()
        real_roullete_value = get_real_roullete_value_df_0_32(df,numd_df)
        double_real_roullete_value = real_roullete_value * 2
        iterations = 37
        max_sektor = 33
        dict_of_max_sectors = {}
        dict_of_indexes_sektors = {}
        dict_of_len_win_numbers_in_sektor = {}
        dict_of_avg_score_win_numbers_in_sektor = {}
        dict_of_sum_score_win_numbers_in_sektor = {}
        for sektor in range(max_sektor):
            max_sum_sektor = 0
            index1_max_sum_sektor = -1
            index2_max_sum_sektor = -1
            for num_iter in range(iterations):
                sum_of_current_sektor, index1, index2 = get_sum_of_current_sektor(double_real_roullete_value, sektor, num_iter)
                if sum_of_current_sektor > max_sum_sektor:
                    max_sum_sektor = sum_of_current_sektor
                    index1_max_sum_sektor = index1
                    index2_max_sum_sektor = index2

            ev = calculate_ev(sektor, max_sum_sektor,sum_df)
            dict_of_max_sectors[sektor+1] = ev
            dict_of_indexes_sektors[sektor + 1] = [index1_max_sum_sektor, index2_max_sum_sektor]

            # abstrakcja
            len_win_numbers_in_sektor = calculate_len_win_numbers_in_sektor(sektor, index1_max_sum_sektor, index2_max_sum_sektor, double_real_roullete_value)
            avg_score_win_numbers_in_sektor_in_sektor = calculate_avg_score_win_numbers_in_sektor(sektor, index1_max_sum_sektor, index2_max_sum_sektor, double_real_roullete_value)
            sum_score_win_numbers_in_sektor_in_sektor = calculate_sum_score_win_numbers_in_sektor(sektor, index1_max_sum_sektor, index2_max_sum_sektor, double_real_roullete_value)
            print('')
            dict_of_len_win_numbers_in_sektor[sektor+1] = len_win_numbers_in_sektor
            dict_of_avg_score_win_numbers_in_sektor[sektor+1] = avg_score_win_numbers_in_sektor_in_sektor
            dict_of_sum_score_win_numbers_in_sektor[sektor+1] = sum_score_win_numbers_in_sektor_in_sektor
            # abstrakcja

        dict_of_max_sectors[34] = sum_df
        list_of_dict_sektors_ratio.append(dict_of_max_sectors)
        list_of_dict_of_indexes_sektors.append(dict_of_indexes_sektors)

        list_of_dict_len_win_numb_in_sekt.append(dict_of_len_win_numbers_in_sektor)
        list_of_dict_avg_score_win_numbrs_in_sekt.append(dict_of_avg_score_win_numbers_in_sektor)
        list_of_dict_sum_score_win_numbrs_in_sekt.append(dict_of_sum_score_win_numbers_in_sektor)
        list_of_double_real_roullete_value.append(double_real_roullete_value)

    final_df_of_sektors_ratio = pd.DataFrame(list_of_dict_sektors_ratio, columns=list(range(1,35))) #wiaderny
    final_df_of_sektors_ratio.set_index(df.index, inplace=True)
    final_df_of_sektors_ratio.rename(columns={34: 'count'}, inplace=True) #wiaderny
    column_order = ['count', 1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
    final_df_of_sektors_ratio = final_df_of_sektors_ratio[column_order]

    df_len_win_numb_in_sekt = change_single_dict_for_df(list_of_dict_len_win_numb_in_sekt, df)
    df_avg_score_numb_in_sekt = change_single_dict_for_df(list_of_dict_avg_score_win_numbrs_in_sekt, df)
    df_sum_score_numb_in_sekt = change_single_dict_for_df(list_of_dict_sum_score_win_numbrs_in_sekt, df)

    print('')

    return final_df_of_sektors_ratio, list_of_dict_of_indexes_sektors, df_len_win_numb_in_sekt, \
           df_avg_score_numb_in_sekt, df_sum_score_numb_in_sekt, list_of_double_real_roullete_value

def get_real_roullete_value_df_0_32(df, row_num):
    real_roullete_list = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
    kolo = df.iloc[row_num]
    real_roullete_value_df_0_32 = []
    for x in real_roullete_list:
        value_of_df = kolo[x]
        real_roullete_value_df_0_32.append(value_of_df)
    return real_roullete_value_df_0_32

def get_sum_of_current_sektor(kolo_double_real_value, sektor, nume_iter):
    index1 = nume_iter
    index2 = nume_iter+sektor+1
    sektor_to_sum_as_list = kolo_double_real_value[index1:index2]
    sum_of_sektor = sum(sektor_to_sum_as_list)

    return sum_of_sektor, index1, index2

def calculate_ev(sektor, max_sum_sektor, number_of_spins):
    number_of_lost_spins = number_of_spins - max_sum_sektor
    total_win = max_sum_sektor * 35
    total_loose =  number_of_lost_spins * (sektor+1)
    diff_total_win_loose = total_win - total_loose
    additional_loose = sektor * max_sum_sektor
    diff_total_win_loose = diff_total_win_loose - additional_loose

    obrot = number_of_spins * (sektor+1)
    ev = diff_total_win_loose/obrot
    return ev

def get_list_sektors_stats_for_random_wheels(my_wheels_df_sektors, list_of_random_wheels):
    iterations = range(len(my_wheels_df_sektors))
    list_of_df_sektor_stats_random_df_wheels = []
    indexes_sektors_for_random_wheels = []
    list_len_win_nums_in_random_sektor = []
    list_avg_score_wins_num_in_ranodm_sektor = []
    list_sum_score_wins_num_in_ranodm_sektor = []
    list_of_double_roullete_value = []
    for num in iterations:
        random_df_wheels = list_of_random_wheels[num]
        random_wheels_sektors, dict_of_indexes_random_sektors_stats, len_win_nums_in_sektor, \
        avg_score_wins_num_in_sektor, df_sum_score_numb_in_sekt, real_roullete_value = get_df_sektor_stats(random_df_wheels)

        list_of_df_sektor_stats_random_df_wheels.append(random_wheels_sektors)
        indexes_sektors_for_random_wheels.append(dict_of_indexes_random_sektors_stats)
        list_len_win_nums_in_random_sektor.append(len_win_nums_in_sektor)
        list_avg_score_wins_num_in_ranodm_sektor.append(avg_score_wins_num_in_sektor)
        list_sum_score_wins_num_in_ranodm_sektor.append(df_sum_score_numb_in_sekt)
        list_of_double_roullete_value.append(real_roullete_value)

    return list_of_df_sektor_stats_random_df_wheels, indexes_sektors_for_random_wheels, \
           list_len_win_nums_in_random_sektor, list_avg_score_wins_num_in_ranodm_sektor,list_sum_score_wins_num_in_ranodm_sektor, list_of_double_roullete_value

def calculate_len_win_numbers_in_sektor(sektor, index1_max_sum_sektor, index2_max_sum_sektor, double_real_roullete_value):
    sum_roullte = sum(double_real_roullete_value[0:37])
    sektor = sektor+1
    count_over_1_36 = sum_roullte/36
    badany_sektor = double_real_roullete_value[index1_max_sum_sektor:index2_max_sum_sektor]
    count = len([num for num in badany_sektor if num > count_over_1_36])
    list_of_winning_numbers = [num for num in badany_sektor if num > count_over_1_36]
    # print('')
    return count

def calculate_avg_score_win_numbers_in_sektor(sektor, index1_max_sum_sektor, index2_max_sum_sektor, double_real_roullete_value):
    sum_roullte = sum(double_real_roullete_value[0:37])
    sektor = sektor + 1
    count_over_1_36 = sum_roullte / 36
    badany_sektor = double_real_roullete_value[index1_max_sum_sektor:index2_max_sum_sektor]
    count = len([num for num in badany_sektor if num > count_over_1_36])
    list_of_winning_numbers = [num for num in badany_sektor if num > count_over_1_36]
    sum_winning_numbers = sum(list_of_winning_numbers)

    count_for_ev = count-1
    ev = calculate_ev(count_for_ev,sum_winning_numbers,sum_roullte)
    # print('')
    return ev

# wiaderny
def calculate_sum_score_win_numbers_in_sektor(sektor, index1_max_sum_sektor, index2_max_sum_sektor, double_real_roullete_value):
    sum_roullte = sum(double_real_roullete_value[0:37])
    sektor = sektor + 1
    count_over_1_36 = sum_roullte / 36
    badany_sektor = double_real_roullete_value[index1_max_sum_sektor:index2_max_sum_sektor]
    count = len([num for num in badany_sektor if num > count_over_1_36])
    list_of_winning_numbers = [num for num in badany_sektor if num > count_over_1_36]
    sum_winning_numbers = sum(list_of_winning_numbers)

    count_for_ev = count-1
    ev = calculate_ev_for_sum_win_numb_in_sektr(sektor, sum_winning_numbers, sum_roullte)   #dajemy tu sektor ponieważ chcemy mieć porównany sum wygranych do sektora a nie tylko do liczby wygranych
    print('')
    return ev

def change_single_dict_for_df(avg_score_win_nums_in_sektor_my_wheels, my_wheels_df):
    df = pd.DataFrame(avg_score_win_nums_in_sektor_my_wheels)
    df.set_index(my_wheels_df.index, inplace=True)
    return df

def calculate_ev_for_sum_win_numb_in_sektr(sektor, max_sum_sektor, number_of_spins):
    # sum_winning_numbers =
    # number_of_spins =
    # sektor_of_winning =

    number_of_lost_spins = number_of_spins - max_sum_sektor
    total_win = max_sum_sektor * 35
    total_loose =  number_of_lost_spins * (sektor+1)
    diff_total_win_loose = total_win - total_loose
    additional_loose = sektor * max_sum_sektor
    diff_total_win_loose = diff_total_win_loose - additional_loose

    obrot = number_of_spins * (sektor+1)
    ev = diff_total_win_loose/obrot
    return ev