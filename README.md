# PySymbol
Yet another Stock Market Symbol class

The following class can be used to get company name from symbol and vice/versa

before running first time, make sure you are connected to the internet, after that, it's only requires if an update is requested.

when first run it will create the data directory structure tree will then look like

```
├── data
│   ├── csv
│   │   ├── AMEX_symbols.csv
│   │   ├── NASDAQ_symbols.csv
│   │   └── NYSE_symbols.csv
│   ├── excel
│   └── json
│       ├── AMEX_symbols.json
│       ├── NASDAQ_symbols.json
│       └── NYSE_symbols.json
├── requirements.txt
└── src
    ├── __init__.py
    ├── CreateDict.py
    ├── __pycache__
    │   ├── CreateDict.cpython-38.pyc
    │   ├── PySymbol.cpython-38.pyc
    │   ├── StkMktPaths.cpython-38.pyc
    │   └── Symbols.cpython-38.pyc
    ├── PySymbol.py
    ├── StkMktPaths.py
    └── TrySymbolFetch.py
```

Setup:
* clone application: git clone https://github.com/Larz60p/PySymbol
* cd to PySymbol
* Create virtual environment: python -m venv venv
* Activate virtual environment: . ./venv/bin/activate
* With internet access update environment: pip install -r requirements.txt
* From PySymbol directory, run application to get current symbol files: python src/PySymbol.py

To use class in application: see (and run if you wish) src/TrySymbolFetch.py
```
To run interactively:
>>> import PySymbol
>>> sym = PySymbol.PySymbol()
>>> lookup = sym.Lookup
>>> lookup('NYSE', company_name='Raytheon Company')
'RTN'
>>> lookup('NYSE', ticker='RTN')
'Raytheon Company'
>>>
```
Enjoy.

