from sektors_stats import change_single_dict_for_df
from sektors_stats import calculate_ev
def n_nest_winners_calc(model):
    my_wheels = model.my_wheels_as_df
    random_wheels = model.my_wheels_as_df
    my_wheels_best_n_numbers = get_df_best_n_numbers_for_df_wheels(my_wheels)
    list_df_best_n_numbers_for_random_wheels = get_df_best_n_numbers_for_random_wheels(my_wheels_best_n_numbers, model.list_of_random_df_wheels)
    return my_wheels_best_n_numbers, list_df_best_n_numbers_for_random_wheels

def get_df_best_n_numbers_for_df_wheels(df_wheels):
    list_of_dict_of_n_best_numbers = []
    for wheel_num in range(len(df_wheels)):
        dict_of_n_best_numbers_for_wheel = {}

        row = df_wheels.iloc[wheel_num]
        sum_of_wheel = sum(row)
        row = row.astype(int)
        for num in range(1, 33):   #2-9
            largest = row.nlargest(num).values
            sum_of_largest = sum(largest)
            ev = calculate_ev_nbest_winners(num, sum_of_largest, sum_of_wheel)
            dict_of_n_best_numbers_for_wheel[num] = ev
            # print('')
        list_of_dict_of_n_best_numbers.append(dict_of_n_best_numbers_for_wheel)
    df = change_single_dict_for_df(list_of_dict_of_n_best_numbers, df_wheels)
    return df

def calculate_ev_nbest_winners(n_numbers, sum_of_winning_spins, number_of_spins):
    number =36/n_numbers
    ev = (number*sum_of_winning_spins-number_of_spins)/number_of_spins
    return ev

def get_df_best_n_numbers_for_random_wheels(my_wheels_n_best_numbers, list_of_random_wheels):
    iterations = range(len(my_wheels_n_best_numbers))
    list_of_random_df_wheels_best_n_numbers = []
    for num in iterations:
        random_df_wheels = list_of_random_wheels[num]
        random_wheels_best_n_numbers = get_df_best_n_numbers_for_df_wheels(random_df_wheels)
        list_of_random_df_wheels_best_n_numbers.append(random_wheels_best_n_numbers)
    return list_of_random_df_wheels_best_n_numbers

