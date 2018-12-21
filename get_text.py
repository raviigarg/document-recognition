# import the necessary packages
import requests
import json

# make request to Free OCR.space API to extract text from image and pdf
# sample code is taken from https://github.com/Zaargh/ocr.space_code_example/blob/master/ocrspace_example.py
def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
	    Python3.5 - not tested on 2.7
    :param filename: file path & name.
    :param overlay: Is OCR.space overlay required in responses.
                    Defaults to False.
    :param api_key: OCR.space API key.
	            Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                     List of available languages codes can be found on https://ocr.space/OCRAPI
                     Defaults to 'en'.
    :return: Result in json format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f}, 
                          data=payload,
                          )
        return r.content.decode()

def ocr_space_url(url, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with remote file.
        Python 3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in responses.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                     List of available languages codes can be found on https://ocr.space/OCRAPI
                     Defaults to 'en'.
    :return: Result in json format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
              }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                     )
    return r.content.decode()

def main():
    test_file_local = ocr_space_file(filename='data/pdfs/sample-pdf.pdf', language='eng')
    test_file_remote = ocr_space_url('file_url', language='eng') # replace value of file_url with valid url of image or pdf
    json_string_local = json.loads(test_file_local)
    extracted_text_local = json_string_local["ParsedResults"][0]["ParsedText"]
    extracted_text_local = extracted_text_local.replace(" \r\n", " ")
    json_string_remote = json.loads(test_file_remote)
    extracted_text_remote = json_string_remote["ParsedResults"][0]["ParsedText"]
    extracted_text_remote = extracted_text_remote.replace(" \r\n", " ")
    print("Local file data : " + extracted_text_local)
    print("Remote file data : " + extracted_text_remote)
   
    
if __name__ == "__main__":
    main()
