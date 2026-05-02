import car_utils 
import car

def main():
    cars = {}  # Dictionary to store cars with car_id as key and car objects as values

    while True:
        print("\nMenu:")
        print("1. Add a new car")
        print("2. View all cars")
        print("3. Drive a car")
        print("4. Paint a car")
        print("5. Exit")

        choice = input("Choose an option:\n")

        if choice == '1':
          Carro = car_utils.create_car_from_input()
          cars[Carro.car_id] = Carro
          print(Carro)
          print("Car added.")


        elif choice == '2':
          car_utils.display_cars(cars)

        elif choice == '3':
          car_id = input("Enter the car ID to drive:\n")
          miles = float(input("How many miles to drive?\n"))
          auto = cars[car_id]
          auto.drive(miles)
          print("Mileage updated.")
          print(auto)
          
        elif choice == '4':
          car_id = input("Enter the car ID to paint:\n")
          new_color = input("Enter the new color:\n")
          auto = cars[car_id]
          auto.change_color(new_color)
          print("Color updated.")
          print(auto)

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
