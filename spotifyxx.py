import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username = sys.argv[1]


#   ID: younesegh?si=de0hYoPKR8iR5Zt1zDYESA

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token= util.prompt_for_user_token(username)

#Create spotify spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

user= spotifyObject.current_user()


displayName = user['display_name']
followers = user['followers']['total']

while True:
    print()
    print(">>>> Welcome to Spotipy")
    print(">>>> You have "+ str(followers) +"follower")
    print()
    print("0 - search for artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    #search for artist
    if choice == "0":
        print("0")
        searchQuery = input("OK, what is their name?: ")
        print()

        #get Search results
        searchResults = spotifyObject.search(searchQuery,1,0,"artist")
        

        #artist details
        artist= searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + "followers")
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        #album and track details
        trackURIs= []
        trackArt = []
        z= 0

        #track album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print("ALBUM" + item['name'])
            albumID = item['id']
            albumArt= item['images'][0]['url']

            trackResults= spotifyObject.album_tracks(albumID)
            trackResults= trackResults['items']

            for item in trackResults:
                print(str(z) + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print()


        while True:
            songSelection =  input("Enter the song number to see which album art associated with it (x to exit) : ")
            if songSelection == "x":
                break
            webbrowser.open(trackArt[int(songSelection)])



    if choice == "1":
        break

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
