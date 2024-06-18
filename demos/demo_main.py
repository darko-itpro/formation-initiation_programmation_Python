episode_viewed = {"title":"The new Project",
                  "duration":98,
                  "viewed":True}
episode_not_viewed = {"title":"Installing the softwares",
                      "duration":42,
                      "viewed":False}
episode_no_key = {'title': 'It works !', 'number': 2, 'duration': 51}

import demos.episode_utils
print( demos.episode_utils.is_viewed(episode_viewed) )

from demos import episode_utils
print( episode_utils.is_viewed(episode_not_viewed) )

import demos.episode_utils as eu
print( eu.is_viewed(episode_not_viewed) )


# network = get_network()
#
# if network:
#     import ws_utils as datasource
# else:
#     import local_cache as datasource
#
# datasource.save(data)
#
