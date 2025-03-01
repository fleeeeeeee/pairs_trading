
from datetime import datetime

import pandas as pd
from pandas import DatetimeIndex

from utils.convert_date import convert_date


def findDateIndex(date_index: DatetimeIndex, search_date: datetime) -> int:
    """
    In a DatetimeIndex, find the index of the date that is nearest to search_date.
    This date will either be equal to search_date or the next date that is less than
    search_date
    """
    i = 0
    search_date = convert_date(search_date)
    date_t = datetime.today()
    for i in range(0, len(date_index)):
        if type(date_index) == pd.Series:
            date_val = date_index.iloc[i]
        else:
            date_val = date_index[i]
        date_t = convert_date(date_val)
        if date_t >= search_date:
            break
    if date_t > search_date:
        index = i - 1
    else:
        index = i
    return index
