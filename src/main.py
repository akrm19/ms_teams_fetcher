#needed for windows
import sys
sys.path.append('src')

from credentials import get_access_token
from teams_fetcher import *

def main():
    access_token = get_access_token()
    teams = get_teams_channels(access_token)
    chats = get_teams_chat(access_token=access_token)

    with open('teams_result.json', 'w') as f:
        json.dump({
            'teams': teams,
            'chats': chats
        }, f, indent=4)

if __name__ == "__main__":
    main()