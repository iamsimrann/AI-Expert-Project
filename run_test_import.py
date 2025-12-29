import L1A6AImovie as m
print(m.movies_df[['Series_Title','Genre','IMDB_Rating']].to_string(index=False))
