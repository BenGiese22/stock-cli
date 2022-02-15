from events.event import Event
from events.watchlist_event import WatchlistEvent
from events.add_to_watchlist_event import AddToWatchlistEvent

def run_cli():
    base_event = Event()
    watchlist_event = WatchlistEvent()
    add_to_watchlist_event = AddToWatchlistEvent()
    outer = ''
    while outer == '':
        event_running = base_event.is_master_thread()
        if not event_running:
            _input = base_event.get_master_input()

        if _input.lower() == 'x':
            outer = ''
            break
        elif _input.lower() == 'w':
            watchlist_event.start_event()
            _input = ''
        elif _input.lower() == 'n':
            add_to_watchlist_event.start_event()
            _input = ''
