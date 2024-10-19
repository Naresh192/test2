# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:52:11 2024

@author: NAlwala
"""
import pickle
import streamlit as st
import spotipy

# Spotify API credentials
SPOTIPY_CLIENT_ID  = '755ba06cada94cd7b6d867fd98e9f20c'
SPOTIPY_CLIENT_SECRET = 'c5089f232b134538833409e397ee7834'
SPOTIPY_REDIRECT_URI = 'https://www.google.com'

# Scope for accessing currently playing track
SCOPE = 'user-read-currently-playing'

try :
    with open('token.pkl', 'rb') as file:
        token_info = pickle.load(file)
except :
    sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri=SPOTIPY_REDIRECT_URI,
                            scope=SCOPE)
    
    token_info = sp_oauth.get_access_token(as_dict=False)
    with open('token.pkl', 'wb') as file:
        pickle.dump(token_info, file)
sp = spotipy.Spotify(auth=token_info)

def get_current_playing_track():
    current_track = sp.current_playback()
    if current_track is not None and current_track['is_playing']:
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        return f"Currently playing: {track_name} by {artist_name}"
    else:
        return "No song is currently playing."

st.title("Spotify Currently Playing")
st.write(get_current_playing_track())
