from datetime import datetime


def filename_gen_fun(json: bool):
    while True:
        current_time = datetime.now()
        day = current_time.date().day
        month = current_time.date().month
        year = current_time.date().year
        current_date_filename = f'{day}_{month}_{year}'

        if json:
            yield current_date_filename + '.json'
        else:
            yield current_date_filename + '.txt'
