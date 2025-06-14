import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator  #this is the library for translation
from language_data import language_dict

languages = sorted(language_dict.keys())

# this handles the translation process...
def translate_text():
    input_text = input_text_box.get("1.0", tk.END).strip()
    src_lang = source_lang.get()
    tgt_lang = target_lang.get()

    if not input_text:
        messagebox.showwarning(" ⚠️ Warning", "Please enter text to translate.")
        return

    try:
        translated = GoogleTranslator(
            source=language_dict[src_lang],
            target=language_dict[tgt_lang]
        ).translate(input_text)

# this is where the translated text is displayed
        output_text_box.config(state="normal")
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translated)
        output_text_box.config(state="disabled")

    except Exception as e:
        messagebox.showerror(" ❌ Error", f"Translation failed:\n{e}")

# it will create the GUI for the translator app...
app = tk.Tk()
app.title("Translator App")
app.geometry("850x500")
app.resizable(False, False)

#it will set the theme for the app...
font_label = ("Arial", 14, "bold")
font_entry = ("Arial", 13)
font_button = ("Arial", 12, "bold") #it is fot the button

# Create and place widgets in the main window
ttk.Label(app, text="From Language:", font=font_label).pack(pady=5)
source_lang = ttk.Combobox(app, values=languages, state='readonly', width=30, font=font_entry)
source_lang.set("English")
source_lang.pack()

ttk.Label(app, text="To Language:", font=font_label).pack(pady=5)
target_lang = ttk.Combobox(app, values=languages, state='readonly', width=30, font=font_entry)
target_lang.set("Hindi")
target_lang.pack()

# Create input and output text boxes in the main window..
ttk.Label(app, text="Enter text:", font=font_label).pack(pady=5)
input_text_box = tk.Text(app, height=6, width=70, font=font_entry)
input_text_box.pack()

#it will create the button to trigger the translation...
ttk.Button(app, text="Translate", command=translate_text).pack(pady=12)


# it will create the output text box to display the translated text....
ttk.Label(app, text="Translated text:", font=font_label).pack(pady=5)
output_text_box = tk.Text(app, height=6, width=70, font=font_entry, state="disabled")
output_text_box.pack()

app.mainloop()
