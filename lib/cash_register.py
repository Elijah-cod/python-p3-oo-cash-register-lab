#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0, items = None):
    self.discount = discount
    self.total = total
    self.items = [] if items is None else items
    self.last_transaction = 0 

  def add_item (self, title, price, quantity = None):
    self.last_transaction = price
    if quantity:
      self.items.extend([title] * quantity)
      self.total += (price * quantity)
    else:
      self.items.append(title)
      self.total += price
    return self.items
  
  def apply_discount(self):
    if self.discount > 0:
      self.total -= (self.total * self.discount/100)
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print("There is no discount to apply.")
  

  def void_last_transaction(self):
    if self.items:
        # Remove the last added item(s) and subtract the total correctly
        self.items = self.items[:-1]  # Remove the last item (one instance of it)
        self.total -= self.last_transaction  # Subtract the last transaction's total
        self.last_transaction = 0  # Reset last transaction tracker
        
        # If no items remain, reset the total to 0.0
        if not self.items:
            self.total = 0.0
