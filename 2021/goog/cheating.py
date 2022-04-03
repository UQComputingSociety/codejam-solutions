from collections import defaultdict
import math

T = int(input())
P = int(input())

num_questions = 10000
num_students = 100

for t in range(T):
    t += 1
    results = [[] for x in range(num_students)]
    num_correct_by_student = [None] * num_students
    all_correct_answers = 0
    for p in range(num_students):
        results[p] = [int(x) for x in input().rstrip()]
        num_correct_by_student[p] = sum(results[p])
        all_correct_answers += num_correct_by_student[p]


    expected_cheated_answers = 0.5 * num_questions
    proportion_cheated = expected_cheated_answers / all_correct_answers
    proportion_not_cheated = 1 - proportion_cheated

    num_correct_by_question = [0] * num_questions

    for q in range(num_questions):
        for s in range(num_students):
            num_correct_by_question[q] += results[s][q]

    print(num_correct_by_question)

    for i in range(len(num_correct_by_question)):
        num_correct_by_question[i] *= proportion_not_cheated

    # assume average student has skill 0, then work backwards to find expected question difficulty.
    question_difficulty = [None] * num_questions

    for q in range(len(question_difficulty)):
        p = num_correct_by_question[q] / num_students
        question_difficulty[q] =  min(3, max(-3,math.log(1/p - 1)))

    print(question_difficulty)
    print(min(question_difficulty), max(question_difficulty))

    student_skill = [None] * num_students
    for s in range(len(results)):
        prop = num_correct_by_student[s] / num_questions
        student_skill[s] = min(3, max(-3, -math.log(1/prop - 1)))

    print(student_skill)

    l = []
    for s in range(num_students):
        expected_correct = 0
        delta = []
        for q in range(num_questions):
            skill = student_skill[s]
            question = question_difficulty[q]
            x = skill - question
            expected_correct += 1 / (1 + math.exp(-x))
            delta.append(results[s][q] - 1 / (1 + math.exp(-x)))
        exp = expected_correct
        actual = num_correct_by_student[s]
        # print(s, exp, actual, exp / actual)
        l.append((sum(delta), actual / exp, exp, actual, s))
    l.sort()
    print(*l, sep='\n')

    print(sum(question_difficulty) / len(question_difficulty))
    print(sum(student_skill) / len(student_skill))