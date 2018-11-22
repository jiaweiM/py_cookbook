stocks = {
    'GOOG': 500.35,
    'FB': 75.76,
    'YHOO': 35.43,
    'AMZN': 369.32,
    'AAPL': 99.79
}
# Sorts numerically
print(sorted(zip(stocks.values(), stocks.keys())))

# Sorts alphabetically
print(sorted(zip(stocks.keys(), stocks.values())))

# Grabs minimum number
print(min(zip(stocks.values(), stocks.keys())))

# Grabs maximum number
print(max(zip(stocks.values(), stocks.keys())))
