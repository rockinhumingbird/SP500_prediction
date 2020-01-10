# NYT_stocks

This is a final project I do for the Flatiron Data Science Immersive program 100719.


### Data
- There are two sources of data provided in this dataset:
News data: I called New York Times archive news API.
Stock data: S&P500 is used for prediction. (Range: 2010-01-01 to 2020-01-06)

## Procedure
- Articles Filtering:
  Sections included: 'Business', 'National', 'World', 'U.S.' , 'Politics', 'Opinion', 'Tech', 'Science',  'Health' and 'Foreign‘
    - Approximately 400,000 articles selected from 1 Million articles.

- Merge stock indices price with articles
- Storing (pickling) the data

- Calculate open - close/open percentage 

- Calculate close- open/open percentage



### Task
Predicting stock price, adding text features using NLP techniques.

Approach
Combinations of a variety of strategies:

- 
- Some classifiers on classifying increase or decrease, using positive and negative scores + historical price
