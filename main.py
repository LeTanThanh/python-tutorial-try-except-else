if __name__ == "__main__":
  # Introduction to the Python try…except…else statement

  """
  try:
    # code that may cause errors
  catch:
    # code that handle exceptions
  else:
    # code that excutes when no exception occurs
  """

  # Using try…except…else statement for control flow

  def calculate_bmi(height, weight):
    """
    calculate body mass index (BMI)
    """
    return weight / (height ** 2)

  def evaluate_bmi(bmi):
    """
    evaluate the bmi
    """

    if 18.5 <= bmi <= 24.9:
      return "healthy"

    if bmi >= 25:
      return "overweight"

    return "underweight"

  # try:
  #   height = float(input("Enter your height (meters): "))
  #   weight = float(input("Enter your weight (kilograms): "))
  # except ValueError as error:
  #   print(error)
  # else:
  #   bmi = round(calculate_bmi(height, weight), 1)
  #   evaluation = evaluate_bmi(bmi)

  #   print(f"Your body mass index is {bmi}")
  #   print(f"This is considered {evaluation}")

  # Using Python try…except…else and finally example

  fruits = {
    "apple": 10,
    "orange": 20,
    "banana": 30
  }

  key = None
  while True:
    try:
      key = input("Enter a key to lookup: ")
      fruit = fruits[key.lower()]
    except KeyError:
      print(f"Error! {key} does not exist.")
    except KeyboardInterrupt:
      break
    else:
      print(fruit)
    finally:
      print("Press Ctrl-C to exit.")
