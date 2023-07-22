import instaloader
ig= instaloader.Instaloader()
profile = input("enter user name:," )
ig.download_profile(profile,profile_pic_only=False)
print("Download completed")

