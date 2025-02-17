# Task To Text

Small Script for turning todoist tasks into text. Currently the script only outputs a file with the intended string.

## Build Guide

You need to have any python3 interpretor installed. You can either use a virtual environment or locally install the following package(s):

```shell
todoist_api_python
```

In order for this code to work, you need to import your own Todoist API token, you can find your API token on your settings in page in Todoist. Dig inside there and you shall find it.

Create a `.env` file inside the root directory. The env.py reads that file to get its API token. Make sure your file has this line:

```sh
API_TOKEN=your_api_token
```
