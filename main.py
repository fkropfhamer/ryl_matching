import argparse
import csv
from mentee import Mentee
import numpy as np
from scipy.optimize import linear_sum_assignment

from mentor import Mentor
from similarity import similarity

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('mentor_file', type=str, help='path of mentor csv file')
    parser.add_argument('mentee_file', type=str, help='path of mentee csv file')
    parser.add_argument('-o', '--out_file', type=str, help='path for output file')
    parser.add_argument('-m', action='store_true')

    args = parser.parse_args()

    mentor_file_path = args.mentor_file
    mentors = create_mentors(mentor_file_path)

    if args.m:
        print("Matching mentors!")

        return
 
    mentee_file_path = args.mentee_file
    mentees = create_mentees(mentee_file_path)

    male_mentors, female_mentors, other_mentors = filter_gender(mentors)
    male_mentees, female_mentees, other_mentees = filter_gender(mentees)

    print("len: ", len(list(male_mentors)))
    print("len: ", len(list(male_mentees)))

    print("len: ", len(list(female_mentors)))
    print("len: ", len(list(female_mentees)))

    print("len: ", len(list(other_mentors)))
    print("len: ", len(list(other_mentees)))


    male_matches = calculate_scores(male_mentors, male_mentees)
    female_matches = calculate_scores(female_mentors, female_mentees)
    other_matches = calculate_scores(other_mentors, other_mentees)

    matches = male_matches + female_matches + other_matches

    if args.out_file:
        with open(args.out_file, 'w') as out_file:
            fieldnames = ['Mentor', 'Mentee', 'Score']
            writer = csv.DictWriter(out_file, fieldnames=fieldnames)

            writer.writeheader()
            rows = map(lambda match: { 'Mentor': match['mentor'].name, 'Mentee': match['mentee'].name, 'Score': match['score']}, matches)

            writer.writerows(rows)

def filter_gender(entities: list):
    MALE = "männlich"
    FEMALE = "weiblich"

    male_entities = list(filter(lambda m: m.gender == MALE, entities))
    female_entities = list(filter(lambda m: m.gender == FEMALE, entities))
    other_entities = list(filter(lambda m: m.gender not in [FEMALE, MALE], entities))

    return male_entities, female_entities, other_entities


def create_mentors(mentor_file_path: str) -> list[Mentor]:
    mentor_csv = read_csv_file(mentor_file_path)
    mentors = list(map(lambda row: Mentor.from_csv_row(row), mentor_csv))

    return mentors


def create_mentees(mentee_file_path: str) -> list[Mentee]:
    mentee_csv = read_csv_file(mentee_file_path)
    mentees = list(map(lambda row: Mentee.from_csv_row(row), mentee_csv))

    return mentees

def calculate_scores(mentors: list, mentees: list):
    cost_matrix = np.zeros((len(mentors), len(mentees)))

    for i, mentor in enumerate(mentors):
        for j, mentee in enumerate(mentees):
            score = similarity(mentor, mentee)

            cost_matrix[i][j] = -score


    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    matches = []

    for match in zip(row_ind, col_ind):
        print(match)
        mentor = mentors[match[0]]
        mentee = mentees[match[1]]

        score = cost_matrix[match[0]][match[1]]

        print(f"Matching {mentor.name} with {mentee.name} with a score of {-score}")

        matches.append({'mentee': mentee, 'mentor': mentor, 'score': -score})

    
    return matches



def read_csv_file(path: str) -> list:
    with open(path) as file:
        reader = csv.DictReader(file)

        return list(reader)

if __name__ == '__main__':
    main()
