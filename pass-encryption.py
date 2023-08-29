import base64


def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)
    print(f"Encoded password : {encoded_bytes}")


def decrypt_pass(password):
    decoded_bytes = base64.b64decode(password)
    print(f"Decoded password : {decoded_bytes.decode()}")


def check_actions():
    action = input("Do you want to encode your password ? (y/n) ")
    if action == "y":
        user_pass = input("Enter you password: ")
        encrypt_pass(user_pass)
    else:
        action = input("Do you want to decode your encoded password ? (y/n) ")
        if action == "y":
            user_encoded_pass = input("Enter you encoded base64 string: ")
            decrypt_pass(user_encoded_pass)

check_actions()