# import requires packages
from tkinter import *
from get_text import *
from tkinter import filedialog as fd
import webbrowser
from tkinter import messagebox
from identify import *

# Open Directory Box, choose file and get path of local file
def get_file():
    # Update global variable filepath
    print("browse document..")
    global filepath
    filename = fd.askopenfilename() # Open directory box
    filepath = filename
    if str(filename) == "" or str(filename) == "()":
        print("nothing selected")
    else :
        print(str(filename) + " selected")

# Get url of remote file
def get_url():
    # Replace button with Entry
    print("enter url..")
    global in_url
    url_button.destroy()
    in_url.grid(row=3, column=0, pady=30)

# Submit local file path
def submit_file():
    global filepath
    # Get text of local file
    print("file submitted..")
    test_file = ocr_space_file(filename=filepath, language='eng') # Make request to OCR.space API
    json_str = json.loads(test_file) # Decode JSON data
    extracted_text = json_str["ParsedResults"][0]["ParsedText"] # Get text from JSON
    extracted_text = extracted_text.replace(" \r\n",  " ")
    print("text extracted..")
    with open("predict/predict", "w") as text_file:
        text_file.write("yes	%s" % extracted_text)
    print("text written to file..")
    # print(extracted_text)
    # get predicted label on extracted text using make_predictions method in identify.py
    print("making prediction..")
    predicted_label = make_predictions()
    print("prediction made..")
    # update filepath to empty
    filepath = ''
    # print(predicted_label)
    print("showing result..")
    show_result(predicted_label)

# Submit remote file url
def submit_url():
    # Get text of remote file
    global filepath
    filepath = in_url.get() # Get file url from Entry field
    if filepath == '':
        print("nothing entered")
        return
    else :
        print(str(filepath) + " entered")
    print("url submitted")
    test_file = ocr_space_url(str(filepath), language='eng') # Make request to OCR.space API
    json_str = json.loads(test_file) # Decode JSON data
    extracted_text = json_str["ParsedResults"][0]["ParsedText"] # Get text from JSON
    extracted_text = extracted_text.replace(" \r\n",  " ")
    print("text extracted..")
    with open("predict/predict", "w") as text_file:
        text_file.write("yes	%s" % extracted_text)
    print("text written to file..")
    # print(extracted_text)
    # get predicted label on extracted text using make_predictions method in identify.py
    print("making prediction..")
    predicted_label = make_predictions()
    print("prediction made..")
    # update filepath to empty
    filepath = ''
    # print(predicted_label)
    print("showing result..")
    show_result(predicted_label)

# open linedin
def open_linkedin(event):
     webbrowser.open_new(r"https://www.linkedin.com/in/raviigarg/")

# open github
def open_github(event):
     webbrowser.open_new(r"https://github.com/raviigarg")

# open twitter
def open_twitter(event):
     webbrowser.open_new(r"https://twitter.com/raviigarg")

# close result window
def close_result(): 
    result_win.destroy()
    print("result window closed..")

# show result box
def show_result(label):
    # window for result
    global result_win # update global variable result_win
    result_win = Tk()
    result_win.title('Predicted result')
    # get screen width and height
    result_screen_width = result_win.winfo_screenwidth()
    result_screen_height = result_win.winfo_screenheight()
    # result window width and height
    result_window_width = 600
    result_window_height = 150
    # x and y cordinate of result window to center in screen
    result_x_cordinate = int((result_screen_width/2) - (result_window_width/2))
    result_y_cordinate = int((result_screen_height/2) - (result_window_height/2))

    result_win.geometry("{}x{}+{}+{}".format(result_window_width, result_window_height, result_x_cordinate, result_y_cordinate))
    result_win.resizable(width=FALSE, height=FALSE)
    result_win.config(bg='black')
    result_text = ''
    if label == 1:
        result_text = 'Document is form 16'
    else :
        result_text = 'Document is not form 16'

    result_title_text = Label(result_win, text=result_text)
    result_title_text.config(bg='black', fg='yellow')  
    result_title_text.config(font=footerfont)           
    result_title_text.config(height=2)       
    result_title_text.grid(row=0, column=0, padx=200, pady=30)

    close_button = Button(result_win, text="Ok", command=close_result)
    close_button.config(bg='black', fg='yellow')
    close_button.grid(row=1, column=0)
    result_win.protocol("WM_DELETE_WINDOW", on_closing_result)
    print("result window opened..")

# display message to ask for closing of application
def on_closing_main():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        main_window.destroy()
        print("application window closed....")

# event log on explicitly closing of result window
def on_closing_result():
    result_win.destroy()
    print("result window closed..")

labelfont = ('times', 20, 'bold')
footerfont = ('times', 15, 'bold')
filepath = None
result_win = None

print("application window opened....")

# Load main window
main_window = Tk()
main_window.title('Document Recognition Application')
# get screen width and height
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
# main window width and height
window_width = 900
window_height = 600
# x and y cordinate of main window to center in screen
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

main_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
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

# protocol for explicitly closing main window using the window manager
main_window.protocol("WM_DELETE_WINDOW", on_closing_main)
# Call main window
main_window.mainloop()
