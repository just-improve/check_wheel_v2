import glob
import os
import pandas as pd
import numpy as np

def get_all_xlsx_names_from_p_dir()-> list[str]:
    names_csv_files = glob.glob('my_wheels/*xlsx')
    names_csv_files = [os.path.basename(file) for file in names_csv_files]
    # names_csv_files: list = glob.glob('*xlsx')
    return names_csv_files

def get_my_wheels_from_files_as_df():
    files_names = get_all_xlsx_names_from_p_dir()
    df = pd.DataFrame(columns=range(37))
    folder = r'my_wheels\\'
    for wheel_name in files_names:
        moje_kolo = pd.read_excel(folder+wheel_name)
        moje_kolo = moje_kolo.transpose()
        moje_kolo.columns = moje_kolo.iloc[0]
        moje_kolo = moje_kolo.drop(['roullete_numbers'])
        moje_kolo = moje_kolo.iloc[:, -1:].join(moje_kolo.iloc[:, :-1])
        moje_kolo = moje_kolo.rename(index={'count': wheel_name})
        df = pd.concat([df, moje_kolo])
        print('')

    return df

def get_list_of_random_df_wheels(my_df_wheels, amount_wheels_to_generate):
    iterations = range(len(my_df_wheels))
    list_of_random_df_wheels = []
    for num in iterations:
        wheel_spin_sum = my_df_wheels.iloc[num].sum()
        print('')
        random_wheels_for_single_wheel = get_random_df_wheels(amount_wheels_to_generate, wheel_spin_sum)
        list_of_random_df_wheels.append(random_wheels_for_single_wheel)
    return list_of_random_df_wheels

def get_random_df_wheels(amount_of_wheels, number_of_spins):
    count = 0
    df = pd.DataFrame(columns=range(37))
    while amount_of_wheels > count:
        count += 1
        arr = np.random.randint(0, 37, number_of_spins)
        counts = np.bincount(arr, minlength=37)
        df.loc[len(df)] = counts
    return df