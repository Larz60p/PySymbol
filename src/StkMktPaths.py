# StkMktPaths.py
#
# License:
#
# Copyright <2019> <Larz60+>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#
# Author: Larz60+ (c) November 2019
#
import os
from pathlib import Path


class StkMktPaths:
    def __init__(self):
        os.chdir(os.path.abspath(os.path.dirname(__file__)))

        self.dicts = {
            'NASDAQ': {},
            'AMEX': {},
            'NYSE': {},
        }


        self.homepath = Path('.')
    
        self.rootpath = self.homepath / '..'
        
        self.datapath = self.rootpath / 'data'
        self.datapath.mkdir(exist_ok=True)

        self.csvpath = self.datapath / 'csv'
        self.csvpath.mkdir(exist_ok=True)

        self.excelpath = self.datapath / 'excel'
        self.excelpath.mkdir(exist_ok=True)

        self.jsonpath = self.datapath / 'json'
        self.jsonpath.mkdir(exist_ok=True)

        self.symbols = {
            'NASDAQ': {
                'url': 'https://old.nasdaq.com/screening/companies-by-name.' \
                    'aspx?letter=0&exchange=nasdaq&render=download',
                'filename': self.csvpath / 'NASDAQ_symbols.csv',
                'json_filename': self.jsonpath / 'NASDAQ_symbols.json',
                'dictname': self.dicts['NASDAQ'],
                'companies': {},
                'symbols': {}

            },
            'AMEX': {
                'url': 'https://old.nasdaq.com/screening/companies-by-name.' \
                    'aspx?letter=0&exchange=amex&render=download',
                'filename': self.csvpath / 'AMEX_symbols.csv',
                'json_filename': self.jsonpath / 'AMEX_symbols.json',
                'dictname': self.dicts['AMEX'],
                'companies': {},
                'symbols': {}
            },
            'NYSE': {
                'url': 'https://old.nasdaq.com/screening/companies-by-name.' \
                    'aspx?letter=0&exchange=nyse&render=download',
                'filename': self.csvpath / 'NYSE_symbols.csv',
                'json_filename': self.jsonpath / 'NYSE_symbols.json',
                'dictname': self.dicts['NYSE'],
                'companies': {},
                'symbols': {}
            }
        }

if __name__ == '__main__':
    StkMktPaths()
