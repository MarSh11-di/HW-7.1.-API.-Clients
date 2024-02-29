import requests
from pprint import pprint
def get_recent_commits(name_repo:str):

   curl_req = "https://api.github.com/repos/{owner_repo}/commits"
   respond = requests.get(
      curl_req.format(owner_repo=name_repo),
      headers={
         "Accept": "application/vnd.github+json",
         "X-GitHub-Api-Version": "2022-11-28",
         })
   json_result =respond.json()
   list_of_keys = ["Author","Date","Commit Message","Link to the commit on GitHub"]
   last_commits =[]
   dict_data =[]
   for ind, data in enumerate(json_result):
      data_commit = data["commit"]
      last_commits.append(data_commit["author"]["name"])
      last_commits.append(data_commit["author"]["date"])
      last_commits.append(data_commit["message"])
      last_commits.append( data_commit["url"])
      dict_data.append(dict(zip(list_of_keys,last_commits)))

   pprint(dict_data)

get_recent_commits("octocat/Hello-World")    
