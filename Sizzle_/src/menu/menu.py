# menu.py

class Menu:
    """
    Represents the menu for Sizzle & Spice catering.
    """
    
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        """
        Adds an item to the menu.
        """
        # code to add menu items goes here.

class MenuItem:
    """
    Represents a menu item.
    """
    
    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category

# menu.py

class Menu:
    """
    Represents the menu for Sizzle & Spice catering.
    """
    
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Adds an item to the menu.

        Args:
            item (MenuItem): The menu item to add.
        """
        self.items.append(item)

    def view_menu(self):
        """
        Returns the current menu.
        """
        return self.items

    def recommend_items(self, customer_preferences):
        """
        Generates menu recommendations based on customer preferences.

        Args:
            customer_preferences (list): A list of preferred categories.

        Returns:
            list: Recommended menu items.
        """
        recommendations = []
        for item in self.items:
            if item.category in customer_preferences:
                recommendations.append(item)
        return recommendations

class MenuItem:
    """
    Represents a menu item.
    """
    
    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
