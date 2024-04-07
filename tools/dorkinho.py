import argparse
from src.Manager import Dorkinho

parser = argparse.ArgumentParser(prog="Dorkinho", description="Perform Google Dorking with an automated script.")
parser.add_argument("domain")
parser.add_argument("-l", "--list", action="store_true", help="list all dorks names")
parser.add_argument("-a", "--all", action="store_true", help="request all dorks in browser")
parser.add_argument("-e", "--exc", action="store_true", help="use an exclusive dork")
args = parser.parse_args()

if __name__ == "__main__":
        dorkinho =  Dorkinho()
        print(args.domain)
        if(args.list):
                dorkinho.list_dorks()
        if(args.all):
                dorkinho.all_requests(args.domain)
        if(args.exc):
                dorkinho.exclusive_dork(args.domain, args.exc)