# natalieweger-bot
ideas for a federal website bot 

My idea for a bot would notify users whenever a federal website gets taken down, by tracking if the website has a 404 or some other related error. This bot would help reporters track down which federal departments and websites might be impacted by the Trump Administration. 

The New York Times has already written an article (https://www.nytimes.com/2025/02/02/upshot/trump-government-websites-missing-pages.html) about how thousands of U.S. Government Web Pages were taken down in February. The Times downloaded a list of the most visited government domains in the U.S. (https://analytics.usa.gov/data/live/top-100000-domains-30-days.csv) and then compiled a complete list of pages using the site maps. The Times analysis found more than seven million pages to start with across 150 different sites. 

However, even The Times had trouble capturing every single changes on the millions of website pages that the goverment hosts. Especially since The Times navigated this through site maps, rather than downloading actual copies of websites, its approach has some trade-offs. 

For my bot, I'm thinking I could just work with the original downloaded list of the most visited government domains in the U.S. Though I'm not sure how I would be able to find errors within each website, or if this scope of a project is way too big for the first ever bot that I'm attempting to do. 

As a first step though, I uploaded the same CSV from The Times onto this repository. I also started up my code and downloaded a few Python libraries that I might need. 

I'm assuming that I would use requests in Python to each domain, and see if I get any errors in return. This can then be logged into another CSV that will trigger an alert the page is no longer running. Something I'm still wondering, though, is that the original NYT csv is multiple main website pages, and I'm not sure how to find website subpages of the main pages and then compile it into a CSV.  