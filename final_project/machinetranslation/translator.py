'''
Created By Bahij Sayegh
    # source language code
    # target language code
    # English --> en
    # french --> fr

'''

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''
    This function return english to french translation
    '''
    translated_french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    return translated_french_text

def french_to_english(french_text):
    '''
    This function return french to english translation
    '''
    translated_english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return translated_english_text
