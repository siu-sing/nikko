# Nikko


```python
pipenv install
pipenv shell
```

Get `api_id` and `api_hash` from https://my.telegram.org/auth?to=apps

App title and shortname can be random.

To start creating a job, create a new file in the project folder called `config.py`. Enter the job details in the followint format in the file.

```python
jobs = [
    {
        "job_name": "<name of job>",
        "api_id": "<api_id>",
        "api_hash": "<api_hash>",
        "msg_file": "<name of template file>",
        "recipients": ["list","of","chat_id","like",-345234213,"or","@channel_name"],
    }
]
```