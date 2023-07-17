import numpy as np
import pandas as pd

dataset = pd.read_csv("USvideos.csv")

# İlk 5 veriyi gösterme
# Reading the first 5 data
"""
print(dataset.head(n = 5))
"""
# Silme thumbnail_link,video_id,trending_date,publish_time,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed
# Delete thumbnail_link,video_id,trending_date,publish_time,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed
"""
dataset.drop(["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis = 1,inplace = True)
"""
# Like ve Dislike sayılarının ortalamaları
# Calculate the averages of the number of likes and dislikes
"""
print(dataset["likes"].mean())
print(dataset["dislikes"].mean())
"""
# En yüksek views olan video
# Most views videos
"""
print(dataset[dataset["views"] == dataset["views"].max()]["title"].iloc[0])
"""
# En düşük views olan video
# The video with the lowest number of views
"""
print(dataset[dataset["views"] == dataset["views"].min()]["title"].iloc[0])
"""
# Kategorilere Göre (category_id) Yorum Sayılarının Ortalamasını Bulun
# Find the average number of comments per category_id
"""
print(dataset.groupby("category_id").mean()[["comment_count"]])
"""
# Her kategoride kaç adet videonun olduğunu bulma
# Find the number of videos in each category
"""
print(dataset["category_id"].value_counts())
"""
# Başlıkların uzunluğunu column olarak ekleme
# Add the length of the titles as a new column
"""
def FindLen(title):
    return len(title)
dataset["title_length"] = dataset["title"].apply(FindLen)
print(dataset)
"""
# Tag sayısını column olarak ekleme
# Add the number of tags as a new column
"""
def countTag(tags):
    tagList = tags.split("|")
    return len(tagList)

dataset["tag_count"] = dataset["tags"].apply(countTag)
print(dataset)
"""
