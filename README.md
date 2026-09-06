# Meme Flask

A small Flask app that pulls a random meme from a subreddit (via the [meme-api](https://meme-api.com)) and displays it, auto-refreshing every 30 seconds.

## Features

- Shows a random meme from the `wholesomememes` subreddit
- Auto-refreshes every 30 seconds to fetch a new meme

## Requirements

- Python 3.8+
- Flask
- requests

## Setup

```bash
pip install -r requirements.txt
```

## Running

```bash
python meme_flask.py
```

The app binds to `0.0.0.0:5001`, so it's reachable at `http://localhost:5001`.

## Project Structure

```
meme_flask.py            # Flask app and meme-fetching logic
templates/meme_index.html  # Main page template
static/styles.css        # Page styling
```

## Notes

- `flasktest.py` is a minimal, unrelated Flask scratch file and isn't used by the meme app.
