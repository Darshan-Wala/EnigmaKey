# Importing necessary modules
import random  # for generating random characters
import string  # for getting string constants
import sqlite3 # for creating and retriving database

# Establish a connection to the SQLite database
conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

# Create the table to store passwords if it doesn't exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY,
    website TEXT,
    username TEXT,
    password TEXT
)
'''
cursor.execute(create_table_query)

def add_password(website, username, password):
    """
    Add a password entry to the database.

    Parameters:
    - website (str): The website name.
    - username (str): The username.
    - password (str): The password.

    Returns:
    None
    """
    insert_query = '''
    INSERT INTO passwords (website, username, password)
    VALUES (?, ?, ?)
    '''
    cursor.execute(insert_query, (website, username, password))
    conn.commit()
    print("✅ Your password has been successfully stored!")

def get_password(website):
    """
    Retrieve a password from the database based on the website name.

    Parameters:
    - website (str): The website name.

    Returns:
    - str: The password if found, None otherwise.
    """
    select_query = '''
    SELECT password FROM passwords WHERE website = ?
    '''
    cursor.execute(select_query, (website,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def fetching():
    """
    Fetch all website names stored in the database.

    Parameters:
    None

    Returns:
    None
    """
    select_query = '''
    SELECT website FROM passwords
    '''
    cursor.execute(select_query)

    rows = cursor.fetchall()

    for row in rows:
        print(row[0])

def flush_database():
    """
    Flush (delete) the entire passwords table from the database.

    Parameters:
    None

    Returns:
    None
    """
    flush_query = '''
    DROP TABLE IF EXISTS passwords
    '''
    cursor.execute(flush_query)
    conn.commit()
    print("🗑️ The database has been flushed.")

def generate_password(length, use_alphabets, use_special_symbols, use_numbers):
    """
    Generate a random password with specified parameters.

    Parameters:
    - length (int): The length of the password.
    - use_alphabets (bool): Whether to include alphabets.
    - use_special_symbols (bool): Whether to include special symbols.
    - use_numbers (bool): Whether to include numbers.

    Returns:
    - str: The generated password.
    """
    password_lowercase = string.ascii_lowercase
    password_punctuation = string.punctuation
    password_digits = string.digits

    if use_alphabets and use_special_symbols and use_numbers:
        result = password_lowercase + password_punctuation + password_digits
    elif use_alphabets and use_special_symbols and not use_numbers:
        result = password_lowercase + password_punctuation
    elif use_alphabets and not use_special_symbols and use_numbers:
        result = password_lowercase + password_digits
    elif not use_alphabets and use_special_symbols and use_numbers:
        result = password_punctuation + password_digits
    elif not use_alphabets and not use_special_symbols and use_numbers:
        result = password_digits
    elif not use_alphabets and use_special_symbols and not use_numbers:
        result = password_punctuation
    elif use_alphabets and not use_special_symbols and not use_numbers:
        result = password_lowercase
    else:
        raise ValueError("Invalid input!")

    password = ''.join(random.choice(result) for i in range(length))
    return password

def main():
    """
    Main function to interact with the password generator.

    Parameters:
    None

    Returns:
    None
    """
    print("+---------------------------------------------------------------------------------------+")
    print("|                                                                                       |")
    print("|                    😈WELCOME TO THE WORLD OF HACKING😈                                |")
    print("|                                                                                       |")
    print("|         🔐This is a password generating tool based on Python programming 🔐           |")
    print("|                          🤖made by RootDenied!🤖                                      |")
    print("|                                                                                       |")
    print("+---------------------------------------------------------------------------------------+")

    choice = input("\n🔐 Do you want to create a password or retrieve passwords or flush your database? (C/R/f): ")
    if choice.lower() == 'c':
        length = int(input("Enter your password length: "))
        use_alphabets = input("Do you want alphabets in your password? (y/n): ").lower() == 'y'
        use_special_symbols = input("Do you want any special symbols? (y/n): ").lower() == 'y'
        use_numbers = input("Do you want numbers in your password? (y/n): ").lower() == 'y'

        password = generate_password(length, use_alphabets, use_special_symbols, use_numbers)

        print(f"\n🔑 Your password is: {password}")
        database = input("\nDo you want to store it in the database? (y/n): ")
        if database.lower() == 'y':
            website = input("\nEnter the website name: ")
            username = input("\nEnter the username: ")
            password_db = password
            add_password(website, username, password_db)
    elif choice.lower() == 'r':
        print("Do you want to retrieve your stored passwords write a password for the Database?: ")
        retrieve = input()
        if retrieve == '#RootDenied!123':
            fetching()
            website = input("\nEnter the website name: ")
            retrieved_password = get_password(website)
            print(retrieved_password)
        else:
            print("❌ Invalid password!")
    
    elif choice.lower() == "f":
        flush_database()

    else:
        print("❌ Sorry, invalid choice.")

if __name__ == '__main__':
    main()
