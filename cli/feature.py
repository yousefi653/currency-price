import requests as re
from prettytable import PrettyTable
import shlex

api_key = "FreeG16oeLl7ve3h4abbbIviMDfezM7u"
url = "https://BrsApi.ir/Api/Market/Gold_Currency.php?key="
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0"
}


def price(symbol):
    data = get_data()
    symbol = symbol.upper()

    for type in data:
        for item in data[type]:
            if item["symbol"] == symbol:

                if type == "cryptocurrency":
                    unit = "Dollar $"
                    print(
                        f"\ndate: {item['date']}\n{20 * '-'}\ntime: {item['time']}\n{20 * '-'}\nprice: {float(item['price']):,} {unit}\n{20 * '-'}\nname: {item['name_en']}\n{20 * '-'}\nsymbol: {item['symbol']}\n{20 * '-'}\nmarket_cap: {item['market_cap']:,}\n{20 * '-'}\nchange_percent: {item['change_percent']:.2f}%\n"
                    )
                    return True

                if item["unit"] == "تومان":
                    unit = "Toman"
                else:
                    unit = "Dollar $"
                print(
                    f"\ndate: {item['date']}\n{20 * '-'}\ntime: {item['time']}\n{20 * '-'}\nprice: {item['price']:,} {unit}\n{20 * '-'}\nname: {item['name_en']}\n{20 * '-'}\nsymbol: {item['symbol']}\n{20 * '-'}\ndiffrance: {item['change_value']:,} {unit}\n{20 * '-'}\nchange_percent: {item['change_percent']:.2f}%\n\n(Changes compared to yesterday)\n"
                )
                return True
    print(ValueError(f"{symbol} not found!!!!"))
    return False


def get_data():
    try:
        response = re.get(url + api_key, headers=headers, timeout=5)
        data = response.json()
        return data
    except re.exceptions.ConnectionError:
        print(
            "Had a Error:\nWe can't connect to the server \nplease check your internet connection....."
        )
        return False
    except re.exceptions.Timeout:
        print(
            "Had a Error:\nThe request took too long\nis the problem with your internet or the server..."
        )
        return False


def List(t, all):
    data = get_data()
    if data:
        if all:
            for type in data:
                print(type, ": ")
                table = PrettyTable(["id", "type", "name_en", "symbol"])
                id = 0
                for item in data[type]:
                    id += 1
                    table.add_row([id, type, item["name_en"], item["symbol"]])
                print(table)
            return True
        elif t:
            id = 0
            table = PrettyTable(["id", "type", "name_en", "symbol"])
            for item in data[t]:
                id += 1
                table.add_row([id, t, item["name_en"], item["symbol"]])
            print(table)
            return True
    return False


def check_command(command):

    if command == ["--help"]:
        return True

    if command[0] == "price":
        templates = {"1": "price -s", "2": "price --symbol"}
        if command == shlex.split("price --help"):
            return True
        for item in templates.values():
            if (len(command) == 3) and (command[:2] == shlex.split(item)):
                return True
        return "\nPlease see price --help"

    if command[0] == "list":
        templates = {
            "1": "list --type",
            "2": "list -t",
            "3": "list --all",
            "4": "list -a",
        }
        if command == shlex.split("list --help"):
            return True
        for item in templates.values():
            if (2<=len(command)<=3) and (command[:2] == shlex.split(item)):
                return True
        return "\nPlease see list --help"

    return "!! Command not found !!\nEnter --help"
