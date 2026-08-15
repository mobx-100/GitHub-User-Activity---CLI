
# GitHub User Activity CLI

A simple command-line interface (CLI) tool built in Python to fetch and display recent activity for any public GitHub user directly in your terminal. This project uses only Python's standard library with **no external dependencies or frameworks**.

---

## Project URL

* **Roadmap.Sh:** [https://roadmap.sh/projects/github-user-activity](https://roadmap.sh/projects/github-user-activity) 

---

## Features

* **Zero Dependencies:** Built entirely using Python's built-in modules (`urllib`, `json`, and `sys`).
* **Clean Terminal Output:** Parses raw GitHub event data into human-readable summaries (e.g., pushes, issues opened, starred repositories).
* **Robust Error Handling:** Gracefully handles invalid usernames, API rate limits, and network connection issues.

---

## Requirements

* Python 3.6 or higher installed on your system.

---

## Installation & Setup

1. Create a directory for the project and navigate into it:
   ```bash
   mkdir github-activity
   cd github-activity

```

2. Save the script code into a file named `github_activity.py`.

---

## Usage

Run the script from your terminal by passing a public GitHub username as an argument:

```bash
python github_activity.py <username>

```

### Example

```bash
python github_activity.py kamranahmedse

```

**Output:**

```text
Fetching recent activity for kamranahmedse...

- Pushed 3 commit(s) to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap

```

---

## How It Works

* **API Endpoint:** Uses the public GitHub Events API endpoint: `https://api.github.com/users/<username>/events`
* **Limitations:** Note that the GitHub Events API has a hard retention limit of **30 days** (and a maximum cap of 300 recent events).

```

```
