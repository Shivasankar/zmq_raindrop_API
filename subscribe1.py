import raindrop_api


def main():
    raindrop_api.subscriber(channel='price_update', callback=price_update_receiver)


def price_update_receiver(value):
    print 'price update ', value

main()

