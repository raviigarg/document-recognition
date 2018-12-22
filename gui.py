# import requires packages
from tkinter import *
from tkinter import filedialog as fd

# Open Directory Box, choose file and get path of local file
def get_file():
    filename = fd.askopenfilename() # Open directory box
    print(filename)

# Get url of remote file
def get_url():
    # Replace button with Entry
    url_button.destroy()
    in_url = Entry(main_window, width=17)
    in_url.grid(row=3, column=0, pady=30)
    print("URL window called")

# Submit local file path
def submit_file():
    print("File submitted")

# Submit remote file url
def submit_url():
    print("URL submitted")

labelfont = ('times', 20, 'bold')
footerfont = ('times', 15, 'bold')

# Load main window
main_window = Tk()
main_window.title('Document Recognition Application')
main_window.geometry("900x600")
main_window.resizable(width=FALSE, height=FALSE)
main_window.config(bg='black')

# Show title text
title_text = Label(main_window, text='Document Recognition Application')
title_text.config(bg='black', fg='gainsboro')  
title_text.config(font=labelfont)           
title_text.config(height=2)       
title_text.grid(row=0, column=0, columnspan=3, padx=200, pady=75)

# Show browse document button and call get_file method
browse_button = Button(main_window, text="Browse Document", command=get_file)
browse_button.config(bg='black', fg='gainsboro')
browse_button.grid(row=1, column=0, pady=30)

arrow1 = Label(main_window, text='===>>>>>')
arrow1.config(bg='black', fg='gainsboro')  
arrow1.config(font=labelfont)           
arrow1.config(height=2)       
arrow1.grid(row=1, column=1)

# Show button for local file path submission
submit_file = Button(main_window, text="Submit", command=submit_file)
submit_file.config(bg='black', fg='gainsboro')
submit_file.grid(row=1, column=2)

# Separation text
sep_text = Label(main_window, text='OR')
sep_text.config(bg='black', fg='gainsboro')  
sep_text.config(font=labelfont)           
sep_text.config(height=2)       
sep_text.grid(row=2, column=1)

# Show enter url button and call get_url method
url_button = Button(main_window, text="Enter URL", command=get_url)
url_button.config(bg='black', fg='gainsboro')
url_button.grid(row=3, column=0, pady=30)

arrow2 = Label(main_window, text='===>>>>>')
arrow2.config(bg='black', fg='gainsboro')  
arrow2.config(font=labelfont)           
arrow2.config(height=2)       
arrow2.grid(row=3, column=1)

# show button for remote file url submission
submit_url = Button(main_window, text="Submit", command=submit_url)
submit_url.config(bg='black', fg='gainsboro')
submit_url.grid(row=3, column=2)

# Show footer text
footer_text = Label(main_window, text='Made with \u2665 by Ravi.')
footer_text.config(bg='black', fg='gainsboro')  
footer_text.config(font=footerfont)           
footer_text.config(height=1)       
footer_text.grid(row=4, column=1, pady=(120,0))

# Call main window
main_window.mainloop()
