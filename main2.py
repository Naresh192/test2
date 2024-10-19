# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:52:11 2024

@author: NAlwala
"""
import pickle
import streamlit as st
from spotipy.oauth2 import SpotifyOAuth
import spotipy

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id='755ba06cada94cd7b6d867fd98e9f20c',client_secret='c5089f232b134538833409e397ee7834',redirect_uri='http://localhost:8000/'))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    st.write(track)
