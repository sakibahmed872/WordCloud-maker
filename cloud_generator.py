from wordcloud import WordCloud, STOPWORDS

comment_word=""

stopword=set(STOPWORDS)

file=open("word.txt","r+")

text=file.read().replace("\n"," ")

wc=WordCloud(stopwords=stopword, width=792, height=507, min_font_size=10, background_color="Black")


# generate word cloud
wc.generate(text)

# store to file
wc.to_file("wordcloud.png")
print("Successfull")
