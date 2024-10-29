import sys

testcase = int(sys.stdin.readline())
for _ in range(testcase):
    n = int(sys.stdin.readline())

    applicants = []
    for idx in range(n):
        a, b = map(int, sys.stdin.readline().split())
        applicants.append((a, b, idx))

    isEmployed = [1 for _ in range(n)]

    applicants.sort() # sorted by document rating
    last_interview_rating = applicants[0][1]
    for applicant in applicants:
        _, interview_rating, idx = applicant
        if last_interview_rating < interview_rating:
           isEmployed[idx] = 0
        else:
            last_interview_rating = interview_rating

    applicants.sort(key=lambda x:x[1])
    last_document_rating = applicants[0][0]
    for applicant in applicants:
        document_rating, _, idx = applicant
        if last_document_rating < document_rating:
            isEmployed[idx] = 0
        else:
            last_document_rating = document_rating

    print(sum(isEmployed))