def check_key_presence(user_dict, key):
 
  if key in user_dict:
    print(f"Key '{key}' is present in the dictionary.")
  else:
    print(f"Key '{key}' is not present in the dictionary.")

# Get the dictionary from the user
user_dict = eval(input("Enter a dictionary in the format {'key1': value1, 'key2': value2}: "))

# Get the key to check from the user
key = input("Enter the key to check: ")

# Call the function to check for the key
check_key_presence(user_dict, key)
