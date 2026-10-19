import pandas as pd

songs = pd.read_csv("songs.csv")

print("Our music dataset:")
print(songs)

most_streamed = songs.loc[songs["streams_millions"].idxmax()]


print("\nMost-streamed song:")
print(most_streamed["song"])
print("Artist:", most_streamed["artist"])
print("Streams (millions):", most_streamed["streams_millions"])
average_streams = songs["streams_millions"].mean()

print("\nAverage streams (millions):", average_streams)
