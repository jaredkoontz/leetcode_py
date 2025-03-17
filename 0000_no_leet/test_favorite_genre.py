"""
question url:

https://leetcode.com/discuss/interview-question/373006
https://leetcode.com/playground/bzSMcEUD
https://leetcode.com/playground/XKfo6DLV

Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

Example 1:

Input:
userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
Example 2:

Input:
userSongs = {
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4"]
},
songGenres = {}

Output: {
   "David": [],
   "Emma":  []
}


"""


def figure_out_genre(song, song_genres):
    for genre in song_genres:
        if song in song_genres[genre]:
            return genre


def filter_favorites(favorites):
    curr_max = -9999
    pretty_favs = []
    for genre in favorites:
        if favorites[genre] > curr_max:
            curr_max = favorites[genre]
            pretty_favs.clear()
            pretty_favs.append(genre)
        elif favorites[genre] == curr_max:
            pretty_favs.append(genre)
    return pretty_favs


def naive_favorite(user_songs, song_genres):
    user_favorites = {}
    for user in user_songs:
        favorites = {}

        for song in user_songs[user]:
            genre = figure_out_genre(song, song_genres)
            if genre in favorites:
                favorites[genre] += 1
            else:
                favorites[genre] = 1

        user_favorites[user] = filter_favorites(favorites)
    return user_favorites


def smarter_favorite(user_songs, song_genres):
    new_map = {}
    ret_val = {}
    for genre in song_genres:
        for song in song_genres[genre]:
            new_map[song] = genre

    for user in user_songs:
        ret_val[user] = []
        for song in user_songs[user]:
            genre = new_map.get(song)


def favorite_genre(user_songs: dict, song_genres: dict) -> dict:
    if not user_songs or not song_genres:
        return {}

    # return smarter_favorite(user_songs,song_genres)

    return naive_favorite(user_songs, song_genres)


def test_one():
    user_songs = {
        "David": ["song1", "song2", "song3", "song4", "song8"],
        "Emma": ["song5", "song6", "song7"],
    }

    song_genres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"],
    }

    assert favorite_genre(user_songs, song_genres) == {
        "David": ["Rock", "Techno"],
        "Emma": ["Pop"],
    }


def test_two():
    user_songs = {
        "David": ["song2", "song3", "song4", "song8"],
        "Emma": ["song5", "song6", "song7"],
    }

    song_genres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"],
    }

    assert favorite_genre(user_songs, song_genres) == {
        "David": ["Techno"],
        "Emma": ["Pop"],
    }


def test_three():
    user_songs = {
        "David": ["song1", "song2", "song3", "song4", "song8", "song9"],
        "Emma": ["song5", "song6", "song7"],
    }

    song_genres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"],
    }

    assert favorite_genre(user_songs, song_genres) == {
        "David": ["Rock", "Techno", "Jazz"],
        "Emma": ["Pop"],
    }


def test_four():
    assert favorite_genre({}, {}) == {}
