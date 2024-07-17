import requests
import json
import sys

while True:
    try:
        if len(sys.argv) == 2:
            qnt = float(sys.argv[1])
            if qnt > 0:
                quote = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

                # print do json completo
                #print(json.dumps(quote, indent = 2))

                '''
                o json que obetemos da API
                "bpi":{
                "USD":{
                    "code":"USD",
                    "symbol":"&#36;",
                    "rate":"38,761.0833",
                    "description":"United States Dollar",
                    "rate_float":38761.0833
                }
                '''

                rate_float_usd = quote['bpi']['USD']['rate_float'] # Como aceder a nested dictionaries no Python
                total = float(rate_float_usd) * qnt
                print(f"${total:,.4f}")
                break
            else:
                print("apenas numeros positivos")
                break

        elif len(sys.argv) != 2:
            sys.exit("Missing command-line argument")

    except requests.RequestException:
        sys.exit
    except ValueError:
        sys.exit("Command line argument is not a number")
