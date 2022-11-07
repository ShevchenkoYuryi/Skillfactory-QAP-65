import requests
import json
from Config import money

class ConvertException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(v_1: str, v_2: str, amount: str):
        if v_1 == v_2:
            raise ConvertException(f"Невозможно перевести одинаковые валюты {v_2}.")

        try:
            v_1_ticker = money[v_1]
        except KeyError:
            raise ConvertException(f'Не удалось обработать валюту {v_1}')

        try:
            v_2_ticker = money[v_2]
        except KeyError:
            raise ConvertException(f'Не удалось обработать валюту {v_2}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={v_1_ticker}&tsyms={v_2_ticker}')
        total_base = json.loads(r.content)[money[v_2]]
        return total_base