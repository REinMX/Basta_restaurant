from datetime import time
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return '{address}'.format(address = self.address)
  
  def available_menus(self, time):
    temp_menus = []
    for i in self.menus:
       if (time >= i.start_time) and (time <= i.end_time):
         temp_menus.append(i.name)
    return temp_menus

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "{name} menu available from {start} to {end}".format(name = self.name, start = self.start_time, end = self.end_time)
  
  def calculate_bill(self, purchased_items):
    total_price = 0
    for i in purchased_items:
      temp_dict = self.items
      total_price += temp_dict.get(i)
    return total_price


# Brunch menu
brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, time(11), time(16) )

# Early bird menu
early_bird = Menu("early bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, time(15), time(18) )

# Dinner menu
dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, time(17), time(23) )

# Kids menu
kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, time(11), time(21) )

# Test of method calculate bill from class Menu
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


# Creating Franchise flagship_store
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])

# Creating Franchise new_installment
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

# Test of method available_menus from class Franchise 
print(new_installment.available_menus(time(17)))

# Creating Business basta
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Creating arepas_menu
arepas_menu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

# Creating Franchise arepas_place
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

# Creating Business Take_a_arepa
Take_a_arepa = Business("Take a' Arepa", arepas_place)