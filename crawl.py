import urllib.parse;
import urllib.request;
from bs4 import BeautifulSoup;


def searchLink(search):

	BASE_URL = "http://www.990.ro/"
	key = urllib.parse.urlencode({'kw': search}).encode('ascii');

	re = urllib.request.Request(BASE_URL + 'functions/search3/live_search_using_jquery_ajax/search.php', key);
	re_link = urllib.request.urlopen(re);
	soup = BeautifulSoup(re_link.read(), "lxml");

	ref = soup.find_all('a');
	names = soup.find_all('div', id="rest");

	if(ref != []):
		print("Search returned:")
		i = 1;

		for name in names:
			print(str(i) + ". " + name.get_text());
			i+=1;

		select = int(input("\nPlease select the corresponding number: "));

		return BASE_URL + ref[select - 1].get('href');

	else:
		print("Nothing found!");
		return '';

movie = input("search: ");
print(searchLink(movie));
