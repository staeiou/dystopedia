# dystopedia
A Markov chain Twitter bot based on the titles of deleted Wikipedia articles.

## The data
The data in titles.txt is drawn from the first version of [deletionpedia](http://deletionpedia.dbatley.com/w/index.php), which was a project to archive articles that had been deleted from Wikipedia or might be deleted soon. It closed in 2011, but the database archive of deletionpedia v1 is accessible at the Internet Archive [here](https://archive.org/details/wiki-deletionpedia.dbatley.com). In the compressed archive deletionpediadbatleycom_w-20110712-wikidump.7z, there is a file with the titles of all articles archived on deletionpedia called deletionpediadbatleycom_w-20110712-titles.txt. Every article title is listed twice, once with just the title, then another time with the title and date of deletion. I cleaned this up by sorting it for unique items, then took every other line from this file:

    sort -u titles.txt
    awk 'NR%2==0' titles.txt

