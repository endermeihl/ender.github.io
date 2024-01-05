import requests

# Replace YOUR_API_KEY with your actual API key
headers = {
    'Authorization': 'Bearer secret_Hyo4zOXHHozqg9kjNfAi9hDHakcGZBwWn3mAyOIkx3T',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

# Replace DATABASE_ID with the ID of the database you want to add the page to
page_id = '924e4308b2294189a2cf33a222ba11e6'

# Replace PAGE_TITLE with the title of the new page
new_page = {
    "parent": { "page_id": "924e4308b2294189a2cf33a222ba11e6" },
    "properties": {
        "title": {
      "title": [{ "type": "text", "text": { "content": "A note from your pals at Notion" } }]
        }
    },
    "children": [
    {
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{ "type": "text", "text": { "content": "You made this page using the Notion API. Pretty cool, huh? We hope you enjoy building with us." } }]
      }
    }
  ]
}

url = 'https://api.notion.com/v1/pages'
response = requests.post(url, headers=headers, json=new_page)

# The response will contain the ID of the new page
new_page_id = response.json()['id']
print(f'The ID of the new page is {new_page_id}')