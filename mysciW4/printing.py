def print_comparison(name, dates, times, original_data, computed_data):
    """
    print a comparision of two time series (original and computed)

    parameter:
      name: a string name for the data being comparedi(Limited to 9 characters in length)
      date: List of strings represnting dates for each data
      times: List of strings representing times for each data
      original_data: List of original data (floats)
      computed_data: List of computed data(floats)

    """
    # output comparision data
    print('              ORIGINAL   COMPUTED')
    print(f' DATE   TIME  {name.upper():>9}  {name.upper():>9}  DIFFERENCE')
    print('------- ------ --------- --------- ----------')

    zip_data = zip(dates, times, original_data, computed_data)
    for date, time, orig, comp in zip_data:
        diff = orig - comp
        print(f'{date} {time:>6} {orig:9.6f} {comp:9.6f} {diff:10.6f}')

