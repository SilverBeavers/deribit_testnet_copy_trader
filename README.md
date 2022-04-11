# Deribit Testnet Copy Trader
 
<p>Deribit Testnet Copy Trader is a python script that copy trade from Deribit mainnet to testnet.</p>
<p>Some instruments in Deribit testnet may have limited liquidity and create addition challenges for testing scripts. By copying mainnet trades to testnet, it can creates a more liquid testing environment.</p>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li>
      <a href="#docs">Docs</a>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## Built With
- <a href="https://github.com/Jimmy-sha256/deribit_websocket_v2">Jimmy-sha256 / deribit_websocket_v2</a>
- <a href="https://docs.python.org/3/library/asyncio.html">asyncio</a>
- <a href="https://websockets.readthedocs.io/en/stable/index.html">websockets</a>
- <a href="https://docs.python.org/3/library/json.html">json</a>
- <a href="https://docs.python.org/3/library/time.html">time</a>

## Getting Started
1. Register a mainnet account with Deribit (<a href="https://www.deribit.com/?reg=16509.3813">Affiliated link</a>, 
<a href="https://www.deribit.com/register">Non-affiliated link</a>).
2.Register a testnet account with Deribit (<a href="https://test.deribit.com/register">Non-affiliated link</a>).
3.Fund testing token to testnet account. (Do not send real coin to testnet deposite address)</li>
<ol>
    <li>Select coin type (BTC, ETH, SOL) on top left corner</li>
    <li>Click "Generate a deposit address"</li>
    <li>Copy deposit address</li>
    <li>Click on "here" of "You can fund your account with internal test coins here. In this case, please don't deposit more than 10 BTC to leave some coins for other traders as well." or <a href="https://test.deribit.com/dericoin/BTC/deposit">https://test.deribit.com/dericoin/BTC/deposit</a>.</li>
    <li>Paste the deposit address.</li>
    <li>Input the deposit amount.</li>
    <li>Click "Make deposit".</li>
</ol>
4.  
```sh
git clone https://github.com/SilverBeavers/deribit-testnet-copy-trader
```
5. Add mainnet API key to "credentials.py"
<ol>
    <li>Click on User Name on top right corner > "My Account" > "API" > "Add New Key"</li>
    <li>Select "Trade" > "read" > "Create a new API key"</li>
    <li>Copy "Client ID" and "Client Secret" to "credentials.py"</li>
</ol>
6. Add testnet API key to "credentials.py"
<ol>
    <li>Click on User Name on top right corner > "My Account" > "API" > "Add New Key"</li>
    <li>Select "Trade" > "read" > "Create a new API key"</li>
    <li>Copy "Client ID" and "Client Secret" to "credentials.py"</li>
</ol>
7. Input parameters to "user_settings.py"
8.  
```sh
python deribit_testnet_copy_trader.py
```

## Docs
```sh
deribit_testnet_copy_trader(_instrument_names, _trade_amount)
```
<table>
  <tr>
    <th>Parameter</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>_instrument_names</td>
    <td>List</td>
    <td>The instrument name list which to be monitored</td>
  </tr>
  <tr>
    <td>_trade_amount</td>
    <td>List</td>
    <td>The trade amount list for each side of trade</td>
  </tr>
</table>

```sh
deribit_limit_trade(deribit_client, instrument_name, is_buy, trade_amount, price)
```

<table>
  <tr>
    <th>Parameter</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>deribit_client</td>
    <td>WS_Client</td>
    <td>Deribit websocket client</td>
  </tr>
  <tr>
    <td>is_buy</td>
    <td>bool</td>
    <td>Whether buy or sell, True: buy, False: sell</td>
  </tr>
  <tr>
    <td>trade_amount</td>
    <td>float</td>
    <td>The amount of contract wish to be traded</td>
  </tr>  
  <tr>
    <td>price</td>
    <td>float</td>
    <td>The limit price</td>
  </tr>

</table>

## Contact

- GitHub:  <a href="https://github.com/SilverBeavers">https://github.com/SilverBeavers</a>
- Project Link: <a href="https://github.com/SilverBeavers/deribit-testnet-copy-trader">https://github.com/SilverBeavers/deribit-testnet-copy-trader</a>
- Twitter:  <a href="https://twitter.com/Silver_Beavers">https://twitter.com/Silver_Beavers</a>


