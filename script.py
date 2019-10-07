import math
import sys
from os import rename

import requests

print(sys.version)  # tell version of python
print(sys.executable)  # where python is located in the computer


def greet(who_to_greet):
    greeting = "hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Corey'))

r = requests.get("https://coreyms.com")
print(r.status_code)
