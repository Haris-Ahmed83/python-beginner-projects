print("=== WEATHER NOTES APP ===")

while True:
    print("\nMenu:")
    print("1. Add Today's Weather Note")
    print("2. View All Notes")
    print("3. Exit")

    choice = input("Choose option (1-3): ")

    if choice == "1":
        weather = input("Enter today's weather (sunny/cloudy/rainy/etc.): ")
        note = input("Write your note: ")

        with open("weather_notes.txt", "a") as file:
            file.write(f"Weather: {weather} | Note: {note}\n")

        print("Note saved successfully!")

    elif choice == "2":
        print("\n=== All Saved Weather Notes ===")

        try:
            with open("weather_notes.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No notes found yet. Add your first note!")

    elif choice == "3":
        print("Goodbye! Stay consistent with learning 😊")
        break

    else:
        print("Invalid option! Please choose from (1-3).")
