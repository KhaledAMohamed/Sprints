import datetime
import csv


def user_input():
    print("Please select an action:")
    print("1. Create")
    print("2. Update")
    print("3. Delete")
    selection = int(input("Enter a number: "))
    if selection == 1:
        create()
    elif selection == 2:
        update()
    elif selection == 3:
        delete()
    else:
        print("Wrong choice. Please choose from 1, 2, or 3.")
        user_input()


def create():
    contact_name = input("Please enter the contact name: ")
    contact_email = input("Please enter the contact email: ")
    contact_number = get_valid_contact_number()
    contact_address = input("Please enter the contact address: ")
    insertion_date = datetime.datetime.now().strftime('%d-%m-%Y- %H:%M:%S')
    save_inputs(contact_name, contact_email, contact_number, contact_address, insertion_date)


def get_valid_contact_number():
    while True:
        contact_number = input("Please input the contact number: ")
        if contact_number.isdigit():
            return contact_number
        else:
            print("Please enter a correct contact number.")


def save_inputs(contact_name, contact_email, contact_number, contact_address, insertion_date):
    with open('khaled.csv', 'a', newline='') as file:
        adder = csv.writer(file)
        adder.writerow([contact_name, contact_email, contact_number, contact_address, insertion_date])
    print("Your data has been successfully saved!")


def update():
    search_field = get_valid_search_field()
    search_email = input("Please enter the email of the contact to be updated: ")

    with open('khaled.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if validate_email(rows, search_email):
        for row in rows:
            if row[1] == search_email:
                if int(search_field) == 1:
                    new_value = input("Please enter the new value for contact name: ")
                    row[0] = new_value
                elif int(search_field) == 2:
                    new_value = input("Please enter the new value for contact email: ")
                    row[1] = new_value
                elif int(search_field) == 3:
                    new_value = get_valid_contact_number()
                    row[2] = new_value
                elif int(search_field) == 4:
                    new_value = input("Please enter the new value for contact address: ")
                    row[3] = new_value

        with open('khaled.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Contacts list has been updated successfully")
    else:
        print("Please enter a valid email!")
        update()


def get_valid_search_field():
    while True:
        search_field = input("Please choose the field you want to update:\n"
                             "1. Contact Name\n"
                             "2. Contact Email\n"
                             "3. Contact Number\n"
                             "4. Contact Address\n"
                             "Enter a number: ")
        if search_field.isdigit() and 0 < int(search_field) < 5:
            return search_field
        else:
            print("Please enter a valid choice.")


def validate_email(rows, email):
    for row in rows:
        if row[1] == email:
            return True
    return False


def Delete():
    search_email = input("Enter The Contact email You Want To Remove: ")

    with open('khaled.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    for row in rows:
        if row[1] == search_email:
            validation = 1
            break
        else:
            validation = 0
    if validation == 1:
        for row in rows:
            if row[1] == search_email:
                rows.remove(row)
                with open('khaled.csv', 'w', newline='') as file:
                    adder = csv.writer(file)
                    adder.writerows(rows)
        print("Contact Has Been  Deleted Successfully")

    else:
        print("please enter a valid email !")
        Delete()





if __name__ == '__main__':
    user_input()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/