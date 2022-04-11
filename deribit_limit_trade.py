# @notice call buy or sell in deribit_client
# @param deribit_client The WS_Client
# @param is_buy Whether buy or sell, True: buy, False: sell
# @param trade_amount The amount of contract wish to be traded
# @param price The limit price
def deribit_limit_trade(deribit_client, instrument_name, is_buy, trade_amount, price):
    if price != 0:
        if is_buy:
            deribit_client.buy(
                instrument_name,
                trade_amount,
                "limit",
                False,
                price,
            )
            print(
                f"Opened {trade_amount} long  position at the price of {price} and amount of {trade_amount}"
            )
        else:
            deribit_client.sell(
                instrument_name,
                trade_amount,
                "limit",
                False,
                price,
            )
            print(
                f"Opened {trade_amount} short position at the price of {price} and amount of {trade_amount}"
            )
