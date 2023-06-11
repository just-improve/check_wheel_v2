import creator_random_wheels
from roullete_tests import make_tests
from plots_data_representations import df_to_html
import score_stats
import comparator
import sektors_stats
import winners_in_sektors
import show_sektors
import n_best_winners

class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self):
        self.frame.create_random_wheels_btn.config(command=self.create_random_wheels)
        self.frame.make_tests_for_my_wheels.config(command=self.display_tests_my_wheels)
        self.frame.make_score_stats.config(command=self.display_score_stats_my_wheels)
        self.frame.show_score_among_wheels.config(command=self.display_score_among_wheels)
        self.frame.make_sektors_stats_btn.config(command=self.make_sektors_stats_my_wheels)
        self.frame.winners_in_sektors_stats_btn.config(command=self.calulate_winners_in_sektors)
        self.frame.n_best_winners_btn.config(command=self.calculate_best_n_numbers)
        self.frame.find_sektor_for_wheel_btn.config(command=self.show_sektor)

    def create_random_wheels(self):
        # amount_of_random_wheels = 100
        entry_amount_of_random_wheels = int(self.frame.entry_amount_random_wheels.get())
        # print('')
        self.model.my_wheels_as_df = creator_random_wheels.get_my_wheels_from_files_as_df()
        self.model.list_of_random_df_wheels = creator_random_wheels.get_list_of_random_df_wheels(self.model.my_wheels_as_df, entry_amount_of_random_wheels)

    def display_tests_my_wheels(self):
        self.model.my_wheels_as_df = creator_random_wheels.get_my_wheels_from_files_as_df()
        my_df_stats = make_tests(self.model.my_wheels_as_df)
        df_to_html(my_df_stats, 'Tests for my wheels')

    def display_score_stats_my_wheels(self):
        self.model.my_df_score = score_stats.get_df_score_for_df_wheels(self.model.my_wheels_as_df)
        df_to_html(self.model.my_df_score, 'Score winning numbers for my wheels')

    def display_score_among_wheels(self):
        df_score_among_random_wheels = score_stats.get_df_list_score_for_list_df_random_wheels(self.model.list_of_random_df_wheels)
        list_my_score_wheel_with_randoms = comparator.get_list_of_connected_my_wheel_with_randoms_wheel_dfs(self.model.my_df_score, df_score_among_random_wheels)
        df_score_stats_among_randoms = comparator.get_dict_of_sektors_position_among_randoms_wheels(list_my_score_wheel_with_randoms, self.model.my_df_score)
        df_to_html(df_score_stats_among_randoms, f'Score winning numbers among random {len(self.model.list_of_random_df_wheels[0])} wheels ')

    def make_sektors_stats_my_wheels(self):
        self.model.my_wheels_as_df = creator_random_wheels.get_my_wheels_from_files_as_df()
        # score_setter = int(self.frame.entry_score_setter.get())
        # print('')
        self.model.my_wheels_sektor_stats, self.model.my_wheels_sektor_indexes, self.model.len_win_nums_in_sektor, \
        self.model.avg_score_wins_num_in_sektor, self.model.sum_score_wins_num_in_sektor, self.model.real_roullete_value_my_wheels = \
            sektors_stats.get_df_sektor_stats(self.model.my_wheels_as_df)

        # print('')
        self.model.random_wheels_sektor_stats, self.model.random_wheels_sektor_indexes, \
        self.model.len_win_nums_in_randoms_sektor, self.model.avg_score_wins_num_in_randoms_sektor, self.model.sum_score_wins_num_in_randoms_sektor, self.model.list_real_roullete_value_randoms \
            = sektors_stats.get_list_sektors_stats_for_random_wheels(self.model.my_wheels_sektor_stats, self.model.list_of_random_df_wheels)

        list_sektors_my_wheels_with_randoms = comparator.get_list_of_connected_my_wheel_with_randoms_wheel_dfs(self.model.my_wheels_sektor_stats, self.model.random_wheels_sektor_stats)
        df_sektors_stats_among_randoms_sektors = comparator.get_dict_of_sektors_position_among_randoms_wheels(list_sektors_my_wheels_with_randoms, self.model.my_wheels_sektor_stats)

        df_to_html(self.model.my_wheels_sektor_stats, f'Sectors stats my wheels ')
        df_to_html(df_sektors_stats_among_randoms_sektors, f'Sectors position among random {len(self.model.list_of_random_df_wheels[0])} wheels ')

    def calculate_best_n_numbers(self):
        self.model.my_wheels_best_n_numbers, list_df_best_n_numbers_for_random_wheels = n_best_winners.n_nest_winners_calc(self.model)

        list_best_n_numbers_my_wheels_with_randoms = comparator.get_list_of_connected_my_wheel_with_randoms_wheel_dfs(
            self.model.my_wheels_best_n_numbers, list_df_best_n_numbers_for_random_wheels)

        df_best_n_numbers_among_randoms_sektors = comparator.get_dict_of_sektors_position_among_randoms_wheels(
            list_best_n_numbers_my_wheels_with_randoms,  self.model.my_wheels_best_n_numbers)

        df_to_html(self.model.my_wheels_best_n_numbers, f'my_wheels_best_n_numbers avg_score')
        df_to_html(df_best_n_numbers_among_randoms_sektors, f'df_best_n_numbers_among_randoms_{len(self.model.list_of_random_df_wheels[0])} wheels ')
        # df_to_html(list_df_best_n_numbers_for_random_wheels, f' list_df_best_n_numbers_for_random_wheels ')

        # print('')

    def calulate_winners_in_sektors(self):
        list_avg_scores_in_sektors_my_wheels_with_randoms = comparator.get_list_of_connected_my_wheel_with_randoms_wheel_dfs(
            self.model.avg_score_wins_num_in_sektor, self.model.avg_score_wins_num_in_randoms_sektor)
        df_avg_score_among_randoms_sektors = comparator.get_dict_of_sektors_position_among_randoms_wheels(
            list_avg_scores_in_sektors_my_wheels_with_randoms, self.model.avg_score_wins_num_in_sektor)
        df_to_html(df_avg_score_among_randoms_sektors, f'df_avg_score_among_randoms_{len(self.model.list_of_random_df_wheels[0])} wheels ')


        len_win_nums_in_sektors_my_wheels_with_randoms = comparator.get_list_of_connected_my_wheel_with_randoms_wheel_dfs(
            self.model.len_win_nums_in_sektor, self.model.len_win_nums_in_randoms_sektor)
        df_len_win_nums_among_randoms_sektors = comparator.get_dict_of_sektors_position_among_randoms_wheels(
            len_win_nums_in_sektors_my_wheels_with_randoms, self.model.len_win_nums_in_sektor)

        df_to_html(self.model.len_win_nums_in_sektor,
                   f' My wheels len win nums in  sektor ')
        df_to_html(df_len_win_nums_among_randoms_sektors,
                   f' len_win_nums in sektors _among_randoms _{len(self.model.list_of_random_df_wheels[0])} wheels ')


        sum_score_nums_in_sektors_my_wheels_with_randoms = comparator.get_list_of_connected_my_wheel_with_randoms_wheel_dfs(
            self.model.sum_score_wins_num_in_sektor, self.model.sum_score_wins_num_in_randoms_sektor)
        df_sum_score_win_nums_among_randoms_sektors = comparator.get_dict_of_sektors_position_among_randoms_wheels(
            sum_score_nums_in_sektors_my_wheels_with_randoms, self.model.sum_score_wins_num_in_sektor)

        df_to_html(self.model.sum_score_wins_num_in_sektor,
                   f'My wheels sum_score_wins_num_in_sektors ')

        df_to_html(df_sum_score_win_nums_among_randoms_sektors,
                   f'sum_score_win_nums_among_randoms_sektors_{len(self.model.list_of_random_df_wheels[0])} wheels ')

    def show_sektor(self):
        show_sektors.display_sektor(self.frame, self.model)

