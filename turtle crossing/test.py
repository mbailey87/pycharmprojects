import random
import time

def my_function():
  """
  This is the function that will be repeated.
  Replace this with your desired function.
  """
  print("Function executed!")

def repeat_random_interval(func, min_interval, max_interval):
  """
  Repeats the given function at random intervals.

  Args:
    func: The function to repeat.
    min_interval: The minimum interval (in seconds) between executions.
    max_interval: The maximum interval (in seconds) between executions.
  """
  while True:
    interval = random.uniform(min_interval, max_interval)
    time.sleep(interval)
    func()

if __name__ == "__main__":
  # Set the minimum and maximum interval in seconds
  min_interval_seconds = 1
  max_interval_seconds = 5

  # Start repeating the function at random intervals
  repeat_random_interval(my_function, min_interval_seconds, max_interval_seconds)