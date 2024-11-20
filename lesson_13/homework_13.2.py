
class Counter:

   def __init__(self, current=4, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self):
       self.current = int(input("Set the start value: "))

   def set_max(self):
        self.max_value = int(input("Set the max value: "))

   def set_min(self):
       self.mim_value = int(input("Set the min value: "))

   def step_up(self):
       self.current += 1
       if self.current == self.max_value:
           raise ValueError("The value can't be bigger than maximum value!")

   def step_down(self):
       self.current -= 1
       if self.current == self.min_value:
            raise ValueError("The value can't be more smaller than minimum value!")

   def get_current(self):
       return self.current

my_value = Counter()
my_value.set_current()
my_value.set_min()
my_value.set_max()
my_value.step_down()
my_value.step_down()
my_value.step_down()
print(my_value.get_current())
