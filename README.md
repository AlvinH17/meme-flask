# Meme Flask

A small Flask app that pulls a random meme from a given subreddit (via the [meme-api](https://meme-api.com)) and displays it, auto-refreshing every 30 seconds.

## Features

- Shows a random meme from any subreddit (defaults to `wholesomememes`)
- Enter a different subreddit name to switch feeds
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

## Usage

- Visit the site to see a meme from the default subreddit.
- Type a subreddit name into the input field and press Enter to load a meme from it.
- You can also pass a subreddit directly via query string, e.g. `http://localhost:5001/?sr=aww`.
- If the subreddit is invalid or has no meme available, the app falls back to the default subreddit.

## Project Structure

```
meme_flask.py            # Flask app and meme-fetching logic
templates/meme_index.html  # Main page template
static/styles.css        # Page styling
```

## Notes

- `flasktest.py` is a minimal, unrelated Flask scratch file and isn't used by the meme app.
