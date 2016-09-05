#!/opt/rh/python33/root/usr/bin/python3
import re
import urllib.request
#https://www.google.com/finance?q=goog

arrayofStocks = ["FB", "GOOG", "HPY"]

url = "https://www.google.com/finance?q="
stock = input("Enter your stock: ")
url = url + stock # Cat'ting Strings


data = urllib.request.urlopen(url).read()

data1 = data.decode("utf-8")


m = re.search('meta itemprop="price"', data1)




start = m.start
end = start + 50
newString = data1[start:end]
#strip the content out
m = re.search('content="', newString)
start = m.end()
newString1 = newString[start:]


m = re.search("/", newString1)
start = 0
end = m.end()-3
final = newString1[0:end]
print("the value of" + stock + "is" + final)
