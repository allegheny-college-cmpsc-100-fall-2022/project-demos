from inventory.Item import ItemSpec

class Pizza(ItemSpec):

  consumable = True

  def __init__(self):
    super().__init__(__file__)
    self.price = 15.99
