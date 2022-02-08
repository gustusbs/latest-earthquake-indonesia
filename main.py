"""
Detection the latest earthquake in Indonesia
"""

import dataoflatestearthquakeindonesia

if __name__ == '__main__':
    print('Latest Earthquake in Indonesia')
    result = dataoflatestearthquakeindonesia.extract_data()
    dataoflatestearthquakeindonesia.show_data(result)