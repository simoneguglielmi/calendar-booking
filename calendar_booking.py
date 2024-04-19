from cat.mad_hatter.decorators import tool 
from .calendly import Calendly      
    
@tool(examples =["dimmi gli eventi", "dimmi tutti gli eventi", "quali eventi ci sono?", "eventi", "slot", "dimmi le prestazioni"])
def get_events(_, cat):
    """Get all events from the calendar. Input is the event name"""
    
    settings = cat.mad_hatter.get_plugin().load_settings()
    api_key = settings["api_key"]
    calendly = Calendly(api_key)
    if api_key is None:
        return "Non è stata configurata l'API Key, impossibile ottenere eventi."
    events = calendly.get_events()
    if events is None:
        return "Non sono riuscito a trovare eventi, riprova più tardi."
    
    return events

@tool
def get_event(event, cat):
    """Get a specific event from the calendar. Input is the event name"""
    
    settings = cat.mad_hatter.get_plugin().load_settings()
    api_key = settings["api_key"]
    calendly = Calendly(api_key)
    if api_key is None:
        return "Non è stata configurata l'API Key, impossibile ottenere eventi."
    events = calendly.get_events()
    
    for e in events:
        if e["name"] == event:
            return e
    return "Non ho trovato l'evento richiesto."




    
