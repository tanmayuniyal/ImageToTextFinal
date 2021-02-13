#%%
def background(file_path):

    import re
    import nltk
    import cv2
    import numpy as np
    import pytesseract
    from pytesseract.pytesseract import Output
    from matplotlib import pyplot as plt
    import seaborn as sns
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    from nltk.stem import WordNetLemmatizer 
    from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
    from textblob import TextBlob
    from openpyxl import Workbook

    img = cv2.imread(file_path)
    #img = cv2.imread('/home/tanmay/Desktop/img1.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        

    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # noise removal
    def remove_noise(image):
        return cv2.medianBlur(image,5)
        #%%
        #thresholding
    def thresholding(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


    rem_noise = remove_noise(img)
    gray = get_grayscale(rem_noise)
    thresh = thresholding(gray)
    print(pytesseract.image_to_string(img))


    
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
            
        
    var=text_processing(pytesseract.image_to_string(img))

    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')


    workbook=Workbook()
    sheet= workbook.active
    sheet["A1"]="WORDS"
    sheet["B1"]="HINDI"
    sheet["C1"]="TAMIL"
    sheet["D1"]="TELUGU"
    sheet["E1"]="PUNJABI"

    workbook.save(filename="TransText.xlsx")
    lwords=[]
    j=2
    for i in range(len(var)):
        lwords.append(var[i])
        s="A"+str(j)
        sheet[s]=var[i]
        j=j+1
        workbook.save(filename="TransText.xlsx")
    j=2
    from google_trans_new import google_translator
    ltranswordshindi=[]
    ltranswordstamil=[]
    ltranswordstelugu=[]
    ltranswordspunjabi=[]
    translator=google_translator()
    for i in var:
        translate_text=translator.translate(i,lang_tgt="hi")    
        ltranswordshindi.append(translate_text)
        translate_text=translator.translate(i,lang_tgt="pa")    
        ltranswordspunjabi.append(translate_text)  
        translate_text=translator.translate(i,lang_tgt="ta")    
        ltranswordstamil.append(translate_text)  
        translate_text=translator.translate(i,lang_tgt="te")    
        ltranswordstelugu.append(translate_text)  
            
    dictwords={}
    j=2
    for i in range(len(lwords)):
        shindi="B"+str(j)
        spu="C"+str(j)
        ste="D"+str(j)
        sta="E"+str(j)
        sheet[shindi]=ltranswordshindi[i]
        sheet[spu]=ltranswordspunjabi[i]
        sheet[ste]=ltranswordstamil[i]
        sheet[sta]=ltranswordstelugu[i]
        j=j+1
        workbook.save(filename="TransText.xlsx")
    j=2