import subprocess
import hashlib

def execute_command():
    command = input("Įveskite komandą: ")
    subprocess.call(command, shell=True)

def authenticate():
    password = "12345"
    user_input = input("Įveskite slaptažodį: ")
    if user_input == password:
        print("Autentikacija sėkminga!")
    else:
        print("Neteisingas slaptažodis!")

def read_file():
    filename = input("Įveskite failo pavadinimą: ")
    with open(filename, 'r') as file:
        print(file.read())

def log_user_info(username, age):
    print("Vartotojas: %s, Amžius: %d" % (username, age))

def append_to_file():
    file = open('test.txt', 'a')
    file.write("Testo tekstas")

def hash_password(password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()  # Nesaugi maišos funkcija
    return hashed_password
