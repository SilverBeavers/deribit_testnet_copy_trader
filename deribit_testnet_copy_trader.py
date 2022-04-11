from deribit_ws import WS_Client
from deribit_limit_trade import deribit_limit_trade
import time

from credentials import (
    testnet_client_id,
    testnet_client_secret,
    testnet_client_url,
    mainnet_client_id,
    mainnet_client_secret,
    mainnet_client_url,
)

from user_settings import instrument_names, trade_amount, sleep_time

testnet_client = WS_Client(testnet_client_id, testnet_client_secret, testnet_client_url)
mainnet_client = WS_Client(mainnet_client_id, mainnet_client_secret, mainnet_client_url)


# @param _instrument_names The instrument name list which to be monitored
# @param _trade_amount The trade amount list for each side of trade
def deribit_testnet_copy_trader(_instrument_names, _trade_amount):
    for index, instrument_name in enumerate(_instrument_names):
        # loop through the instruments
        print(f"instrument_name: {instrument_name}")

        # get price of mainnet open position
        mainnet_ticker_response = mainnet_client.ticker(instrument_name)

        # get best price at mainnet order book
        mainnet_best_bid_price = mainnet_ticker_response["result"]["best_bid_price"]
        mainnet_best_ask_price = mainnet_ticker_response["result"]["best_ask_price"]

        # get account open order at testnet
        testnet_open_orders_response = testnet_client.get_open_orders_by_instrument(
            instrument_name, "limit"
        )

        # check for open position
        if len(testnet_open_orders_response["result"]) == 0:
            # no open position
            deribit_limit_trade(
                testnet_client,
                instrument_name,
                True,
                _trade_amount[index],
                mainnet_best_bid_price,
            )
            deribit_limit_trade(
                testnet_client,
                instrument_name,
                False,
                _trade_amount[index],
                mainnet_best_ask_price,
            )
        elif len(testnet_open_orders_response["result"]) == 1:
            # one open position
            if testnet_open_orders_response["result"][0]["direction"] == "buy":
                deribit_limit_trade(
                    testnet_client,
                    instrument_name,
                    False,
                    _trade_amount[index],
                    mainnet_best_ask_price,
                )

            else:
                deribit_limit_trade(
                    testnet_client,
                    instrument_name,
                    True,
                    _trade_amount[index],
                    mainnet_best_bid_price,
                )

        # check for edit position
        for result in testnet_open_orders_response["result"]:
            if result["direction"] == "buy" and (
                result["price"] != mainnet_best_bid_price
                or result["amount"] != _trade_amount[index]
            ):
                if mainnet_best_bid_price != 0:
                    # mainnet best price is different from the testnet price
                    testnet_client.edit(
                        result["order_id"], _trade_amount[index], mainnet_best_bid_price
                    )
                    print(
                        f"Edited {_trade_amount[index]} long  position to the price of {mainnet_best_bid_price} and amount of {_trade_amount[index]}"
                    )
                else:
                    # if no best price
                    # then cancel order
                    testnet_client.cancel(result["order_id"])
                    print(f"Canceled long  position")
            elif result["direction"] == "sell" and (
                result["price"] != mainnet_best_ask_price
                or result["amount"] != _trade_amount[index]
            ):
                if mainnet_best_ask_price != 0:
                    # mainnet best price is different from the testnet price
                    testnet_client.edit(
                        result["order_id"], _trade_amount[index], mainnet_best_ask_price
                    )
                    print(
                        f"Edited {_trade_amount[index]} short position to the price of {mainnet_best_ask_price} and amount of {_trade_amount[index]}"
                    )
                else:
                    # if no best price
                    # then cancel order
                    testnet_client.cancel(result["order_id"])
                    print(f"Canceled short position")
        # break line
        print("-" * 80)


def main():
    while True:
        deribit_testnet_copy_trader(instrument_names, trade_amount)
        # wait for some time before the next loop
        time.sleep(sleep_time)


main()
