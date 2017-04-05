
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
    '''
    displayMessage("WELCOME TO Qoutes !")

    while(True):
        displayMenu()
        user_in = user_input("Please select a choice.: ")

        if user_in == '1':
            symbol = user_input("Please Input a Symbol: ")
        elif user_in == '2':
            symbol = user_input("please Input a Symbol: ")
        else:
            displayMessage("Goodbye! Thanks for using Qoutes!")
            break
    return


if __name__ == "__main__":
    main()
