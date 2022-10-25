from distance import distance as distance_fn, get_school_address

DISTANCE_WEIGHT = 2.
MOVIES_WEIGHT = 1.
MUSIC_WEIGHT = 1.
SPORT_WEIGHT = 1.
HOBBIES_WEIGHT = 1.
LANGUAGE_WEIGHT = 1.
SCHOOL_DISTANCE_WEIGHT = .5
SUBJECT_AREA_WEIGHT = .25
WAY_AFTER_SCHOOL_WEIGHT = .75
FAV_SUBJECT_WEIGHT = 0.5

def similarity(mentor, mentee):
    return basic_similarity(mentor, mentee)

def basic_similarity(mentor, mentee):
    distance_score = distance(mentor, mentee) * DISTANCE_WEIGHT
    movies_score = movies(mentor, mentee) * MOVIES_WEIGHT
    music_score = music(mentor, mentee) * MUSIC_WEIGHT
    sport_score = sport(mentor, mentee) * SPORT_WEIGHT
    hobbies_score = hobbies(mentor, mentee) * HOBBIES_WEIGHT
    language_score = language(mentor, mentee) * LANGUAGE_WEIGHT
    school_distance_score = distance_school(mentor, mentee) * SCHOOL_DISTANCE_WEIGHT
    subject_area_score = profession_sim(mentor, mentee) * SUBJECT_AREA_WEIGHT
    way_after_school_score = way_after_school_sim(mentor, mentee) * WAY_AFTER_SCHOOL_WEIGHT
    fav_subject_score = subject_sim(mentor, mentee) * FAV_SUBJECT_WEIGHT


    return sum([distance_score, movies_score, music_score, sport_score, hobbies_score, language_score, school_distance_score, subject_area_score, way_after_school_score, fav_subject_score])

def similarity_mentors(mentor1, mentor2):
    if mentor1.id == mentor2.id:
        return -100000.
    score = basic_similarity(mentor1, mentor2)
    
    return score


def distance(mentor, mentee):
    distance_km = distance_fn(mentor.address, mentee.address)

    if distance_km < 2:
        return 1.
    if distance_km < 4:
        return .75
    if distance_km < 6:
        return .5
    if distance_km < 8:
        return .25
    if distance_km < 10:
        return .1
    
    return 0.


def language(mentor, mentee):
    if mentor.native_language == mentee.native_language:
        return 1.
    if mentee.native_language in mentor.languages:
        return .75
    # intersection of languages
    if set(mentee.languages) & set(mentor.languages):
        return .5
    
    return 0.


def distance_school(mentor, mentee):
    school_address = get_school_address(mentee.school)

    if not school_address:
        return 0.

    distance_km = distance_fn(mentor.address, school_address)

    if distance_km < 2:
        return 1.
    if distance_km < 4:
        return .75
    if distance_km < 6:
        return .5
    if distance_km < 8:
        return .25
    if distance_km < 10:
        return .1
    
    return 0.



profession_match = {
   'Ingenieurwissenschaften' : ['Feuerwehrmann']
}


def profession_sim(mentor, mentee):
    if mentor.subject_area in profession_match:
        if mentee.dream_profession in profession_match[mentor.subject_area]:
            return 1.

    return 0.

def way_after_school_sim(mentor, mentee):
    mentee_goal = mentee.goal_after_school 

    if mentor.vocational_training and mentee_goal == 'Ausbildung':
        return 1.

    if mentor.second_chance_education and mentee_goal == 'Schule':
        return 1.

    if (mentor.vocational_training or mentor.second_chance_education) and mentee_goal == 'Weiß ich noch nicht.':
        return 0.5

    return 0. 


subject_match = {
    'Ingenieurwissenschaften' : ['Mathe']
}


def subject_sim(mentor, mentee):
    if mentor.subject_area not in subject_match:
        print("Studienrichtung not in list!")

        return 0.
    
    subjects = set(subject_match[mentor.subject_area])

    if len(subjects.intersection(mentee.fav_subjects)) > 0:
        return 1.

    return 0.


def cat_sim(set1: set, set2: set):
    return len(set1.intersection(set2)) / 3

def movies(mentor, mentee):
    return cat_sim(mentor.movies, mentee.movies)

def music(mentor, mentee):
    return cat_sim(mentor.musics, mentee.musics)

def sport(mentor, mentee):
    return cat_sim(mentor.sports, mentee.sports) 

def hobbies(mentor, mentee):
    return cat_sim(mentor.hobbies, mentee.hobbies)
    