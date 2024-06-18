def is_viewed(episode: dict):
    status = False
    if "viewed" in episode:
        status = bool(episode['viewed'])

    return status
