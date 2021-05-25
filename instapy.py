from instapy import InstaPy

session = InstaPy(username = 'rianying', password = 'rianyingg69')
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage = 100)
session.like_by_tags(["rider","bmw","yamaha","ducati","kawasaki"], amount = 3)
session.set_dont_like(["boobs","thigh","bums","child","kids","kid","sexy"])

session.end()