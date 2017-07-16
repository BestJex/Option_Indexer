import csv

# with open('./nothing/m1709c2500.csv') as f_1:
#     data_1 = csv.DictReader(f_1)
# with open('./nothing/m1709c2600.csv') as f_2:
#     data_2 = csv.DictReader(f_2)


def get_first_rate_list():
    with open('./nothing/m1709c2500.csv') as f_1:
        data_1 = csv.DictReader(f_1, delimiter=";")
        return [float(x["vol"]) for x in data_1]


def get_second_rate_list():
    with open('./nothing/m1709c2600.csv') as f_2:
        data_2 = csv.DictReader(f_2, delimiter=";")
        return [float(x["vol"]) for x in data_2]


def get_first_price_list():
    with open('./nothing/m1709c2500.csv') as f_1:
        data_1 = csv.DictReader(f_1, delimiter=";")
        return [float(x["close"]) for x in data_1]


def get_second_price_list():
    with open('./nothing/m1709c2600.csv') as f_2:
        data_2 = csv.DictReader(f_2, delimiter=";")
        return [float(x["close"]) for x in data_2]


def get_data_list(time_start, time_end, code):
    pass

def get_rate_list(time_start, time_end, code):
    pass

def calc_cash_deposit(closing_price_yesterday_of_future, closing_price_yesterday_of_option, contracts_for_option,
                      exercise_price, is_call_option=True):
    contracts_for_future = 10 * contracts_for_option
    if is_call_option:
        out_of_the_money = max(exercise_price - closing_price_yesterday_of_future, 0)
        cash_deposit_1 = closing_price_yesterday_of_option + closing_price_yesterday_of_future * 0.07 - 0.5 * out_of_the_money
        cash_deposit_1 *= contracts_for_future
        cash_deposit_2 = closing_price_yesterday_of_option + 0.5 * closing_price_yesterday_of_future * 0.07
        cash_deposit_2 *= contracts_for_future
        cash_deposit_of_option = max(cash_deposit_1, cash_deposit_2)
        cash_deposit_of_future = closing_price_yesterday_of_future * 0.07 * contracts_for_future
        return cash_deposit_of_option + cash_deposit_of_future
    else:
        out_of_the_money = max(closing_price_yesterday_of_future - exercise_price, 0)
        cash_deposit_1 = closing_price_yesterday_of_option + closing_price_yesterday_of_future * 0.07 - 0.5 * out_of_the_money
        cash_deposit_1 *= contracts_for_future
        cash_deposit_2 = closing_price_yesterday_of_option + 0.5 * closing_price_yesterday_of_future * 0.07
        cash_deposit_2 *= contracts_for_future
        cash_deposit_of_option = max(cash_deposit_1, cash_deposit_2)
        cash_deposit_of_future = closing_price_yesterday_of_future * 0.07 * contracts_for_future
        return cash_deposit_of_option + cash_deposit_of_future