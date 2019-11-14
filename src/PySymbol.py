# PySymbol.py
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
import StkMktPaths
import CreateDict
import requests
import copy
import json
import csv
import sys


class PySymbol:
    def __init__(self, force_update=False):
        self.cd = CreateDict.CreateDict()
        self.spath = StkMktPaths.StkMktPaths()
        self.load_symbols(force_update)
        self.convert_to_json(force_update)
        self.load_json()

    def load_symbols(self, force_update):
        for market, info in self.spath.symbols.items():
            if force_update or not info['filename'].exists():
                self.get_file(info['url'], info['filename'], force_update)

    def convert_to_json(self, force_update):
        for market, info in self.spath.symbols.items():
            if force_update or not info['json_filename'].exists():
                self.convert_csv_to_json(info['filename'], 
                    info['json_filename'], info['dictname'], force_update)

    def get_file(self, url, savefile, force_update):
        if force_update or not savefile.exists():
            response = requests.get(url)
            if response.status_code == 200:
                with savefile.open('wb') as fp:
                    fp.write(response.content)
            else:
                print(f"Download failed for {url} with ststus_code " \
                    f"{response.status_code}")
                sys.exit(0)

    def load_symbols(self, force_update):
        for market, info in self.spath.symbols.items():
            if force_update or not info['filename'].exists():
                self.get_file(info['url'], info['filename'], 
                    info['json_filename'])

    def convert_csv_to_json(self, csvfile, jsonfile, dictionary, force_update):
        odict = {}
        if force_update or not jsonfile.exists():
            symbolid = 1
            with csvfile.open() as fp:
                crdr = csv.DictReader(fp)
                for row in crdr:
                    odict[symbolid] = row
                    symbolid += 1
            with jsonfile.open('w') as fp:
                json.dump(odict, fp)

    def load_json(self):
        for market, data in self.spath.symbols.items():
            filename = data['json_filename']
            xdict = data['dictname']
            with filename.open() as fp:
                xdict = json.load(fp)
            for key in xdict.keys():
                company = xdict[key]['Name']
                symbol = xdict[key]['Symbol']
                self.cd.add_cell(data['companies'], company, symbol)
                self.cd.add_cell(data['symbols'], symbol, company)

    def Lookup(self, market, company_name=None, ticker=None):
        if company_name is not None:
            return self.spath.symbols[market]['companies'][company_name]
        elif ticker is not None:
            return self.spath.symbols[market]['symbols'][ticker]
        return None

def main():
    sy = PySymbol()
    # Lookup by company name
    symbol = sy.Lookup('NYSE', company_name='Niagara Mohawk Holdings, Inc.')
    print(f"\nThe NYSE stock symbol for Niagara Mohawk Holdings, Inc. " \
        f"is {symbol} ")

    # Lookup by Symbol
    company = sy.Lookup('NASDAQ', ticker='BFST')
    print(f"\nThe NASDAQ company name for symbol BFST is {company}")


if __name__ == '__main__':
    main()
