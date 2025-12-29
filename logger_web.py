# Web-compatible logger - no file operations
def log_state():
    pass  # Disabled for web

def log_event(event_name):
    print(f"Event: {event_name}")  # Just print to console