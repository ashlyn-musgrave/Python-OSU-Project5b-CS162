# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/21/2023
# Description: This program reads a JSON file containing data on Nobel Prizes and allows the user
# to search that data.

import json
class NobelData:
    """This class reads a JSON file containing data on Nobel Prizes and allows the user to search
    that data"""

    def __init__(self):
        """This method reads the file and stores it in a data member"""
        with open('nobels.json', 'r') as infile:
            self._data = json.load(infile)

    def search_nobel(self, year, category):
        """This method takes as parameters a year and a category, and returns a sorted list
        of the surnames for the winner(s) in that category for that year"""
        a = len(self._data['prizes'])
        winners = []
        for i in range(0, a):
            if self._data['prizes'][i]['year'] == year and self._data['prizes'][i]['category'] == category:
                winners = self._data['prizes'][i]['laureates']
                break
        b = len(winners)
        winner_sur = []
        for i in range(0, b):
            winner_sur.append(winners[i]['surname'])
        winner_sur.sort()
        return winner_sur

nd = NobelData()
winner_sur = nd.search_nobel("2001", "economics")
print(winner_sur)

surnames = ["chemistry", 'economics', 'literature', 'peace', 'physics', 'medicine']

