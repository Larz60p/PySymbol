from distutils.core import setup
setup(
  name = 'PySymbol',         # How you named your package folder (MyLib)
  packages = ['PySymbol'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'US Stock Market Symbol/Company lookup',   # Give a short description about your library
  author = 'Larz60+',                   # Type in your name
  author_email = 'larry@pypython.com',      # Type in your E-Mail
  url = 'https://github.com/Larz60p/PySymbol',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Larz60p/PySymbol',    # I explain this later on
  keywords = ['Stock', 'Symbol', 'Ticker', 'Company'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
          'requests',
          'lxml'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)
