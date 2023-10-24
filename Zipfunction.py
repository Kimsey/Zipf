# Loading packages
import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Function
# Webscrapping the information from wikipedia using beautifulSoup
def load_data(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    return soup

# Making a list from words
def var_maker(soup):
    count = 0
    wiki = " "
    while count < len(soup.select('p')):
        wiki += soup.select('p')[count].text
        count += 1
    word_lists = wiki.split(" ")
    return word_lists

# Joining dataframes
def jon(*args):
    jon_df = pd.DataFrame()
    for ind in range(int(len(args) / 2)):
        temp = pd.DataFrame({args[ind * 2]: args[ind * 2 + 1]})
        jon_df = jon_df.join(temp, how='outer')
    return jon_df

# Get the rank and count of the words
def num_marker(wrd_lts):
    index = 0
    zipf = list()
    dict_of_words = dict()
    while index < len(wrd_lts):
        word = wrd_lts[index]
        dict_of_words[word] = wrd_lts.count(word)
        index += 1
    sorted_dict = dict(sorted(dict_of_words.items(), reverse=True, key=lambda x: x[1]))
    
    zipf = list()
    for wrd in range(1, len(sorted_dict) + 1):
        math = next(iter(sorted_dict.values())) * (1 / wrd)
        zipf.append(math)
    return sorted_dict, zipf

# Get the corr score
def scorr(df, *args):
    temp = list()
    for ind in range(int(len(args) / 2)): 
        temp.append(df[[args[ind * 2], args[ind * 2 + 1]]].corr('spearman'))
    return temp

# Plot the data
def real_plot(df, *args):
    for ind in range(int(len(args) / 2)):
        plt.plot(range(1, 31), df[args[ind * 2]], '-*', color='black', label= "Top 30 words")
        plt.plot(range(1, 31), df[args[ind * 2 + 1]],  '-*', color='red', label='Zipf Line')
        plt.xlabel("Rank")
        plt.ylabel("Frequency")
        plt.title(args[ind*2].split(' ')[0])
        plt.xticks(rotation = 45)
        plt.legend()
        plt.show()