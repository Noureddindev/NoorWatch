import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import init, Fore

init()

Banner with developer credit
def print_banner():
    banner = f"""{Fore.CYAN}
 _   _                       _       _       _     
| \ | | __  _ _ __   __ | |_ __| |_   | |__  
|  \| |/ _ \| '_ ` _ \ / _ \| _/ _| '_ \  | '_ \ 
| |\  | (_) | | | | | | (_) | || (__| | | | | | | |
\_| \_/\__/|_| |_| |_|\__/ \_\__|_| |_| |_| |_|

         Folder Activity Monitor - NoorWatch
              Developed by ASKAL NOUREDDIN
{Fore.RESET}"""
    print(banner)

Logging utility
def log_event(message):
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{time.ctime()} - {message}\n")

Handler for file system events
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

Main function to start monitoring
def start_monitoring(path_to_watch):
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
        print("\nMonitoring stopped.")
        log_event("Monitoring stopped by user.")

    observer.join()

Entry point
if _name_ == "_main_":
    print_banner()
    folder = input("Enter full path to the folder you want to monitor: ").strip()

    if os.path.exists(folder):
        start_monitoring(folder)
    else:print(Fore.RED + "Folder does not exist. Please check the path and try again." + Fore.RESET)