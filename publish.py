import zmq
import raindrop_api



def main():
    raindrop_api.publisher(channel='price_update', value='x=100$')
    raindrop_api.publisher(channel='price_update', value='y=200$')
    raindrop_api.publisher(channel='inventory_update', value='x=10')
    raindrop_api.publisher(channel='inventory_update', value='y=200')
    raindrop_api.publisher(channel='inventory_update', value='x=5')
    raindrop_api.publisher(channel='inventory_update', value='x=150')
    main()
main()
