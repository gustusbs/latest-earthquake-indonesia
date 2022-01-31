"""
Detection the latest earthquake in Indonesia
"""

import data

if __name__ == '__main__':
    print('Latest Earthquake in Indonesia')
    result = data.extract_data()
    data.show_data(result)