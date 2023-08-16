import random

def prank():
  message = random.choice([
    "Your computer has crashed",
    "You have a virus",
    "Your files are being deleted",
    "Your credit card information has been stolen",
    "You are being tracked by the government"
  ])

  print(message)

if __name__ == "__main__":
  prank()
