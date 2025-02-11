import json

from azure.identity import DefaultAzureCredential


default_credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)

def get_access_token_for_client():
    """Get an access token using Azure Identity's DefaultAzureCrendential"""
    return default_credential.acquire_token_for_client(scopes=['https://graph.microsoft.com/.default'])
    #return default_credential.get_token('https://management.azure.com/.default').token

def get_access_token():
    """Get an access token using Azure Identity's DefaultAzureCrendential"""
    return default_credential.get_token('https://graph.microsoft.com/.default').token
