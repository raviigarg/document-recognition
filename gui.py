# import requires packages
from tkinter import *
from get_text import *
from tkinter import filedialog as fd
import webbrowser
from identify import *

# Open Directory Box, choose file and get path of local file
def get_file():
    # Update global variable filepath
    global filepath
    filename = fd.askopenfilename() # Open directory box
    filepath = filename

# Get url of remote file
def get_url():
    # Replace button with Entry
    global in_url
    url_button.destroy()
    in_url.grid(row=3, column=0, pady=30)

# Submit local file path
def submit_file():
    # Get text of local file
    test_file = ocr_space_file(filename=filepath, language='eng') # Make request to OCR.space API
    json_str = json.loads(test_file) # Decode JSON data
    extracted_text = json_str["ParsedResults"][0]["ParsedText"] # Get text from JSON
    extracted_text = extracted_text.replace(" \r\n",  " ")
    with open("predict/predict", "w") as text_file:
        text_file.write("yes	%s" % extracted_text)
    print(extracted_text)
    # get predicted label on extracted text using make_predictions method in identify.py
    predicted_label = make_predictions()
    print(predicted_label)

# Submit remote file url
def submit_url():
    # Get text of remote file
    global filepath
    filepath = in_url.get() # Get file url from Entry field
    test_file = ocr_space_url(str(filepath), language='eng') # Make request to OCR.space API
    json_str = json.loads(test_file) # Decode JSON data
    extracted_text = json_str["ParsedResults"][0]["ParsedText"] # Get text from JSON
    extracted_text = extracted_text.replace(" \r\n",  " ")
    with open("predict/predict", "w") as text_file:
        text_file.write("yes	%s" % extracted_text)
    print(extracted_text)
    # get predicted label on extracted text using make_predictions method in identify.py
    predicted_label = make_predictions()
    print(predicted_label)

# open linedin
def open_linkedin(event):
     webbrowser.open_new(r"https://www.linkedin.com/in/raviigarg/")

# open github
def open_github(event):
     webbrowser.open_new(r"https://github.com/raviigarg")

# open twitter
def open_twitter(event):
     webbrowser.open_new(r"https://twitter.com/raviigarg")

labelfont = ('times', 20, 'bold')
footerfont = ('times', 15, 'bold')
filepath = ''

# Load main window
main_window = Tk()
main_window.title('Document Recognition Application')
main_window.geometry("900x600")
main_window.resizable(width=FALSE, height=FALSE)
main_window.config(bg='black')

# Show title text
title_text = Label(main_window, text='Document Recognition Application')
title_text.config(bg='black', fg='yellow')  
title_text.config(font=labelfont)           
title_text.config(height=2)       
title_text.grid(row=0, column=0, columnspan=3, padx=200, pady=75)

# Show browse document button and call get_file method
browse_button = Button(main_window, text="Browse Document", command=get_file)
browse_button.config(bg='black', fg='yellow')
browse_button.grid(row=1, column=0, pady=30)

arrow1 = Label(main_window, text='===>>>>>')
arrow1.config(bg='black', fg='yellow')  
arrow1.config(font=labelfont)           
arrow1.config(height=2)       
arrow1.grid(row=1, column=1)

# Show button for local file path submission
submit_file = Button(main_window, text="Submit", command=submit_file)
submit_file.config(bg='black', fg='yellow')
submit_file.grid(row=1, column=2)

# Separation text
sep_text = Label(main_window, text='OR')
sep_text.config(bg='black', fg='yellow')  
sep_text.config(font=labelfont)           
sep_text.config(height=2)       
sep_text.grid(row=2, column=1)

# Show enter url button and call get_url method
url_button = Button(main_window, text="Enter URL", command=get_url)
url_button.config(bg='black', fg='yellow')
url_button.grid(row=3, column=0, pady=30)

# Entry for URl
in_url = Entry(main_window, width=17)

arrow2 = Label(main_window, text='===>>>>>')
arrow2.config(bg='black', fg='yellow')  
arrow2.config(font=labelfont)           
arrow2.config(height=2)       
arrow2.grid(row=3, column=1)

# Show button for remote file url submission
submit_url = Button(main_window, text="Submit", command=submit_url)
submit_url.config(bg='black', fg='yellow')
submit_url.grid(row=3, column=2)

# Show footer text
footer_text = Label(main_window, text='<< Made with \u2665 by Ravi >>')
footer_text.config(bg='black', fg='yellow')  
footer_text.config(font=footerfont)           
footer_text.config(height=1)       
footer_text.grid(row=4, column=1, pady=(110,0))

# Show linkedin icon
image_linkedin = PhotoImage(file="icons/linkedin.png")
label_linkedin = Label(image=image_linkedin, bg='black', cursor="hand2")
label_linkedin.grid(row=5, column=1, pady=(7,0))
label_linkedin.bind("<Button-1>", open_linkedin)

# Show github icon
image_github = PhotoImage(file="icons/github.png")
label_github = Label(image=image_github, bg='black', cursor="hand2")
label_github.grid(row=5, column=1, padx=(0,75), pady=(7,0))
label_github.bind("<Button-1>", open_github)

# Show twitter icon
image_twitter = PhotoImage(file="icons/twitter.png")
label_twitter = Label(image=image_twitter, bg='black', cursor="hand2")
label_twitter.grid(row=5, column=1, padx=(75, 0), pady=(7,0))
label_twitter.bind("<Button-1>", open_twitter)

# Call main window
main_window.mainloop()
