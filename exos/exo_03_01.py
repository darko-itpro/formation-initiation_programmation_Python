
episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]

episode = episode_viewed
# episode = episode_not_viewed
print("Episode Vu")
viewed = episode[3]

if viewed:
    print("Episode Vu")
else:
    print("Episode NON Vu")
