from threading import Thread
from typing import Callable
from traceback import print_exc
import globals

class UnableToFindThreadError(RuntimeError):
    pass

class NoRunningThreadsError(RuntimeError):
    pass

class ThreadManager:

    def __init__(self) -> None:
        self.threads = []

    def add_thread(self, _target: Callable, _name: str) -> int:
        # return index? name?
        thread = Thread(target=_target, name=_name, args=(lambda: globals.KEY_LISTENER_HIT, ))
        thread_index = len(self.threads) - 1
        self.threads.append({
            'name': _name,
            'thread': thread,
            'is_running': True
        })
        thread.start()
        return thread_index


    def join_thread(self, find_param) -> None:
        if len(self.threads) == 0:
            raise NoRunningThreadsError('There are no running threads.')

        try:
            if type(find_param) is str:
                self._join_thread_by_name(str(find_param))
            elif type(find_param) is int:
                self._join_thread_by_index(int(find_param))
        except BaseException:
            print_exc()

    def _join_thread_by_name(self, _name: str) -> None:
        found_thread = None
        thread_index = -1
        for index, thread in enumerate(self.threads):
            if thread['name'] == _name:
                found_thread = thread['thread']
                thread_index = index
        if found_thread is None:
            raise UnableToFindThreadError(f"Thread name '{_name}' not found.")
        found_thread.join()
        del self.threads[thread_index]


    def _join_thread_by_index(self, index: int) -> None:
        if index > (len(self.threads) - 1):
            raise UnableToFindThreadError(f"Thread index {index} is out of of bounds.")
        self.threads[index].join()
        del self.threads[index]
        # self.threads[index]['is_running'] = False
        # Do I want to remove them?

    def are_threads_running(self):
        return True if (len(self.threads) > 0) else False
