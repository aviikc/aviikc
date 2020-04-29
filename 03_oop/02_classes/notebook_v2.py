# !/usr/bin/env python3

from datetime import datetime

global count
count = 0


class Note:

    def __init__(self, memo="", title="", tags=[]):
        self.memo = memo
        self.title = title
        self.tags = tags
        self.time_now = datetime.now()
        count += 1
        self.note_id = count

    def match(self, filter):
        return filter in self.title or filter in self.tags

    def __del__(self):
        return f'Note titled {self.title} created on {self.time_now} deleted!'

    def __repr__(self):
        return f'{self.title} created at {self.time_now} with id: {self.note_id}'


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

    def modifyNoteContent(self, noteId, new_content):
        for note in self.my_notes:
            if note.note_id == noteId:
                note.memo = new_content
                break

    def modifyNoteTitle(self, noteId, new_title):
        for note in self.my_notes:
            if note.note_id == noteId:
                note.title = new_title
                break

    def delNote(self, noteId):
        for note in self.my_notes:
            if note.note_id == noteId:
                self.my_notes.remove(note)
                del note
                break


class NotebookInterface:
    def __init__(self):
        self.my_notebook = Notebook()
        self.menu()

    def menu(self):
        print('''
        1. Add Note
        2. Search Note
        3. Modify Content
        4. Modify Title
        5. List all notes
        6. Quit Program
        ''')
        self.run()
        
    def run(self):
        while True:
            choice = input("Enter Choice: ")
            if choice == "1":
                memo = input("Enter the content: ")
                title = input("Enter a Title: ")
                tags = input("Enter tags seperated by commas: ").strip().split(",")
                self.my_notebook.addNote(memo, title, tags)
                continue
            elif choice == "2":
                current_filter = input("Enter an indentifiable tag or title: ")
                self.my_notebook.searchNote(current_filter)
                continue
            elif choice == "3":
                n_id = int(input("Enter Note Id: "))
                memo = input("Enter the content: ")
                self.my_notebook.modifyNoteContent(n_id, memo)
                continue
            elif choice == "4":
                n_id = int(input("Enter Note Id: "))
                titl = input("Enter the Title: ")
                self.my_notebook.modifyNoteTitle(n_id, titl)
                continue
            elif choice == "5":
                for note in self.my_notebook.my_notes:
                    print(f'{note.note_id}-{note.title} created on {note.time_now}')
                continue
            elif choice == "6":
                break
            else:
                print("Enter a valid choice.")
                continue

myApp = NotebookInterface()

