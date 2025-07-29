import argparse
import os 
import time

parser = argparse.ArgumentParser(description="File organizer with Python.")
subparser = parser.add_subparsers(dest="command")

clean_parser_days = subparser.add_parser("clean_days")
clean_parser_days.add_argument("folder", type=str, help="The folder destination.")
clean_parser_days.add_argument("--days", type=int, help="Delete files older than this date.")

clean_parser_minutes = subparser.add_parser("clean_minutes")
clean_parser_minutes.add_argument("folder", type=str, help="The folder destination.")
clean_parser_minutes.add_argument("--minutes", type=int, help="Delete files older than this time in minutes.")

delete_parser_empty_folders = subparser.add_parser("delete_empty_folders")
delete_parser_empty_folders.add_argument("folder", type=str, help="The folder destination.")

args = parser.parse_args()

def clean_folder_days(folder, days):
    now = time.time()
    cutoff = now - (days * 86400)
    
    for items in os.listdir(folder):
        item_path = os.path.join(folder, items)
        modification_date = os.path.getmtime(item_path)
        if os.path.isfile(item_path) and modification_date <= cutoff:
            try:
                os.remove(item_path)
                print(f"{item_path} successfully deleted.")
            except OSError as e:
                print(f"Trouble deleting {item_path}: {e}")        
                
def clean_folder_minutes(folder, minutes):
    now = time.time()
    cutoff = now - (minutes * 60)
    
    for items in os.listdir(folder):
        item_path = os.path.join(folder, items)
        modification_date = os.path.getmtime(item_path)
        if os.path.isfile(item_path) and modification_date <= cutoff:
            try:
                os.remove(item_path)
                print(f"{item_path} successfully deleted.")
            except OSError as e:
                print(f"Error deleting file {item_path}: {e}")

def delete_empty_folders(folder):
    for filename in os.listdir(folder):
        join_folder = os.path.join(folder, filename)
        if os.path.isdir(join_folder):
            if not os.listdir(join_folder):
                try:
                    os.rmdir(join_folder)
                    print(f"Successfully deleted empty folder {join_folder}")
                except OSError as e:
                    print(f"Error deleting folder {join_folder}: {e}")
            
                
if args.command == "clean_days":
    clean_folder_days(args.folder, args.days)
elif args.command == "clean_minutes":
    clean_parser_minutes(args.folder, args.minutes)
elif args.command == "delete_empty_folders":
    delete_empty_folders(args.folder)
else:
    parser.print_help()