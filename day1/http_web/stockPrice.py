
import requests

#logic
def lookup(symbol):
    '''
    looks up if  a symbol is available
    input : symbol -> sting
    output : dict[symbol: name]
    '''
    url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input={}".format(symbol)
    response = request(url)
    if response == None:
        pass
    else:
        return analyseData(response)


def quote(symbol):
    '''
    looks up the share price of symbol
    input: symbol -> string
    output: dict[symbol: price]
    '''
    url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol={}".format(symbol)
    response = request(url)
    if response == None:
        pass
    else:
        return analyseData(response)


def request(url):
    '''
    returns the requested url
    '''
    try:
        return requests.get(url)
    except Exception:
        displayError(" Occured while connecting to URL. Please Check You Internet Connection")
        return None

def analyseData(response):
    '''
    input : response object
    output: dictionary containig data
    '''
    return response.json()

def user_input(message):
    '''
    promt's user for input
    '''
    return input(message);

#User interface
def displayLookup(data):
    '''
    display lookup data
    '''
    displayMessage("PLEASE NOTE THE SYMBOL *THIS CAN BE USED TO GET QUOTES!")
    padding = 50
    half_padding = padding // 2
    quater_padding = padding // 4
    print("_" * 150)
    print("|"  + " " * half_padding + str("NAME") + " " * half_padding + "|" +" " * half_padding+ str("SYMBOL") + " " * half_padding + "|" + " " * 6 + "Location")
    print("_" * 150)
    if data == None:
        print("NO INFO SORRY :-(")
    else:

        for info in data:
            side_padd_name = (padding + 4  - len(info['Name'])) // 2
            side_padd_symbol = (padding + 6 - len(info['Symbol'])) // 2
            side_padd_location = (padding + 7 - len(info['Exchange'])) // 2
            print("| "  + " " * side_padd_name + info['Name'] +  " " * side_padd_name +"|"  + " " * side_padd_symbol + info['Symbol'] +" " * side_padd_symbol + "|" + " " * side_padd_location +info['Exchange'])


def displayQoute(data):
    '''
    display quote data
    '''
    
    if data == None or 'Name' not in data:
        print(" NOTHING TO DISPLAY HERE :-)")
    else:
        padding = 40
        half_padding = padding // 2
        print("_" * 100)
        print("|"  + " " * half_padding + "NAME" + " " * half_padding + "|" +" " * half_padding+ "PRICE IN $" )
        print("_" * 100)
        side_padd_name = (padding + 4 - len(data['Name'])) // 2
        side_padd_price = 10
        print("|" + " " * side_padd_name + data['Name'] + " " * side_padd_name + "|" + " " * side_padd_price + str(data['LastPrice']) )


def displayError(messgae = ''):
    '''
    display error message
    '''
    print("Error: {}".format(messgae))

def displayMessage(message):
    '''
    displays abitray message on screen
    '''
    print(message)

def displayMenu():
    '''
    displays the menu
    '''
    print("-" * 10)
    print(" " * 5 + str("Please selcect 1 to Lookup A symbol"))
    print(" " * 5 + str("Please select 2 to Qoute A Symbol"))
    print(" " * 5 + str("Please select E  or Press any Other key to Exit"))


#entry point
def main():
    '''
    runs' program 
    '''
    displayMessage("WELCOME TO Qoutes !")

    while(True):
        displayMenu()
        user_in = user_input("Please select a choice.: ")

        if user_in == '1':
            symbol = user_input("Please Input a Symbol: ")
            data = lookup(symbol)
            displayLookup(data)
            user_input("Press any Key to continue: ")
        elif user_in == '2':
            symbol = user_input("please Input a Symbol: ")
            data = quote(symbol)
            displayQoute(data)
            user_input("Press any Key to continue: ")
        else:
            displayMessage("Goodbye! Thanks for using Qoutes!")
            break
    return


if __name__ == "__main__":
    main()
