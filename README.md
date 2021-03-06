# Trading Playground

This project allows user to experiment with various investment strategies.

The project is split into these sections:
- trading data
- utility scripts
- investment framework
- investing models

## Trading Data
We store CSV files for several Exchange Traded Funds, or any other trading series.
The CSVs are organised using `date,price` format. The data is sorted chronologically.
We are mostly interested in price data series and its prediction.

## Utility Scripts
This is a collections of scripts to provide useful functionality that is not directly used in the investment framework.
These can be:
- populate trading data from the Internet
- plot data series

### TODO
- automate the process of getting/refreshing data

### DONE
- query the Internet for the trading data
- extract price and date series from the internet data
- Store internet data into `trading_data` folder in the correct CSV format
- plot price series in individual figures

## Investment Framework
Run a trading simulation using a selection of trading data and a prediction model.
Plot profits and losses over time for comparison of different trading strategies.

### TODO
- create simulation skeleton
### DONE

## Investing Models
Code and Data for price prediction model.
This includes training framework and prediction framework.
Some models are simplistic and do no require any model data to be stored.
Some models are complex deep learning architectures that are trained prior to any prediction.
Trained models might share model architectures and only differ in hyperparameters used during training.
 
### TODO
- design model interface
- create simple models for testing
### DONE