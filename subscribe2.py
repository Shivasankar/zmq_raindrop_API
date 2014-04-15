import raindrop_api
import optparse


def main():
    raindrop_api.subscriber(channel='inventory_update', callback=my_func)


def my_func(value):
    print 'inventory changed ', value

main()
