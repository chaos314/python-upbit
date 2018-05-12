import unittest
import time
import json
from upbit import Upbit

MARKET = 'KRW-BTC'
CURRENCY = 'BTC'


def test_basic_api_response(ut, actual, api_name):
    ut.assertIsNotNone(actual, '{0:s} returns an error.'.format(api_name))


class TestUpbitQuotationAPI(unittest.TestCase):
    """
    Integration tests for the Upbit quotation API.
    """

    def setUp(self):
        self.upbit = Upbit(None, None)

    def tearDown(self):
        pass

    def test_has_neither_access_key_nor_secret_key(self):
        self.upbit = Upbit('abc', None)
        actual = self.upbit.get_markets()
        self.assertIsNotNone(actual)
        self.upbit = Upbit(None, 'xyz')
        actual = self.upbit.get_markets()
        self.assertIsNotNone(actual)
        self.upbit = Upbit(None, None)
        actual = self.upbit.get_markets()
        self.assertIsNotNone(actual)

    def test_get_markets(self):
        actual = self.upbit.get_markets()
        test_basic_api_response(self, actual, 'get_markets')
        self.assertGreater(len(actual), 0, 'get_markets\'s list is 0-length.')

    def test_get_candles_per_minutes_with_exception(self):
        minute = 2
        with self.assertRaises(Exception) as cm:
            actual = self.upbit.get_candles_per_minutes(minute, MARKET)
        self.assertIn('{0:d}-minute'.format(minute), str(cm.exception).split() )

    def test_get_candles_per_minutes(self):
        minutes = [1, 3, 5, 10, 15, 30, 60, 240]
        count = 3
        for i in minutes:
            actual = self.upbit.get_candles_per_minutes(i, MARKET, '', count)
            test_basic_api_response(self, actual, 'get_candles_per_minutes')
            self.assertEqual(len(actual), count, 'the candle count is wrong.')

    def test_get_candles_daily(self):
        count = 5
        actual = self.upbit.get_candles_daily(MARKET, '', count)
        test_basic_api_response(self, actual, 'get_candles_daily')
        self.assertEqual(len(actual), count, 'the candle count is wrong.')

    def test_get_candles_weekly(self):
        count = 5
        actual = self.upbit.get_candles_weekly(MARKET, '', count)
        test_basic_api_response(self, actual, 'get_candles_weekly')
        self.assertEqual(len(actual), count, 'the candle count is wrong.')
        
    def test_get_candles_monthly(self):
        count = 5
        actual = self.upbit.get_candles_monthly(MARKET, '', count)
        test_basic_api_response(self, actual, 'get_candles_monthly')
        self.assertEqual(len(actual), count, 'the candle count is wrong.')

    def test_get_trading_history(self):
        actual = self.upbit.get_trading_history(MARKET)
        test_basic_api_response(self, actual, 'get_trading_history')
        self.assertGreater(len(actual), 0, 'the trading history is wrong.')

    def test_get_ticker(self):
        markets = '{0:s}, BTC-ETH, KRW-STORM'.format(MARKET)
        actual = self.upbit.get_ticker(markets)
        test_basic_api_response(self, actual, 'get_ticker')
        self.assertEqual(len(actual), 3, 'A list length is wrong.')


class TestUpbitAccountAPI(unittest.TestCase):
    """
    Integration tests for the Upbit exchange API.

    A JSON file required for this test. It should have an access key and a secret key issued by Upbit.

    ie. key.json:
    {
        "access": "f4AT0XjalGRvnMPXaxaEK6u3lTTa5szKv7NZSW0q",
        "secret": "aSGFdg23948afj3487faheWGAEalsidhAGFDFaFa"
    }
    """

    def setUp(self):
        with open('key.json') as key_file:
            self.__key = json.load(key_file)
        self.upbit = Upbit(self.__key['access'], self.__key['secret'])

    def tearDown(self):
        #time.sleep(5.0)
        pass

    def test_should_have_access_and_secret(self):
        self.upbit = Upbit(None, None)
        actual = self.upbit.get_assets()
        self.assertIsNone(actual, 'Authorization failed.')
        self.upbit = Upbit(self.__key['access'], None)
        actual = self.upbit.get_assets()
        self.assertIsNone(actual, 'Authorization failed.')
        self.upbit = Upbit(None, self.__key['secret'])
        actual = self.upbit.get_assets()
        self.assertIsNone(actual, 'Authorization failed.')
        self.upbit = Upbit(self.__key['access'], self.__key['secret'])
        actual = self.upbit.get_assets()
        self.assertIsNotNone(actual, 'Authorization failed.')

    def test_get_assets(self):
        actual = self.upbit.get_assets()
        test_basic_api_response(self, actual, 'get_assets')

    def test_get_order_chance(self):
        actual = self.upbit.get_order_chance(MARKET)
        test_basic_api_response(self, actual, 'get_order_chance')

    def test_get_withdraw_chance(self):
        actual = self.upbit.get_withdraw_chance(CURRENCY)
        test_basic_api_response(self, actual, 'get_withdraw_chance')


if __name__ == '__main__':
    unittest.main()

