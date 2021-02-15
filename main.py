def background(filepath):
    import cv2
    import pytesseract
    from pytesseract.pytesseract import Output
    # %matplotlib inline
    pytesseract.pytesseract.tesseract_cmd=r'E:/Tesseract-OCR/tesseract.exe'
    import numpy as np
    from matplotlib import pyplot as plt
    import numpy as np
    import re
    import nltk
    import seaborn as sns
    from sklearn.linear_model import LogisticRegression
    from nltk.corpus import stopwords
    
    from nltk.stem.porter import PorterStemmer
    from nltk.stem import WordNetLemmatizer 
    from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
    from textblob import TextBlob
    from openpyxl import Workbook
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    from nltk.corpus import wordnet
    img = cv2.imread(filepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pytesseract
    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    def remove_noise(image):
        return cv2.medianBlur(image,5)
    #thresholding
    def thresholding(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    rem_noise = remove_noise(img)
    gray = get_grayscale(rem_noise)
    thresh = thresholding(gray)
    #print(pytesseract.image_to_string(img))
    #plt.imshow(img)
    #plt.show()
    pytesseract.image_to_string(img)
    def text_processing(tweet):
        def form_sentence(tweet):
            tweet_blob = TextBlob(tweet)
            return ' '.join(tweet_blob.words)
        new_tweet = form_sentence(tweet)

        def no_user_alpha(tweet):
            tweet_list = [ele for ele in tweet.split() if ele != 'user']
            clean_tokens = [t for t in tweet_list if re.match(r'[^\W\d]*$', t)]
            clean_s = ' '.join(clean_tokens)
            clean_mess = [word for word in clean_s.split() if word.lower() not in set(stopwords.words('english'))]
            return clean_mess
        no_punc_tweet = no_user_alpha(new_tweet)

        def normalization(tweet_list):
            lem = WordNetLemmatizer()
            normalized_tweet = []
            for word in tweet_list:
                normalized_text = lem.lemmatize(word)
                normalized_tweet.append(normalized_text)
            return normalized_tweet
        return normalization(no_punc_tweet)
    
   
    var1=text_processing(pytesseract.image_to_string(img))
    print(var1)
    var=[]
    for i in var1:
        if i not in var:
            var.append(i)
            
        
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "WORDS"
    sheet["B1"] = "SYNONYMS"
    sheet["C1"] = "ANTONYMS"
    sheet["D1"] = "HINDI"
    sheet["E1"] = "PUNJABI"
    sheet["F1"] = "TAMIL"
    sheet["G1"] = "TELUGU"

    workbook.save(filename="translate.xlsx")
    lwords=[]
    j=2
    for i in var:
        lwords.append(i)
        s="A"+str(j)
        sheet[s]=i
        j=j+1
        workbook.save(filename="translate.xlsx")
    j=2
    synonyms = []
    antonyms = []
    js=2
    for i in lwords:
        synonyms=[]
        for syn in wordnet.synsets(i):
            for lm in syn.lemmas():
                 synonyms.append(lm.name())#adding into synonyms
        if len(synonyms)>0:
            s="B"+str(js)
            sheet[s]=synonyms[0]
            workbook.save(filename="translate.xlsx")
        js=js+1
    js=2
    for i in lwords:
        antonyms=[]
        for syn in wordnet.synsets(i):
            for lm in syn.lemmas():
                if lm.antonyms():
                    antonyms.append(lm.antonyms()[0].name()) #adding into antonyms
        if len(antonyms)>0:
            s="C"+str(js)
            sheet[s]=antonyms[0]
            workbook.save(filename="translate.xlsx")
        js=js+1
    js=2
    from nltk.corpus import wordnet
    

    
    
    from google_trans_new import google_translator  
    ltranswordshindi=[]
    ltranswordspunjabi=[]
    ltranswordstamil=[]
    ltranswordstelugu=[]
    translator = google_translator()  
    for i in var:
      translate_text = translator.translate(i,lang_tgt='hi')  
      ltranswordshindi.append(translate_text)
      translate_text = translator.translate(i,lang_tgt='ta')
      ltranswordstamil.append(translate_text)
      translate_text = translator.translate(i,lang_tgt='te')
      ltranswordstelugu.append(translate_text)
      translate_text = translator.translate(i,lang_tgt='pa')
      ltranswordspunjabi.append(translate_text)
      j=2
    for i in range(len(lwords)):
        shindi="D"+str(j)
        spu="E"+str(j)
        sta="F"+str(j)
        ste="G"+str(j)
        sheet[shindi]=ltranswordshindi[i]
        sheet[spu]=ltranswordspunjabi[i]
        sheet[sta]=ltranswordstamil[i]
        sheet[ste]=ltranswordstelugu[i]
        j=j+1
        workbook.save(filename="translate.xlsx")
    j=2
