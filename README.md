# S&P index prediction
This is a final project I do for the Flatiron Data Science Immersive program 100719.

![alt test](https://github.com/rockinhumingbird/SP500_prediction/blob/master/nyt.jpeg)
### Data
- There are two sources of data provided in this dataset:

1. News Headline data: I called New York Times archive news API.
2. Stock data: S&P500 is used for prediction. (Range: 2010-01-01 to 2020-01-06)

## Procedure
- Headlines Filtering:
  Sections included: 'Business', 'National', 'World', 'U.S.' , 'Politics', 'Opinion', 'Tech', 'Science',  'Health' and 'Foreign‘.

- Merge stock indices price with articles
- Storing (pickling) the data

- Calculate open - close/open percentage 

- Calculate close- open/open percentage

- Get investor sentiments from American Investor Assoication using Quandl: 
- Get monthly data such S&P P/E ratio, S&P earning per share, S&P dividend yield.


### Task
Predicting stock price, adding text features using NLP techniques.

Approach
Combinations of a variety of strategies:
