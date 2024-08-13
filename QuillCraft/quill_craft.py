# MrJ
# Text Editor
# 7/25/2024


import tkinter as tk
from tkinter import font as tkfont
from tkinter import simpledialog, colorchooser, filedialog, messagebox


def view_help():
    messagebox.showinfo(
        "Help",
        "Open a file or simply start typing to create a new file. Save as any extension you like. "
        "Plenty of customization options to suit your needs in the Format tab. "
        "All your favorite action shortcuts in the Edit tab like undo and redo. "
        "Happy typing."
    )


def show_about():
    messagebox.showinfo(
        "About",
        "QuillCraft - A Simple Text Editor\n"
        f"\tCreated by MrJ\n\t        2024©"
    )


class QuillCraft:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - QuillCraft")  # Update title when application is first opened
        self.root.geometry("768x768")

        self.setup_widgets()
        self.setup_menu()
        self.setup_toolbar()

        # Initialize default font
        self.current_font = tkfont.Font(family="Courier New", size=14)
        self.textarea.config(font=self.current_font)

        # Set default tab spaces
        self.set_tab4()

        # Text area is set arbitrarily small to allow resizing
        self.textarea.config(height=5, width=10)

        # Default theme
        self.light_theme()

        self.filename = None

        # Enable wordwrap
        self.word_wrap_enabled = True

    def set_tab2(self):
        self.textarea.config(tabs=20)

    def set_tab4(self):
        self.textarea.config(tabs=40)

    def set_tab8(self):
        self.textarea.config(tabs=80)

    def dark_theme(self):
        self.textarea.config(
            background="#2e2e2e",
            foreground="white",
            insertbackground="white",  # Text cursor color
            selectbackground="#1E90FF",  # Dodger Blue highlight color
            selectforeground="black"
        )

    def light_theme(self):
        self.textarea.config(
            background="white",
            foreground="black",
            insertbackground="black",  # Text cursor color
            selectbackground="#1E90FF",  # Dodger Blue highlight color
            selectforeground="white"
        )

    def setup_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)

        # Configure horizontal scrolling behavior
        self.scrollbar2 = tk.Scrollbar(toolbar, orient=tk.HORIZONTAL, command=self.textarea.xview)
        self.scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)
        self.textarea.config(xscrollcommand=self.scrollbar2.set)

        toolbar.pack(side=tk.BOTTOM, fill=tk.X)

    def setup_widgets(self):
        # Main frame setup
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Sub-frame for text area and vertical scrollbar
        text_frame = tk.Frame(self.main_frame)
        text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Text area
        self.textarea = tk.Text(text_frame, wrap="word", undo=True)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for vertical scrolling
        self.scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.textarea.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.textarea.config(yscrollcommand=self.scrollbar.set)

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open...", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit, accelerator="Ctrl+Q")

        # Edit menu
        editmenu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Undo", command=self.textarea.edit_undo, accelerator="Ctrl+Z")
        editmenu.add_command(label="Redo", command=self.textarea.edit_redo, accelerator="Ctrl+H")
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        editmenu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        editmenu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        editmenu.add_separator()
        editmenu.add_command(label="Find...", command=self.find_text, accelerator="Ctrl+F")
        editmenu.add_command(label="Replace...", command=self.replace_text, accelerator="Ctrl+R")

        # Format menu
        format_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Background Color", command=self.choose_bg_color)
        format_menu.add_command(label="Text Color", command=self.choose_text_color)
        format_menu.add_separator()
        format_menu.add_command(label="Font Style", command=self.choose_font_style)
        format_menu.add_command(label="Font Size", command=self.choose_font_size)
        format_menu.add_separator()
        format_menu.add_command(label="Word Wrap", command=self.toggle_word_wrap)
        format_menu.add_separator()

        # Tabs sub-menu
        tabs_menu = tk.Menu(format_menu, tearoff=0)
        format_menu.add_cascade(label="Tabs", menu=tabs_menu)
        tabs_menu.add_command(label="2 Spaces", command=self.set_tab2)
        tabs_menu.add_command(label="4 Spaces", command=self.set_tab4)
        tabs_menu.add_command(label="8 Spaces", command=self.set_tab8)

        # Theme sub-menu
        theme_menu = tk.Menu(format_menu, tearoff=0)
        format_menu.add_cascade(label="Themes", menu=theme_menu)
        theme_menu.add_command(label="Dark", command=self.dark_theme)
        theme_menu.add_command(label="Light", command=self.light_theme)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="View Help", command=view_help)
        help_menu.add_separator()
        help_menu.add_command(label="About", command=show_about)

        self.root.config(menu=menu_bar)

        # Bind shortcuts
        self.root.bind_all('<Control-n>', self.new_file_shortcut)
        self.root.bind_all('<Control-o>', self.open_file_shortcut)
        self.root.bind_all('<Control-s>', self.save_file_shortcut)
        self.root.bind_all('<Control-Shift-S>', self.save_as_file_shortcut)
        self.root.bind_all('<Control-q>', self.quit_shortcut)

        self.root.bind_all('<Control-z>', self.undo_shortcut)
        self.root.bind_all('<Control-h>', self.redo_shortcut)
        self.root.bind_all('<Control-x>', self.cut_shortcut)
        self.root.bind_all('<Control-c>', self.copy_shortcut)
        self.root.bind_all('<Control-v>', self.paste_shortcut)
        self.root.bind_all('<Control-f>', self.find_shortcut)
        self.root.bind_all('<Control-r>', self.replace_shortcut)

    def new_file_shortcut(self, event):
        self.new_file()

    def open_file_shortcut(self, event):
        self.open_file()

    def save_file_shortcut(self, event):
        self.save_file()

    def save_as_file_shortcut(self, event):
        self.save_as_file()

    def quit_shortcut(self, event):
        self.quit()

    def undo_shortcut(self, event):
        try:
            self.textarea.edit_undo()
        except:
            pass

    def redo_shortcut(self, event):
        try:
            self.textarea.edit_redo()
        except:
            pass

    def cut_shortcut(self, event):
        self.cut_text()

    def copy_shortcut(self, event):
        self.copy_text()

    def paste_shortcut(self, event):
        self.paste_text()

    def find_shortcut(self, event):
        self.find_text()

    def replace_shortcut(self, event):
        self.replace_text()

    def toggle_word_wrap(self):
        if self.word_wrap_enabled:
            self.textarea.config(wrap="none")
            self.word_wrap_enabled = False
        else:
            self.textarea.config(wrap="word")
            self.word_wrap_enabled = True

    def choose_font_style(self):
        # Create a new window for font style selection
        font_window = tk.Toplevel(self.root)
        font_window.title("Font Style")
        font_window.geometry("320x240")

        font_label = tk.Label(
            font_window,
            text="Select Font Style:",
        )
        font_label.pack(anchor=tk.N)

        font_families = tkfont.families()
        self.font_listbox = tk.Listbox(font_window, selectmode=tk.SINGLE, height=10, width=35)
        for family in font_families:
            self.font_listbox.insert(tk.END, family)
        self.font_listbox.pack()

        # Confirm button
        confirm_button = tk.Button(
            font_window,
            text="Confirm",
            command=self.apply_font_style,
            width=10
        )
        confirm_button.pack(pady=10, padx=10)

    def choose_font_size(self):
        # Create a new window for font size selection
        size_window = tk.Toplevel(self.root)
        size_window.title("Font Size")
        size_window.geometry("240x240")

        size_label = tk.Label(
            size_window,
            text="Select Font Size:"
        )
        size_label.pack(anchor=tk.N)

        self.size_listbox = tk.Listbox(size_window, selectmode=tk.SINGLE, height=10, width=15)
        for size in range(8, 78, 2):
            self.size_listbox.insert(tk.END, size)
        self.size_listbox.pack()

        # Confirm button
        confirm_button = tk.Button(
            size_window,
            text="Confirm",
            command=self.apply_font_size,
            width=10
        )
        confirm_button.pack(pady=10, padx=10)

    def apply_font_style(self):
        selected_font_family = self.font_listbox.get(tk.ACTIVE)
        if selected_font_family:
            self.current_font.configure(family=selected_font_family)
            self.textarea.config(font=self.current_font)

    def apply_font_size(self):
        selected_font_size = self.size_listbox.get(tk.ACTIVE)
        if selected_font_size:
            self.current_font.configure(size=int(selected_font_size))
            self.textarea.config(font=self.current_font)

    def choose_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.textarea.config(foreground=color)

    def choose_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.textarea.config(background=color)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.update_title()  # Update title for new file

    def open_file(self):
        filetypes = (
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("Java files", "*.java"),
            ("HTML files", "*.html"),
            ("CSS files", "*.css"),
            ("JavaScript files", "*.js"),
            ("JSON files", "*.json"),
            ("SQL files", "*.db"),
            ("Bash Script files", "*.sh")
        )
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            with open(file_path, "r") as file:
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(1.0, file.read())
                self.filename = file_path
            self.update_title()  # Update title for opened file

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.textarea.get(1.0, tk.END))
            self.update_title()  # Update title for saved file
        else:
            self.save_as_file()

    def save_as_file(self):
        filetypes = (
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("Java files", "*.java"),
            ("HTML files", "*.html"),
            ("CSS files", "*.css"),
            ("JavaScript files", "*.js"),
            ("JSON files", "*.json"),
            ("SQL files", "*.db"),
            ("Bash Script files", "*.sh")
        )
        file_path = filedialog.asksaveasfilename(filetypes=filetypes)
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.textarea.get(1.0, tk.END))
                self.filename = file_path
            self.update_title()  # Update title for saved file

    def update_title(self):
        # Update the window title based on the current filename
        if self.filename:
            title = f"{self.filename.split('/')[-1]} - QuillCraft"
        else:
            title = "Untitled - QuillCraft"
        self.root.title(title)

    def quit(self):
        self.root.quit()

    def cut_text(self):
        self.textarea.event_generate("<<Cut>>")

    def copy_text(self):
        self.textarea.event_generate("<<Copy>>")

    def paste_text(self):
        self.textarea.event_generate("<<Paste>>")

    def find_text(self):
        target = simpledialog.askstring("Find", "\tEnter text to find:\t\t")
        if target:
            start_pos = self.textarea.search(target, "1.0", tk.END)
            if start_pos:
                end_pos = f"{start_pos}+{len(target)}c"
                self.textarea.tag_remove("sel", "1.0", tk.END)
                self.textarea.tag_add("sel", start_pos, end_pos)
                self.textarea.mark_set("insert", end_pos)
                self.textarea.see("insert")
            else:
                messagebox.showinfo("Not Found", f"Cannot find '{target}'")

    def replace_text(self):
        target = simpledialog.askstring("Replace", "\tEnter text to replace:\t\t")
        if target:
            replace_text = simpledialog.askstring("Replace", f"\tReplace '{target}' with:\t\t")
            if replace_text:
                self.textarea.replace(
                    "1.0", tk.END, self.textarea.get("1.0", tk.END).replace(target, replace_text).strip()
                )


def main():
    root = tk.Tk()
    app = QuillCraft(root)
    root.mainloop()


if __name__ == "__main__":
    main()
