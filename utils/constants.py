



NOW = 0
FIVE_MINUTES = 60 * 5
FIFTEEN_MINUTES = FIVE_MINUTES * 3
HALF_HOUR = FIFTEEN_MINUTES * 2
HOUR = HALF_HOUR * 2
TWO_HOUR = HOUR * 2
FOUR_HOUR = HOUR * 4
DAY = HOUR * 24
YEAR = DAY * 365


COINS = [ "BTC-USD", "ETH-USD", "ADA-USD",
                  "DOGE-USD",  "SOL-USD", "DOT-USD",
                  "LTC-USD","CRO-USD"]
FEATURES = ["low", "high", "open", "close", "volume"]
NUM_ASSETS = len(COINS)
NUM_FEATURES = 3