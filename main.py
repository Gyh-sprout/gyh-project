from random import randrange


def get_gpa_score(gpa):  # gpa 숫자로
    match gpa:
        case 'A+':
            return 4.5
        case 'A':
            return 4
        case 'B+':
            return 3.5
        case 'B':
            return 3
        case 'C+':
            return 2.5
        case 'C':
            return 2
        case 'D+':
            return 1.5
        case 'D':
            return 1
        case 'F':
            return 0


def calculate_gpa():  # gpa 계산
    submit_gpa, archive_gpa = 0, 0
    submit_credit, archive_credit = 0, 0

    for taken_course in taken_course_list:
        gpa_score = get_gpa_score(taken_course[2])

        if taken_course[2] != 'F':
            submit_gpa += taken_course[1] * gpa_score
            submit_credit += taken_course[1]
        archive_gpa += taken_course[1] * gpa_score
        archive_credit += taken_course[1]

    submit_gpa /= submit_credit
    archive_gpa /= archive_credit
    return submit_credit, archive_credit, submit_gpa, archive_gpa


name_to_gpa = {}  # 과목명 : 평점
taken_course_name = {}  # 과목 코드 : 과목명 & 과목명 : 과목 코드
taken_course_list = []  # (과목 코드, 학점, 평점)

while True:
    print(
        '작업을 선택하세요.\n'
        '1. 입력\n'
        '2. 출력\n'
        '3. 계산'
    )
    match input():
        case '1':  # 입력
            class_name = input('과목명을 입력하세요 : ')
            credit = int(input('학점을 입력하세요 : '))
            gpa = input('평점을 입력하세요 : ')

            if class_name in taken_course_name:
                past_gpa = name_to_gpa[class_name]
                if get_gpa_score(gpa) >= get_gpa_score(past_gpa):  # 이전 리스트 안 학적 정보 삭제
                    course_index = taken_course_list.index((taken_course_name[class_name], credit, past_gpa))
                    del taken_course_list[course_index]
                    course_inform = (taken_course_name[class_name], credit, gpa)  # 기존 과목 코드 유지
                else:
                    print(
                        '평점이 전보다 낮습니다.\n'
                        '입력을 중단합니다.'
                    )
                    continue
            else:  # 처음 등록이므로 과목 코드 생성 및 등록
                class_code = str(randrange(10000, 100000))
                taken_course_name[class_code] = class_name
                taken_course_name[class_name] = class_code
                course_inform = (class_code, credit, gpa)  # 학적 정보 생성

            taken_course_list.append(course_inform)  # 정보 입력
            name_to_gpa[class_name] = gpa

            print('입력되었습니다.')
            continue

        case '2':  # 출력
            for taken_course in taken_course_list:
                taken_class_name = taken_course_name[taken_course[0]]
                print('[{0}] {1}학점: {2}'.format(taken_class_name, taken_course[1], taken_course[2]))
            continue

        case '3':  # 계산
            submit_credit, archive_credit, submit_gpa, archive_gpa = calculate_gpa()
            print('제출용: {0}학점 (GPA: {1})'.format(submit_credit, submit_gpa))
            print('열람용: {0}학점 (GPA: {1})'.format(archive_credit, archive_gpa))

        case _:  # 예외 처리
            print("잘못된 입력입니다. 다시 시도해주세요.")
            continue

    print('프로그램을 종료합니다.')
    break
