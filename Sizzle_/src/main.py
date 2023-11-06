

from payments import MpesaPayment, KCBPayment, CryptoWallet
from menu import Menu, MenuItem
from cooking import CookingTutorial

def main():
    # Create instances of payment options
    mpesa_payment = MpesaPayment(api_key='your_api_key', api_secret='your_api_secret')
    kcb_payment = KCBPayment()
    crypto_wallet = CryptoWallet()

    # Create a menu
    menu = Menu()

    # Create menu items
    item1 = MenuItem(name='Spicy Chicken', description='Tender chicken with a spicy twist', price=12.99, category='Main Course')
    item2 = MenuItem(name='Mango Tango Salad', description='Fresh mango salad with a tangy dressing', price=7.99, category

 # Add menu items to the menu
    menu.add_item(item1)
    menu.add_item(item2)

    # Create cooking tutorials
    tutorial1 = CookingTutorial(title='Sizzling Steak', description='Learn how to cook a perfect steak', video_url='https://youtube.com/steakvideo')
    tutorial2 = CookingTutorial(title='Delicious Desserts', description='Discover the art of dessert making', video_url='https://youtube.com/dessertvideo')

    # Start a live cooking demonstration
    tutorial1.start_live_demo()

if __name__ == '__main__':
    main()

    # main.py

from payments import MpesaPayment, KCBPayment, CryptoWallet
from menu import Menu, MenuItem
from cooking import CookingTutorial

def main():
    # Placeholder API credentials
    mpesa_api_key = 'your_mpesa_api_key'
    mpesa_api_secret = 'your_mpesa_api_secret'

    # Create instances of payment options
    mpesa_payment = MpesaPayment(api_key=mpesa_api_key, api_secret=mpesa_api_secret)
    kcb_payment = KCBPayment()
    crypto_wallet = CryptoWallet()

    # Create a menu
    menu = Menu()

    # Create menu items
    item1 = MenuItem(name='Spicy Chicken', description='Tender chicken with a spicy twist', price=12.99, category='Main Course')
    item2 = MenuItem(name='Mango Tango Salad', description='Fresh mango salad with a tangy dressing', price=7.99, category='Salad')

    # Add menu items to the menu
    menu.add_item(item1)
    menu.add_item(item2)

    # Create cooking tutorials
    tutorial1 = CookingTutorial(title='Sizzling Steak', description='Learn how to cook a perfect steak', video_url='https://youtube.com/steakvideo')
    tutorial2 = CookingTutorial(title='Delicious Desserts', description='Discover the art of dessert making', video_url='https://youtube.com/dessertvideo')

    # Start a live cooking demonstration
    tutorial1.start_live_demo()

if __name__ == '__main__':
    main()
