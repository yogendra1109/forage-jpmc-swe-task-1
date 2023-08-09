import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
            # Test calculations for each quote
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            
            # Assert expected values based on the provided quote data
            self.assertEqual(stock, quote['stock'])
            self.assertEqual(bid_price, float(quote['top_bid']['price']))
            self.assertEqual(ask_price, float(quote['top_ask']['price']))
            self.assertEqual(price, (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2)

    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
      # Test calculations for each quote
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            
            # Assert bid price is greater than ask price
            self.assertGreater(bid_price, ask_price)
    """ ------------ Add the assertion below ------------ """

   def test_getDataPoint_zeroAskPrice(self):
        quote = {'top_ask': {'price': 0, 'size': 0}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'XYZ'}
        
        # Test calculation when ask price is 0
        stock, bid_price, ask_price, price = getDataPoint(quote)
        
        # Assert expected values based on the provided quote data
        self.assertEqual(stock, quote['stock'])
        self.assertEqual(bid_price, float(quote['top_bid']['price']))
        self.assertEqual(ask_price, float(quote['top_ask']['price']))
        self.assertEqual(price, (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2)

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
