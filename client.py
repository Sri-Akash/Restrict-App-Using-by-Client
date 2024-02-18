import requests
import subprocess

def main():
    server_url = 'http://localhost:5000'

    path = input("Enter the path of the application you want to open: ")

    response = requests.get(f'{server_url}/update_access', params={'path': path})

    if response.status_code == 200:
        access_status = response.text
        print(f"Access {access_status} for {path}")

        if access_status == 'granted':
            subprocess.Popen([path])
        else:
            print("Access not granted. Cannot open the application.")
    else:
        print("Failed to communicate with the server.")

if __name__ == '__main__':
    main()
