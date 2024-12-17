# import pandas
import pandas as pd

# load movies metadata
metadata = pd.read_csv('movies_metadata.csv', low_memnory=False)
# need a list of movies in the project with metadata ( vote_average, vote_count)
# print hte first three rows 
metadata.head(3)

# use an algo to compare movies scores
# there must be a review score, and a number of voters / watchers
# a 9.5 with 1 viewer should weigh less than a 8.9 with 10,000 viewers

# calculate the mean of vote average column
movie_mean = metadata['vote_average'].mean()
print(movie_mean)

# calculate the number of votes received by a movie based on it's percentile
# pandas library makes this easier using .quantile()

# calculate the number of votes required to be in the top 250 chart
movie_min_votes = metadata['vote_count'].quantile(0.90)
print(movie_min_votes)

# if a movie has votes greater than or equal to 'movie_min_votes' you can compare / add

# use the .copy() method to make changes to a new dataframe
# this ensures the original metadata dataframe is not changed

# filter out the top 90th percentile into a new dataframe
top_movies_based_on_vote = metadata.copy().loc[metadata['vote_count'] >= movie_min_votes]

top_movies_based_on_vote.shape 
# this returns a tuple representing the dimensions of object


# now we need to build a method to calculate the weighted ranking
# we have movie_min_votes(m) & movie_mean (C)
# select the 'vote_count'(v) & 'vote_average'(R) column from top_movies dataframe

def weighted_ranking(x, m=movie_min_votes, c=movie_mean):
    v = x['vote_count']
    r = x['vote_average']
    # calculation based on the "IMDB" formula
    return (v/(v+m) * r) + (m/(m+v) * c)
# (v / (v + movie_min_votes) * r) + (movie_min_votes / (movie_min_votes+v) * movie_mean)

#give up because what the fuck is this 
# use aigoogle to start prompting ai data models to generate tiktok content and make
# monies wtf