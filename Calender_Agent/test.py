from mcp.server.fastmcp import FastMCP
import os
import pickle
import google.auth.transport.requests
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pytz

mcp = FastMCP("Calendar")

@mcp.tool()
async def create_event(title: str, description: str, start_time: str, end_time: str, attendees: str) -> str:
    """
    Creates a Google Calendar event with the given details and returns the event link or error.
    """
    SCOPES = ['https://www.googleapis.com/auth/calendar.events']

    def get_calendar_service():
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(google.auth.transport.requests.Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return build('calendar', 'v3', credentials=creds)

    event = {
        'summary': title,
        'description': description,

        
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata',
        },
        'attendees': [{'email': email.strip()} for email in attendees.split(',') if email.strip()],
    }

    try:
        service = get_calendar_service()
        event_result = service.events().insert(calendarId='primary', body=event).execute()
        event_link = event_result.get('htmlLink')
        return f"✅ Event '{title}' created successfully. View it here: {event_link}"
    except Exception as e:
        return f"❌ Failed to create event: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="streamable_http")  # Corrected to match your client config
