import os

import github

# Read token
TOKEN = os.getenv('GH_TOKEN')
auth = github.Auth.Token(TOKEN)
gh = github.Github(auth=auth)

# Get input
ISSUE = int(os.getenv('ISSUE'))
REPO = os.getenv('GH_REPO')
print(REPO)

repo = gh.get_repo(REPO)
issue = repo.get_issue(ISSUE)

issue.create_comment("IntegrationTester presents: Test")
