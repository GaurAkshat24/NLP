#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install beautifulsoup4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests

def scrape_single_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('h1').text
        article_text = soup.find('article').text

        return title, article_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


# In[3]:


# Test URL
test_url = 'https://insights.blackcoffer.com/rising-it-cities-and-its-impact-on-the-economy-environment-infrastructure-and-city-life-by-the-year-2040-2/'
title, text = scrape_single_url(test_url)
print(title)
print(text[:500])  # Print first 500 characters of the article for brevity


# In[4]:


urls = [
    "https://insights.blackcoffer.com/rising-it-cities-and-its-impact-on-the-economy-environment-infrastructure-and-city-life-by-the-year-2040-2/",
    "https://insights.blackcoffer.com/rising-it-cities-and-their-impact-on-the-economy-environment-infrastructure-and-city-life-in-future/",
    "https://insights.blackcoffer.com/internet-demands-evolution-communication-impact-and-2035s-alternative-pathways/",
    "https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-in-upcoming-future/",
    "https://insights.blackcoffer.com/ott-platform-and-its-impact-on-the-entertainment-industry-in-future/",
    "https://insights.blackcoffer.com/the-rise-of-the-ott-platform-and-its-impact-on-the-entertainment-industry-by-2040/",
    "https://insights.blackcoffer.com/rise-of-cyber-crime-and-its-effects/",
    "https://insights.blackcoffer.com/rise-of-internet-demand-and-its-impact-on-communications-and-alternatives-by-the-year-2035-2/",
    "https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-by-the-year-2040-2/",
    "https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-by-the-year-2040/",
    "https://insights.blackcoffer.com/rise-of-internet-demand-and-its-impact-on-communications-and-alternatives-by-the-year-2035/",
    "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/",
    "https://insights.blackcoffer.com/rise-of-e-health-and-its-impact-on-humans-by-the-year-2030/",
    "https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030-2/",
    "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-2/",
    "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-2-2/",
    "https://insights.blackcoffer.com/rise-of-chatbots-and-its-impact-on-customer-support-by-the-year-2040/",
    "https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030/",
    "https://insights.blackcoffer.com/how-does-marketing-influence-businesses-and-consumers/",
    "https://insights.blackcoffer.com/how-advertisement-increase-your-market-value/",
    "https://insights.blackcoffer.com/negative-effects-of-marketing-on-society/",
    "https://insights.blackcoffer.com/how-advertisement-marketing-affects-business/",
    "https://insights.blackcoffer.com/rising-it-cities-will-impact-the-economy-environment-infrastructure-and-city-life-by-the-year-2035/",
    "https://insights.blackcoffer.com/rise-of-ott-platform-and-its-impact-on-entertainment-industry-by-the-year-2030/",
    "https://insights.blackcoffer.com/rise-of-electric-vehicles-and-its-impact-on-livelihood-by-2040/",
    "https://insights.blackcoffer.com/rise-of-electric-vehicle-and-its-impact-on-livelihood-by-the-year-2040/",
    "https://insights.blackcoffer.com/oil-prices-by-the-year-2040-and-how-it-will-impact-the-world-economy/",
    "https://insights.blackcoffer.com/an-outlook-of-healthcare-by-the-year-2040-and-how-it-will-impact-human-lives/",
    "https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/",
    "https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/",
    "https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/",
    "https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/",
    "https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/",
    "https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/",
    "https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/",
    "https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/",
    "https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/",
    "https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/",
    "https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/",
    "https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/",
    "https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/",
    "https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/",
    "https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/",
    "https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/",
    "https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/",
    "https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/",
    "https://insights.blackcoffer.com/evolution-of-advertising-industry/",
    "https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/",
    "https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/",
    "https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/",
    "https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/",
    "https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/",
    "https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/",
    "https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/",
    "https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/",
    "https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/",
    "https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/",
    "https://insights.blackcoffer.com/how-we-forecast-future-technologies/",
    "https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/",
    "https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/",
    "https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/",
    "https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/",
    "https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/",
    "https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/",
    "https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/",
    "https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/",
    "https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/",
    "https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/",
    "https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/",
    "https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/",
    "https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/",
    "https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/",
    "https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/",
    "https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/",
    "https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/",
    "https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/",
    "https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/",
    "https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors/",
    "https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-tourism-aviation-industries/",
    "https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-sports-events-around-the-world/",
    "https://insights.blackcoffer.com/changing-landscape-and-emerging-trends-in-the-indian-it-ites-industry/",
    "https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/",
    "https://insights.blackcoffer.com/human-rights-outlook/",
    "https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/",
    "https://insights.blackcoffer.com/how-the-covid-19-crisis-is-redefining-jobs-and-services/",
    "https://insights.blackcoffer.com/how-to-increase-social-media-engagement-for-marketers/",
    "https://insights.blackcoffer.com/impacts-of-covid-19-on-streets-sides-food-stalls/",
    "https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets-2/",
    "https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-5/",
    "https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-4/",
    "https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-2/",
    "https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/",
    "https://insights.blackcoffer.com/travel-and-tourism-outlook/",
    "https://insights.blackcoffer.com/gaming-disorder-and-effects-of-gaming-on-health/",
    "https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation/",
    "https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation-2/",
    "https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-office-space-and-co-working-industries/",
    "https://insights.blackcoffer.com/contribution-of-handicrafts-visual-arts-literature-in-the-indian-economy/",
    "https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/",
    "https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/"
    
    ]


# In[5]:


import os

save_path = '/Users/akshatgaur/Desktop/saved' 

for url in urls:
    url_id = url.split('/')[-2]  
    title, text = scrape_single_url(url)

    if title and text:
        filename = os.path.join(save_path, f"{url_id}.txt")  
        with open(filename, "w") as file:
            file.write(title + "\n\n" + text)
        print(f"Saved: {filename}")
    else:
        print(f"Failed to scrape: {url}")


# In[6]:


def scrape_single_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title_tag = soup.find('h1')
        article_tag = soup.find('article')

        title = title_tag.text if title_tag else "No Title Found"
        article_text = article_tag.text if article_tag else "No Article Text Found"

        return title, article_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


# In[7]:


failed_urls = [
    "https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/",
    "https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/",
]


# In[8]:


for url in failed_urls:
    url_id = url.split('/')[-2]
    title, text = scrape_single_url(url)

    if title and text:
        filename = f"{url_id}.txt"
        with open(filename, "w") as file:
            file.write(title + "\n\n" + text)
        print(f"Saved: {filename}")
    else:
        print(f"Failed to scrape: {url}")


# In[9]:


custom_stop_words = ["ERNST", "YOUNG", "DELOITTE", "TOUCHE", "KPMG", 
                     "PRICEWATERHOUSECOOPERS", "PRICEWATERHOUSE", "COOPERS"]


# In[10]:


def load_words_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(file.read().splitlines())
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as file:
            return set(file.read().splitlines())

path_to_positive_words = '/Users/akshatgaur/Downloads/positive-words.txt'
positive_words = load_words_from_file(path_to_positive_words)
len(positive_words)  # Output the count of positive words loaded


# In[11]:


path_to_negative_words = '/Users/akshatgaur/Downloads/negative-words.txt'
negative_words = load_words_from_file(path_to_negative_words)
print("Number of negative words loaded:", len(negative_words))


# In[12]:


paths_to_stop_words = [
    '/Users/akshatgaur/Downloads/StopWords_Auditor.txt',
    '/Users/akshatgaur/Downloads/StopWords_DatesandNumbers.txt',
    '/Users/akshatgaur/Downloads/StopWords_Generic.txt',
    '/Users/akshatgaur/Downloads/StopWords_GenericLong.txt',
    '/Users/akshatgaur/Downloads/StopWords_Geographic.txt',
    '/Users/akshatgaur/Downloads/StopWords_Names.txt'
]

all_stop_words = set()
for path in paths_to_stop_words:
    all_stop_words.update(load_words_from_file(path))

print("Number of stop words loaded:", len(all_stop_words))


# In[13]:


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# In[14]:


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text, stop_words):
    words = word_tokenize(text)
    return [word for word in words if word.lower() not in stop_words]


# In[15]:


def calculate_sentiment_scores(cleaned_text, positive_words, negative_words):
    positive_score = sum(1 for word in cleaned_text if word.lower() in positive_words)
    negative_score = sum(1 for word in cleaned_text if word.lower() in negative_words)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(cleaned_text) + 0.000001)
    return positive_score, negative_score, polarity_score, subjectivity_score


# In[16]:


def syllable_count(word):
    return sum(1 for char in word if char.lower() in 'aeiou')

def gunning_fog_index(text):
    sentences = nltk.sent_tokenize(text)
    words = word_tokenize(text)
    complex_words_count = sum(1 for word in words if syllable_count(word) > 2)
    avg_sentence_length = len(words) / len(sentences)
    percent_complex_words = complex_words_count / len(words)
    fog_index = 0.4 * (avg_sentence_length + percent_complex_words)
    return fog_index


# In[17]:


import os

directory = '/Users/akshatgaur/Desktop/saved'

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            text_data = file.read()
        cleaned_text = clean_text(text_data, all_stop_words)
        positive_score, negative_score, polarity_score, subjectivity_score = calculate_sentiment_scores(cleaned_text, positive_words, negative_words)
        fog_index = gunning_fog_index(text_data)

        print(f"Analysis for {filename}:")
        print("Positive Score:", positive_score)
        print("Negative Score:", negative_score)
        print("Polarity Score:", polarity_score)
        print("Subjectivity Score:", subjectivity_score)
        print("Gunning Fog Index:", fog_index)
        print("\n")


# In[ ]:




