# A currency converter / set of currency converter functions
# Uses API from https://free.currencyconverterapi.com/
# MolarFox 2021

import sys
import json
import requests

def read_api_key(keypath):
    """Prints the contents of the file at path passed as arg (for use in retrieving API key)

    Args:
        keypath (str): Path to API key file

    Raises:
        SystemExit: When unable to find specified file

    Returns:
        str: File contents
    """
    try:
        with open(keypath, "r") as keyfile:
            return keyfile.read()[:-1]  # slice out newline
    except FileNotFoundError:
        raise SystemExit("Error attempting to read API key file - file does not exist")


def get_conv_rate(apikey, from_curr, to_curr):
    """Gets conversion rate between currencies by using API call to service

    Args:
        apikey (str): API key for free.currconv.com
        from_curr (str): 3 letter abbreviation of currency to convert from
        to_curr (str): 3 letter abbreviation of currency to convert to

    Returns:
        float: conversion rate, else 0 if invalid conversion
    """
    # string required for API in determining conversion
    conv_string = f"{from_curr}_{to_curr}".upper()
    # Attempt to get conversion rate of args specified
    conv_rate = requests.get('https://free.currconv.com/api/v7/convert',
        params={
            'apiKey':apikey,
            'compact':'ultra',
            'q':conv_string
        }
    )

    # Return 0 if the conversion rate was invalid, else parse and return float
    if conv_rate.text == "{}":
        return 0
    else:
        return float(json.loads(conv_rate.text)[conv_string])
    

def get_currencies(apikey):
    """Gets dictionary containing details of all possible currencies
            Has currency full name, 3-letter abbreviation, and symbol (where available)

    Args:
        apikey (str): API key for free.currconv.com

    Returns:
        {str: {str:str}}: Dictionary containing parsed json response from API
    """
    response = requests.get('https://free.currconv.com/api/v7/currencies',
        params={
            'apiKey':apikey
        }
    )

    # Parse and return the response
    return json.loads(response.text)["results"]


def convert(apikey, from_curr, to_curr, amount=1.0):
    """Converts amount of a currency to another currency

    Args:
        apikey (str): API key for free.currconv.com
        from_curr (str): 3 letter abbreviation of currency to convert from
        to_curr (str): 3 letter abbreviation of currency to convert to
        amount (float, optional): Amount of currency to convert. Defaults to 1.

    Returns:
        float: Amount of output currency representing same value as amount of input currency
    """
    conv_rate = get_conv_rate(apikey, from_curr, to_curr)
    return amount * conv_rate



if __name__ == '__main__':
    apikey = read_api_key("apikey.txt")

    print("\nWelcome to a cool and good cli currency converter by MolarFox\n")

    print(get_conv_rate(apikey, "USD", "AUD"))
    print(get_conv_rate(apikey, "USD", "aud"))
    print(get_conv_rate(apikey, "USD", "shittiddies"))

    # Define dictionary to act as pseudo- switch case
    cli_handler = {
        "list" :    lambda : print(),
        "info":     lambda : print(),
        "from":     lambda : print(),
        "to":       lambda : print(),
        "convert":  lambda : print(),
        "about":    lambda : print(),
        "quit":     lambda : sys.exit(0),
        "?":        lambda : print(
                                "Possible commands:\n"
                                "list       - lists available currencies\n"
                                "from       - change currency to convert from\n"
                                "to         - change currency to convert to\n"
                                "info       - display which currencies currently chosen, and their conversion rates\n"
                                "convert    - convert an amount of the defined currencies (will prompt)\n"
                                "about      - about this program\n"
                                "quit       - quit program execution\n"
                                "?          - display this help text\n"
                            )
    }

    # Take user input and handle until user chooses to quit
    while(True):
        # Strip spaces from incoming user command, make all lower case
        command = input("Enter a command ('?' for help): ").strip(" ").lower()  
        # Use anon functions stored in dict above (basically a switch case)
        cli_handler.get(command, lambda : print("Unknown command! Try again"))()

"""
    for key in (currs := get_currencies(apikey)):
        print(f"{key}: {currs[key]['currencyName']}")
"""
