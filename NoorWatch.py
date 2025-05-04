import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import init, Fore

init()

def print_banner():
    banner = r"""{Fore.GREEN}
  _   _                 _        _         _     
 | \ | | ___ _ _ __  __| | ___  | |_  ___ | |__  
 |  \| |/ _ \ '_ ` _ \/ _` |/ _ \| __|/ _ \| '_ \ 
 | |\  |  __/ | | | | | (_| | (_) | |_| (_) | | | |
 \_| \_|\___|_| |_| |_|\__,_|\___/ \__|\___/|_| |_|

      Folder Activity Monitor - NoorWatch
         Developed by ASKAL NOUREDDIN
{Fore.RESET}"""
    print(banner)

def log_event(message):
    try:
        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"{time.ctime()} - {message}\n")
    except IOError:
        print(Fore.RED + "Error: Cannot write to log file. Check permissions." + Fore.RESET)

class WatcherHandler(FileSystemEventHandler):
    def on_modified(self, event):
        message = f"[Modified] {event.src_path}"
        print(Fore.YELLOW + message + Fore.RESET)
        log_event(message)

    def on_created(self, event):
        message = f"[Created] {event.src_path}"
        print(Fore.GREEN + message + Fore.RESET)
        log_event(message)

    def on_deleted(self, event):
        message = f"[Deleted] {event.src_path}"
        print(Fore.RED + message + Fore.RESET)
        log_event(message)

    def on_moved(self, event):
        message = f"[Moved] from {event.src_path} to {event.dest_path}"
        print(Fore.MAGENTA + message + Fore.RESET)
        log_event(message)

def start_monitoring(path_to_watch):
    if not os.access(path_to_watch, os.R_OK):
        print(Fore.RED + "Error: Permission denied for this folder." + Fore.RESET)
        return

    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    print(f"\nMonitoring started on: {path_to_watch}\nPress Ctrl+C to stop...\n")
    log_event(f"Started monitoring: {path_to_watch}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print(Fore.RED + "\nMonitoring stopped by user." + Fore.RESET)
        log_event("Monitoring stopped by user.")
        observer.join()

if __name__ == "__main__":
    print_banner()
    folder = input("Enter full path to the folder you want to monitor: ").strip()

    if not folder or not os.path.exists(folder):
        print(Fore.RED + "Invalid folder path. Please check the path and try again." + Fore.RESET)
    else:
        start_monitoring(folder)
