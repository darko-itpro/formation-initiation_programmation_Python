
episode_viewed = {"title":"The new Project",
                  "duration":98,
                  "viewed":True}
episode_not_viewed = {"title":"Installing the softwares",
                      "duration":42,
                      "viewed":False}
episode_no_key = {'title': 'It works !', 'number': 2, 'duration': 51}

def is_viewed(episode: dict):
    status = False
    if "viewed" in episode:
        status = bool(episode['viewed'])

    return status


def is_viewed(episode: dict):
    return "viewed" in episode and bool(episode['viewed'])


print(is_viewed(episode_not_viewed))
print(is_viewed(episode_no_key))  # Doit retourner False
print(is_viewed(episode_viewed))

