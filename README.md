# S&P index prediction

## This is a final project I do for the Flatiron Data Science Immersive program 100719.

![alt test](https://github.com/rockinhumingbird/SP500_prediction/blob/master/nyt.jpeg)
### Data
- There are two sources of data provided in this dataset:

1. News Headline data: I called New York Times archive news API.
2. Stock data: S&P500 is used for prediction. (Range: 2010-01-01 to 2020-01-06)

### Procedure
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
- Sentiment analysis using Textblob, get the polarity score and subjectvity score
- Using technical indicators as external financial predictors
  1. Calculate open - close/open percentage 
  2. Calculate close- open/open percentage
  3. Open price with 1 day window
 
  4. Calculate relative index strengh: indexing overbought or oversold
  5. Calculate Moving Average convergence index which is a trading indicator used in technical analysis of stock prices,

## EDA
# The price of SP500 has been gradually climbing by annual trend.
![alt test](https://github.com/rockinhumingbird/SP500_prediction/blob/master/image/newplot%20(5).png)

$ Some EDA result using monthly data suggesting the inverse relationship between PE ratio and EPS, overall the price of SP500 went up the past 9 years, the EPS have starting to slightly slow down since 2019.
![alt test](https://github.com/rockinhumingbird/SP500_prediction/blob/master/image/newplot%20(8).png)

## Some results

correlation plot suggests that there is no strong corrleation between the sentiment score of the headlines on the prices.
![alt test](https://github.com/rockinhumingbird/SP500_prediction/blob/master/image/corrplot.png)

SARIMA seems to have the most accurate result.
![alt test](https://github.com/rockinhumingbird/SP500_prediction/blob/master/sarima.png)

![alt test](https://github.com/rockinhumingbird/SP500_prediction/blob/master/image/knn.png)

