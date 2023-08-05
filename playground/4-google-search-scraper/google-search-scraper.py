import yagooglesearch

query = "site:linkedin.com/in \"manager\" \"asset management\" \"ibm maximo\""

client = yagooglesearch.SearchClient(
    query,
    # tbs="li:1", # verbatim search
    max_search_result_urls_to_return=2,
    http_429_cool_off_time_in_minutes=5,
    http_429_cool_off_factor=1.5,
    # proxy="socks5h://127.0.0.1:9050",
    verbosity=5, # 6 turns off all terminal output
    verbose_output=False,  # False (only URLs) or True (rank, title, description, and URL)
)
client.assign_random_user_agent()

urls = client.search()

len(urls)

print("---------------------------------")
print("URLS")
for url in urls:
    print(url)