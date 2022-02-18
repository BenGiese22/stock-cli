from events.event import Event
from events.watchlist_event import WatchlistEvent

def run_cli():
    base_event = Event()
    watchlist_event = WatchlistEvent()
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
            watchlist_event.add_to_watchlist()
            _input = ''
        elif _input.lower() == 'd':
            watchlist_event.delete_from_watchlist()
            _input = ''
