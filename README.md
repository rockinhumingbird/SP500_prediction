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

- Merge stock indices price with headlines each day

- Storing (pickling) the data

- Feature engineering

- Modeling


### Task
Predicting stock price, adding text features using NLP techniques.

Approach
Combinations of a variety of strategies:
- Sentiment analysis using Textblob, get the polarity score and subjectvitity score
- Using technical indicators as external financial predictors
  1. Calculate open - close/open percentage 
  2. Calculate close- open/open percentage
  3. Open price with 1 day window
  4.  Monthly data such S&P P/E ratio, S&P earning per share, S&P dividend yield.
  5. Calculate relative index strengh: indexing overbought or oversold
  6. Calculate Moving Average convergence index which is a trading indicator used in technical analysis of stock prices,

