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

def get_conv_rate():
    pass

def get_currencies(apikey):
    response = requests.get('https://free.currconv.com/api/v7/currencies',
        params={
        'apiKey':apikey
        }
    )

    raw_vals = json.loads(response.text)["results"]
    return raw_vals

if __name__ == '__main__':
    apikey = read_api_key("apikey.txt")

    print("Welcome to a cool and good cli currency converter by MolarFox\n")

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
