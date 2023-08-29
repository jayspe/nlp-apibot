from googlesearch import search

# query string to search on Google
query = "framework laptop"

# number of top search results to fetch
numResults = 10

google_search_results = list(search(query, stop=numResults, pause=1))

print("Here's a list of the top {} search results on Google:\n".format(numResults))
print(google_search_results)