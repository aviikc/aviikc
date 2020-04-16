#!/usr/bin/env python3

from datetime import datetime


class Note:
    def __init__(self, memo="", title="", tags=[]):
        self.memo = memo
        self.title = title
        self.tags = tags
        self.time_now = datetime.now()

    def match(self, filter):
        return filter in self.title or filter in self.tags

    def __del__(self):
        return f'Note titled {self.title} created on {self.time_now} deleted!'

    def __repr__(self):
        return 

class Notebook:
    def __init__(self):
        self.my_notes = []

    def addNote(self, memo_body, title_body, tags):
        my_note = Note(memo=memo_body, title=title_body, tags=tags)
        self.my_notes.append(my_note)

    def searchNote(self, filter):
        for note in self.my_notes:
            if note.match(filter):
                return note

    
