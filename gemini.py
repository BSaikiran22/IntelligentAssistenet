# -*- coding: utf-8 -*-



import google.generativeai as genai




# Configure the API with your API key
genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel('gemini-pro')
# model = genai.GenerativeModel('gemini-pro-vision')
def gemin (vari): 
    response = model.generate_content(vari)
    # print(response)
    re=response.text
    l2=re.replace("*","")
    # print(l2)
    return l2
# -*- coding: utf-8 -*-
# print(gemin("Tell me about virat kohli in hindi"))
