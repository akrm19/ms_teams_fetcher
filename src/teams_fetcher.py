import json, requests

from credentials import default_credential, get_access_token

def get_auth_headers(access_token: str = None):
    if access_token is None:
        access_token = get_access_token().token

    return { 
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

def get_teams_channels(access_token:str = None):
    headers = get_auth_headers(access_token)
    response = requests.get(
        "https://graph.microsoft.com/v1.0/me/joinedTeams", 
        headers=headers
    )
    response_json = response.json()

    teams = []
    for team in response_json['value']:
        team_id = team['id']
        team_name = team['displayName']
        channels = get_team_channel_info(team_id, access_token)
        teams.append({
            'team_id': team_id,
            'team_name': team_name,
            'channels': channels
        })

    return teams

def get_team_channel_info(team_id:str, access_token:str = None):
    headers = get_auth_headers(access_token)
    channel_response = requests.get(
        f"https://graph.microsoft.com/v1.0/teams/{team_id}/channels",
        headers=headers
    )
    channel_response_json = channel_response.json()
    
    channels = []
    for channel in channel_response_json['value']:
        channel_id = channel['id']
        channel_name = channel['displayName']
        channels.append({
            'channel_id': channel_id,
            'channel_name': channel_name
        })
    return channels


    
def get_unseen_channel_messages(access_token: str = None, channels: list = None):
    """Retrieve all unseen messages from each channel."""
    headers = get_auth_headers(access_token)
    
    unseen_messages = []
    for team_channels in channels:
        for channel in team_channels['value']:
            chat_id = channel['id']
            message_response = requests.get(
                f'https://graph.microsoft.com/v1.0/chats/{chat_id}/messages?$filter=lastModifiedDateTime lt {channel["latestMessage"]["createdDateTime"]}',
                headers=headers,
            )
            messages_data = message_response.json()
            unseen_messages.append(messages_data)

    return unseen_messages


def get_teams_chat(access_token: str = None):
    headers = get_auth_headers(access_token)
    response = requests.get(
        "https://graph.microsoft.com/v1.0/me/chats",
        headers=headers
    )
    return response.json()

def get_unseen_chat_messages(access_token: str = None, chats: list = None):
    """Retrieve all unseen messages from each chat."""
    headers = get_auth_headers(access_token)
    unseen_chats = []
    #for chat in chats:
    for chat in chats['value']:
        chat_id = chat['id']
        message_response = requests.get(
            f'https://graph.microsoft.com/v1.0/chats/{chat_id}/messages?$filter=lastModifiedDateTime lt {chat["latestMessage"]["createdDateTime"]}',
            headers=headers,
        )
        messages_data = message_response.json()
        unseen_chats.append(messages_data)
    return unseen_chats

