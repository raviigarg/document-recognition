# Document Recognition
A simple python based Document Recognition Application to identify whether a document is Form 16 or not. Form 16 is a certificate issued by an employer validating the fact that TDS has been deducted and deposited with the authorities on behalf of the employee.

## Demo
![user-interface](user-interface.png)

This application inputs either a local file of document or url of document if it is not present on your personal computer (document should be in image or pdf format). It will work as input for the application and it will predict that whether the document submitted is form 16 or not. Application requires a internet connection as it makes request to an online API to extract text from image or pdf. 

Document file size should not be greater than 1 MB. In case of pdf it should not be more than 3 pages. Image should have dpi greater than 300 dpi (dots per inch).

## Getting Started
These instructions will help you to run the project on your local machine.
### Prerequisites
You will need the following, before running the project:

- [Python](https://www.python.org/) v3.x.
- [Tkinter](https://docs.python.org/2/library/tkinter.html)
- [Requests](http://docs.python-requests.org)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/stable/install.html)
- [PIL](https://pypi.org/project/Pillow/)

It is prefered to make virtual environment to install all the dependencies. To create virtual environment instructions can be found [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/). Now activate your virtual environment.

To install all the dependencies you can run following command -

```
$ pip install -r requirements.txt
```

Make sure that you have installed all the prerequisites.

### Run
Once you have installed all the prerequisites, now it's time to run the application.

First, clone the project.

Open terminal on your machine and run the following command -

```
$ git clone https://gitlab.com/raviigarg/document-recognition.git
Cloning into 'document-recognition'...
```

Now, go into the project's directory and run the following command - 

```
$ python index.py
```

This will start the application. Now you can make predictions on your documents.

## Built With
- [Tkinter](https://docs.python.org/2/library/tkinter.html) - Graphical User Interface
- [Pandas](https://pandas.pydata.org/) - For importing dataset
- [scikit-learn](https://scikit-learn.org) - For classification

## Acknowledgements
- Thanks to [Free OCR API](https://ocr.space/ocrapi) for parsing image and pdf and return the extracted text in json format.
- Thanks to [Flaticon](https://www.flaticon.com/home) for providing icons of social links.
- Thanks to [TRACES](https://contents.tdscpc.gov.in/) for providing form no. 16 and other forms. 
- Thanks to [Zaargh](https://github.com/Zaargh/ocr.space_code_example/blob/master/ocrspace_example.py) for providing code snippet to extract text from OCR.space API using `requests.post`.
