def parse_input(user_input):
    """
    Парсер для введеного користувачем рядка.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    """
    Додає новий контакт до записника.
    """
    if len(args) != 2:
        return "Error: You must provide a name and a phone number."
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """
    Змінює номер телефону для існуючого контакту.
    """
    if len(args) != 2:
        return "Error: You must provide a name and a new phone number."
    
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return f"Error: Contact '{name}' not found."


def show_phone(args, contacts):
    """
    Виводить номер телефону для заданого імені.
    """
    if len(args) != 1:
        return "Error: You must provide a name."
    
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    return f"Error: Contact '{name}' not found."


def show_all(contacts):
    """
    Виводить всі контакти зі словника.
    """
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    """
    Основний цикл програми.
    """
    contacts = {}  # Словник для збереження контактів
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
