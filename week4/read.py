def read_file(filename):
    """
    Function to read content from a file.
    Returns the content if successful, or raises an exception if any error occurs.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


def write_file(new_filename, content):
    """
    Function to write modified content to a new file.
    Returns True if successful, False otherwise.
    """
    try:
        with open(new_filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to '{new_filename}'.")
        return True
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{new_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while writing: {e}")
    return False


def main():
    print("📂 File Read & Write Challenge 🖋️")

    # Step 1: Ask the user for the input filename
    filename = input("Enter the name of the file to read: ")

    # Step 2: Read the content of the file
    content = read_file(filename)

    # If reading was successful, proceed to modify and write
    if content is not None:
        # Step 3: Modify the content (example: converting to uppercase)
        modified_content = content.upper()

        # Step 4: Ask for output filename
        new_filename = input("Enter the name of the new file to write: ")

        # Step 5: Write the modified content to a new file
        write_file(new_filename, modified_content)


if __name__ == "__main__":
    main()
