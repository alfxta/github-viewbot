import os
import time
from itertools import cycle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from colorama import init, Fore, Style

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_refresh_bot(username):
    url = f"https://github.com/{username}"
    options = Options()

    # Reliable headless mode
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    count = 0

    try:
        while True:
            os.system('title fakecrime.bio/cpp')
            driver.get(url)
            count += 1
            status = (
                f"Running on {Fore.MAGENTA}{url}{Style.RESET_ALL} "
                f"| Views: {Fore.MAGENTA}{count}{Style.RESET_ALL} "
                f"| github.com/{Fore.MAGENTA}alfxta{Style.RESET_ALL}"
            )
            os.system('cls')
            print(status, end="\r", flush=True)

            time.sleep(0.1) # U can adjust it to change the speed of the views
    except KeyboardInterrupt:
        os.system('cls')
        print(f"{Fore.RED}??{Style.RESET_ALL}")
    finally:
        driver.quit()


def main():
    clear_console()
    username = input("username:\n").strip()
    start_refresh_bot(username)


if __name__ == "__main__":
    main()
