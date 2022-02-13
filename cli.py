from threading import active_count
from events.event import Event
from events.quote_event import QuoteEvent


def run_cli():
    base_event = Event()
    quote_event = QuoteEvent()
    outer = ''
    while outer == '':
        thread_count = active_count()
        if thread_count <= 6:
            _input = base_event.get_master_input()

            if _input.lower() == 'exit':
                outer = ''
                break
            elif _input.lower() == 'n':
                quote_event.start_event()
