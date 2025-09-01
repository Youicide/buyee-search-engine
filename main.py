import tkinter
import customtkinter
import webbrowser
from CTkListbox import *

#button code

brand_list=[]
def addbrand():
    if brand_input.get()!=""or" ":
        brand=brand_input_string.get()
        if brand.strip:
            brand_list.append(brand)
            brand_output.insert("end", brand)
            print("starting search")
            print(brand_list)
            brand_input_string.set("")

def search():
    for item in brand_list:
        if not item:
            print("empty item, ignoring")
        else:
            webbrowser.open("https://buyee.jp/mercari/search?items=40&keyword="+item+"&price_max=4923&lang=en&page=1&status=on_sale&price_min=422&category_id=2&currencyCode=USD&searchType=filter")

def show_value():
    print(brand_list)

# theme and color
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x720")
app.title("buyee filter engine")

# app grid
app.columnconfigure((0,1,2,3,4), weight = 1, uniform="a")
app.rowconfigure((0,1,2,3,4,5,6,7,8), weight = 1, uniform="a")

# titles
title = customtkinter.CTkLabel(app, text="Buyee filter engine", font=("ROG Fonts", 25))
brandinput_title= customtkinter.CTkLabel(app, text="Input brand", font=("", 15))

#brand input
brand_input_string = tkinter.StringVar()
brand_input = customtkinter.CTkEntry(app, width=350, height=40, textvariable= brand_input_string )

#brand output
brand_output_string = tkinter.StringVar()
brand_output = CTkListbox(app, font=("", 15), command=show_value)

#buttons
add_brand_button = customtkinter.CTkButton(app, text="Add brand", height=40, width=60, command=addbrand)
search_button = customtkinter.CTkButton(app, text="Search", height=20, font=("", 25), command=search)


# Placing

    # title
title.grid(row=0, column=1, columnspan=3, sticky="ew")

    # add brand button
add_brand_button.grid(row=1, column=1, sticky="e")

    #search button title
brandinput_title.grid(row=1, column=0 )

    # brand input
brand_input.grid(row=1, column=1, sticky="ew")

    # brand output
brand_output.grid(row=1, column=2, padx=50, pady=30, columnspan=3, rowspan=6, sticky="news")
for item in brand_list:
    brand_output.insert(item + "\n")

    # Search button
search_button.grid(row=7, column=2, padx=50, columnspan=3, sticky="wns")

# stay open
app.mainloop()
