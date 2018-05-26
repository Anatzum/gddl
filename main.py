import tkinter as tk
from tkinter import filedialog
from tkinter import dialog
import gddl
import file_handling


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.download_link_label = tk.Label(self, text="Download Link: ")
        self.download_link_label.grid(row=0, column=0, pady=10, padx=10)
        self.download_link = tk.Entry(self)
        self.download_link.grid(row=0, column=1, padx=10)
        self.destination_label = tk.Label(self, text="Destination: ")
        self.destination_label.grid(row=1, column=0, pady=10, padx=10)
        self.browse_directory_btn = tk.Button(self, text="Browse", command=self.browse_directory, width=18)
        self.browse_directory_btn.grid(row=1, column=1, padx=10)
        self.status = tk.Label(self, text="")
        self.status.grid(row=2, columnspan=2, pady=10)
        self.start = tk.Button(self, text="START", fg="red",
                               command=self.start_download)
        self.start.grid(row=3, columnspan=2, pady=15)

    def browse_directory(self):
        self.directory = filedialog.askdirectory()
        self.location = self.directory + "/downloadfile"

    def ask(title, text, strings=('Yes', 'No'), bitmap='questhead', default=0):
        d = dialog.Dialog(
            title=title, text=text, bitmap=bitmap, default=default, strings=strings)
        return strings[d.num]

    def start_download(self):
        self.clean_link()
        self.update_status(0)
        gddl.download_file_from_google_drive(self.file_id, self.location)
        if file_handling.is_archive(self.location) is True:
            response = self.ask("Do you want to extract the data?")
            if response is "Yes":
                self.update_status(1)
                file_handling.extract(self.location, self.directory)
        self.update_status(2)

    def clean_link(self):
        self.file_id = self.download_link.get()[self.download_link.get().find("?id=") + 4:]

    def update_status(self, choice):
        if choice == 0:
            self.status['text'] = "Downloading"
        elif choice == 1:
            self.status['text'] = "Extracting"
        elif choice == 2:
            self.status['text'] = "Finished"
        root.update_idletasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
