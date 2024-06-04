import os
import requests
import time
import json

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[33m'
BLUE = '\033[36m'
RESET = '\033[0m'

def check_username(name):
    url = f"https://api.mojang.com/users/profiles/minecraft/{name}"
    retries = 5
    for _ in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return "taken"
            elif response.status_code == 404:
                try:
                    response_data = response.json()
                    if "errorMessage" in response_data and response_data["errorMessage"] == f"Couldn't find any profile with name {name}":
                        return "not taken"
                except json.JSONDecodeError:
                    pass
            else:
                print(f"[{YELLOW}~{RESET}] RATE LIMIT ({name})")
                time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"[{YELLOW}~{RESET}] RATE LIMIT ({name})")
            time.sleep(1)
    return "error"

output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open('names.txt', 'r') as file:
    names = file.readlines()

total_names = len(names)
unavailable = []
available = []
ratelimited = []

total_names_width = len(str(total_names))

for idx, name in enumerate(map(str.strip, names), start=1):
    status = check_username(name)
    percent_checked = round((idx / total_names) * 100, 1)
    percent_string = f"{percent_checked:05.1f}"
    line_number_string = f"{idx:0{total_names_width}d}"
    if status == "taken":
        print(f"[{RED}-{RESET}] {name} is taken     [{BLUE}{line_number_string}/{total_names}{RESET}] [{BLUE}{percent_string}%{RESET}]")
        unavailable.append(name)
    elif status == "not taken":
        print(f"[{GREEN}+{RESET}] {name} is not taken [{BLUE}{line_number_string}/{total_names}{RESET}] [{BLUE}{percent_string}%{RESET}]")
        available.append(name)
    else:
        print(f"[{YELLOW}~{RESET}] {name} got rate limited [{BLUE}{line_number_string}/{total_names}{RESET}] [{BLUE}{percent_string}%{RESET}]")
        ratelimited.append(name)

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(item + '\n')

write_to_file(os.path.join(output_folder, 'unavailable.txt'), unavailable)
write_to_file(os.path.join(output_folder, 'available.txt'), available)
write_to_file(os.path.join(output_folder, 'ratelimited.txt'), ratelimited)
