import re
import urllib
from urllib import request
from bs4 import BeautifulSoup
import http
import socket

regex = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[" \
        "\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[" \
        "a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(" \
        "?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[" \
        "\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

input_file = open('input.csv', mode='r')
next_url = input_file.readlines()

for y in range(0, len(next_url)):
    print(next_url[0 + y])

    try:
        page = request.urlopen(next_url[0 + y], timeout=5)
        soup = BeautifulSoup(page, features='lxml')
        html_code = soup.prettify()

        mails = re.findall(regex, html_code)

        for x in range(0, len(mails)):
            if '.png' in (mails[0 + x]):
                pass
            else:
                output_file = open('output.csv', mode='a')
                output_file.write(str(mails[0 + x]) + '\n')
                print(mails[0 + x])
                output_file.close()

    except urllib.error.URLError:
        print('URLError')
    except http.client.InvalidURL:
        print('InvalidURL')
    except ValueError:
        print('ValueError')
    except socket.error:
        print('socket.error')
    except http.client.IncompleteRead:
        print('IncompleteRead')

input_file.close()