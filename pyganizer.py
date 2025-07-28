import argparse
import os 
import time

parser = argparse.ArgumentParser(description="File organizer with Python.")
subparser = parser.add_subparsers(dest="command")

clean_parser = subparser.add_parser("clean_days")
clean_parser.add_argument("folder", type=str, help="The folder destination.")
clean_parser.add_argument("--days", type=int, default=30, help="Delete files older than this date.")

args = parser.parse_args()

def clean_folder_days(folder, days):
    now = time.time()
    cutoff = now - (days * 86400)
    
    for items in os.listdir(folder):
        item_path = os.path.join(folder, items)
        if os.path.isfile(item_path):
            try:
                os.remove(item_path)
                print(f"{item_path} successfully deleted.")
            except OSError as e:
                print(f"Trouble deleting {item_path}: {e}")        
                
if args.command == "clean_days":
    clean_folder_days(args.folder, args.days)
else:
    parser.print_help()