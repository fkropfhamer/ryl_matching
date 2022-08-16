from distance import distance as distance_fn

DISTANCE_WEIGHT = 2
MOVIES_WEIGHT = 1
MUSIC_WEIGHT = 1
SPORT_WEIGHT = 1
HOBBIES_WEIGHT = 1

def similarity(mentor, mentee):
    distance_score = distance(mentor, mentee) * DISTANCE_WEIGHT
    movies_score = movies(mentor, mentee) * MOVIES_WEIGHT
    music_score = music(mentor, mentee) * MUSIC_WEIGHT
    sport_score = sport(mentor, mentee) * SPORT_WEIGHT
    hobbies_score = hobbies(mentor, mentee) * HOBBIES_WEIGHT

    return distance_score + movies_score + music_score + sport_score + hobbies_score

def similarity_mentors(mentor, mentor):
    return 1

def distance(mentor, mentee):
    distance_km = distance_fn(mentor.address, mentee.address)

    if distance_km < 2:
        return 1
    if distance_km < 4:
        return .75
    if distance_km < 6:
        return .5
    if distance_km < 8:
        return .25
    if distance_km < 10:
        return .1
    
    return 0


def language(mentor, mentee):
    if mentor.native_language == mentee.native_language:
        return 1
    if mentee.native_language in mentor.languages:
        return .75
    # intersection of languages
    if set(mentee.languages) & set(mentor.languages):
        return .5
    
    return 0


def distance_school(distance_km):
    if distance_km < 2:
        return 1
    if distance_km < 4:
        return .75
    if distance_km < 6:
        return .5
    if distance_km < 8:
        return .25
    if distance_km < 10:
        return .1
    
    return 0


def cat_sim(list1, list2):
    return len(x in list2 for x in list1) / 3

def movies(mentor, mentee):
    return cat_sim(mentor.movies, mentee.movies)

def music(mentor, mentee):
    return cat_sim(mentor.musics, mentee.musics)

def sport(mentor, mentee):
    return cat_sim(mentor.sports, mentee.sports) 

def hobbies(mentor, mentee):
    return cat_sim(mentor.hobbies, mentee.hobbies)
    