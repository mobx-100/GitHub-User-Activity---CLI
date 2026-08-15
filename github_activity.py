import json #parse the response 
import sys  #CLI command 
import urllib.request  #http request
import urllib.error   #network error handling 

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    req = urllib.request.Request(
        url,
        headers={"User-Agent" : "python-github-activity-cli"}
    )

    try:
        with urllib.request.urlopen(req) as res:
            if res.status == 200:
                data = res.read().decode('utf-8')
                return json.loads(data)
    except urllib.error.HTTPError as e_http:
        if e_http == 404:
            print(f"Error: User '{username}' not found. ")
        elif e_http.code == 403:
            print("Error: API rate limit exceeded or access forbidden.")
        else:
            print(f"Error: HTTP error occurred (Status code: {e_http.code})")
    except urllib.error.URLError as e:
        print(f"Error: Failed to reach the server. Check your network connection. ({e.reason})")
    
    sys.exit(1) 

def display_activity(events):
    if not events:
        print("No recent activity found for this user.")
        return

    for event in events:
        event_type = event.get("type")
        repo_name = event.get("repo", {}).get("name", "unknown/repository")
        payload = event.get("payload", {})

        if event_type == "PushEvent":
            commit_count = len(payload.get("commits", []))
            print(f"- Pushed {commit_count} commit(s) to {repo_name}")
        elif event_type == "IssuesEvent":
            action = payload.get("action")
            if action == "opened":
                print(f"- Opened a new issue in {repo_name}")
            elif action == "closed":
                print(f"- Closed an issue in {repo_name}")
            else:
                print(f"- {action.capitalize()} an issue in {repo_name}")
        elif event_type == "WatchEvent":
            print(f"- Starred {repo_name}")
        elif event_type == "CreateEvent":
            ref_type = payload.get("ref_type")
            print(f"- Created a new {ref_type} in {repo_name}")
        elif event_type == "PullRequestEvent":
            action = payload.get("action")
            print(f"- {action.capitalize()} a pull request in {repo_name}")
        else:
            # Fallback for other event types
            clean_type = event_type.replace("Event", "")
            print(f"- Performed {clean_type} on {repo_name}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py ")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Fetching recent activity for {username}...\n")
    
    events = fetch_github_activity(username)
    display_activity(events)

if __name__ == "__main__":
    main()  