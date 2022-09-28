import instaloader
L = instaloader.Instaloader()

# Login or load session
username = ''
password = r''
L.login(username, password)  # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, '')

# Print list of followees
follow_list = []
count = 0
for follower in profile.get_followers():
    print('{} has {} followers'.format(follower.username, follower.followers))
    file = open("followers.txt", "a+")
    file.write(follower.username + ";" + str(follower.followers))
    file.write("\n")
    file.close()
    count = count + 1
    print("reading:" + count + " of " + profile.followers)
