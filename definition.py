import requests

def get_definition(word):
    try:
        response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)
        data = response.json()
        meaning = data[0]['meanings'][0]['definitions'][0]['definition']
        return f'MEANING: {meaning}'
    except:
        return "(couldn't load the meaning of the word)"
