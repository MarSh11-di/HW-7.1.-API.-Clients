import requests


def get_repository_info (name_repo:str, owner_repo:str):
   curl_req = "https://api.github.com/repos/{owner}/{repo}"
   respons = requests.get(
      curl_req.format(owner=owner_repo, repo=name_repo),
      headers={
         "Accept": "application/vnd.github+json",
         "X-GitHub-Api-Version": "2022-11-28",
         })     
   required_data ={'name':'name',
                  'owner':'owner',
                  'description':'description',
                  'license':'license',
                  'created_at':'created_at'}
   for obj in respons.json():
      if obj in required_data:
         required_data[obj]= respons.json()[obj]
         if obj == 'owner':
            required_data[obj]=respons.json()[obj]['login']       
   for key, value in required_data.items():
      print(f'{key}:{value}')

get_repository_info ("Hello-World","octocat")
