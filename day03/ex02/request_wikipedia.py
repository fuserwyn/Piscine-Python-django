import requests
import json
import dewiki
import sys

def requset_wiki(page:str):
	try:
		res = requests.get(f"https://en.wikipedia.org/w/api.php?action=parse&page={page}&prop=wikitext&format=json&redirects=true")
		res.raise_for_status()
	except requests.HTTPError as e:
		raise e
	try:
		data = json.loads(res.text)
	except json.decoder.JSONDecodeError as e:
		raise e
	if data.get("error") != None:
		raise Exception(data["error"]["info"])
	return (dewiki.from_string(data["parse"]["wikitext"]["*"]))

def main():
	if (len(sys.argv) == 2):
		try:
			wiki_data = requset_wiki(sys.argv[1])
		except Exception as e:
			return print(e)
		try:
			f = open("{}.wiki".format(sys.argv[1]), "w")
			f.write(wiki_data)
			f.close()
		except Exception as e:
			return print(e)
	elif len(sys.argv) == 2:
		print("one argument required! : title")
	else:
		print("wrong argument count!")

if __name__ == '__main__':
		main()