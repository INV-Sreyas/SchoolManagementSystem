from auth import login
from student import register_student, list_students

def main():
    print("School Management CLI")

    if not login():
        return

    while True:
        print("\n1. Register Student\n2. List Students\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_student()
        elif choice == '2':
            list_students()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
