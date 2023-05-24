
def display_sektor(frame, model):
    entry_from_user = frame.entry_sektor_finder.get()
    list_of_entry_words = entry_from_user.split()
    row_position = model.my_wheels_as_df.index.get_loc(list_of_entry_words[0])
    value = model.my_wheels_sektor_indexes[row_position][int(list_of_entry_words[1])]
    real_roullete_list = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
    searched_sektor = real_roullete_list[value[0]: value[1]]
    print(searched_sektor)
