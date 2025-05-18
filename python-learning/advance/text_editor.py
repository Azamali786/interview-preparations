import tkinter as tk
from tkinter import filedialog, messagebox, font
import os

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Text Editor")
        self.root.geometry("800x600")
        self.current_file = None
        self.setup_ui()
        
    def setup_ui(self):
        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        
        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        
        # Format menu
        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.format_menu.add_command(label="Font", command=self.change_font)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        
        # Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        
        self.root.config(menu=self.menu_bar)
        
        # Create toolbar
        self.toolbar = tk.Frame(self.root)
        self.bold_btn = tk.Button(self.toolbar, text="B", command=self.toggle_bold, width=3)
        self.bold_btn.pack(side=tk.LEFT, padx=2, pady=2)
        self.italic_btn = tk.Button(self.toolbar, text="I", command=self.toggle_italic, width=3)
        self.italic_btn.pack(side=tk.LEFT, padx=2, pady=2)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Create text area with scrollbar
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_area = tk.Text(
            self.root, 
            yscrollcommand=self.scrollbar.set,
            wrap=tk.WORD,
            undo=True,
            font=('Arial', 12)
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        self.scrollbar.config(command=self.text_area.yview)
        
        # Status bar
        self.status_bar = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Keyboard shortcuts
        self.root.bind('<Control-n>', lambda event: self.new_file())
        self.root.bind('<Control-o>', lambda event: self.open_file())
        self.root.bind('<Control-s>', lambda event: self.save_file())
        self.root.bind('<Control-S>', lambda event: self.save_as_file())
        self.root.bind('<Control-x>', lambda event: self.cut_text())
        self.root.bind('<Control-c>', lambda event: self.copy_text())
        self.root.bind('<Control-v>', lambda event: self.paste_text())
        self.root.bind('<Control-a>', lambda event: self.select_all())
        
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.update_status("New file created")
        
    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, file.read())
                self.current_file = file_path
                self.update_status(f"Opened: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{str(e)}")
    
    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.update_status(f"Saved: {os.path.basename(self.current_file)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{str(e)}")
        else:
            self.save_as_file()
    
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.current_file = file_path
                self.update_status(f"Saved as: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{str(e)}")
    
    def exit_editor(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
    
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")
        self.update_status("Text cut to clipboard")
    
    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
        self.update_status("Text copied to clipboard")
    
    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")
        self.update_status("Text pasted from clipboard")
    
    def select_all(self):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
        self.update_status("All text selected")
    
    def toggle_bold(self):
        current_tags = self.text_area.tag_names(tk.SEL_FIRST)
        if "bold" in current_tags:
            self.text_area.tag_remove("bold", tk.SEL_FIRST, tk.SEL_LAST)
            self.update_status("Bold removed")
        else:
            bold_font = font.Font(self.text_area, self.text_area.cget("font"))
            bold_font.configure(weight="bold")
            self.text_area.tag_configure("bold", font=bold_font)
            self.text_area.tag_add("bold", tk.SEL_FIRST, tk.SEL_LAST)
            self.update_status("Bold applied")
    
    def toggle_italic(self):
        current_tags = self.text_area.tag_names(tk.SEL_FIRST)
        if "italic" in current_tags:
            self.text_area.tag_remove("italic", tk.SEL_FIRST, tk.SEL_LAST)
            self.update_status("Italic removed")
        else:
            italic_font = font.Font(self.text_area, self.text_area.cget("font"))
            italic_font.configure(slant="italic")
            self.text_area.tag_configure("italic", font=italic_font)
            self.text_area.tag_add("italic", tk.SEL_FIRST, tk.SEL_LAST)
            self.update_status("Italic applied")
    
    def change_font(self):
        font_window = tk.Toplevel(self.root)
        font_window.title("Font Settings")
        
        tk.Label(font_window, text="Font Family:").grid(row=0, column=0, padx=5, pady=5)
        font_family = tk.StringVar(value="Arial")
        tk.Entry(font_window, textvariable=font_family).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(font_window, text="Font Size:").grid(row=1, column=0, padx=5, pady=5)
        font_size = tk.IntVar(value=12)
        tk.Entry(font_window, textvariable=font_size).grid(row=1, column=1, padx=5, pady=5)
        
        def apply_font():
            new_font = (font_family.get(), font_size.get())
            self.text_area.configure(font=new_font)
            font_window.destroy()
            self.update_status(f"Font changed to {new_font[0]} {new_font[1]}pt")
        
        tk.Button(font_window, text="Apply", command=apply_font).grid(row=2, column=0, columnspan=2, pady=5)
    
    def show_about(self):
        messagebox.showinfo("About", "Python Text Editor\nVersion 1.0\n\nA simple text editor built with Tkinter")
    
    def update_status(self, message):
        self.status_bar.config(text=message)
        self.root.after(3000, lambda: self.status_bar.config(text="Ready"))

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()