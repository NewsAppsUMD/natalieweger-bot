from htmldate import find_date

# List of URLs to process
urls = [
    "https://today.umd.edu/umd-launches-institute-focused-on-ethical-ai-development",
    "https://www.trails.umd.edu/",
    "https://artiamas.umd.edu/",
    "https://ml.umd.edu/",
]

# Loop through each URL and find the publication date
for url in urls:
    date = find_date(url)  # Extract publication date from the webpage
    print(f"{url}: {date}")  # Print the URL and its publication date
