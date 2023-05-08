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


user_list = []


def set_user_class(class_name, credit, gpa):
    user = UserCourse()
    user_list.append(user)
    if class_name in user.taken_course_name:
        past_gpa = user.name_to_gpa[class_name]
        if get_gpa_score(gpa) >= get_gpa_score(past_gpa):  # 이전 리스트 안 학적 정보 삭제
            course_index = user.taken_course_list.index((user.taken_course_name[class_name], credit, past_gpa))
            del user.taken_course_list[course_index]
            course_inform = (user.taken_course_name[class_name], credit, gpa)  # 기존 과목 코드 유지
        else:
            pass
    else:  # 처음 등록이므로 과목 코드 생성 및 등록
        class_code = str(randrange(10000, 100000))
        user.taken_course_name[class_code] = class_name
        user.taken_course_name[class_name] = class_code
        course_inform = (class_code, credit, gpa)  # 학적 정보 생성

    user.taken_course_list.append(course_inform)  # 정보 입력
    user.name_to_gpa[class_name] = gpa
    return user


class UserCourse:
    taken_course_name = {}  # 과목 코드 : 과목명 & 과목명 : 과목 코드

    def __init__(self, name):
        self.name = name
        self.taken_course_list = []
        self.name_to_gpa = {}


while True:  # 실행창
    print(
        '작업을 선택하세요.\n'
        '1. 입력\n'
        '2. 출력\n'
        '3. 조회\n'
        '4. 계산\n'
        '5. 학생 변경\n'
        '6. 종료'
    )
    match input():
        case '1':  # 입력
            class_name = input('과목명을 입력하세요 : ')
            credit = int(input('학점을 입력하세요 : '))
            gpa = input('평점을 입력하세요 : ')

            set_user_class(class_name, credit, gpa)  # return user( = UserCourse() )

            print('입력되었습니다.')
            continue

        case '2':  # 출력
            for taken_course in user_list:  # 클래스 인스턴스화 불러오기
                taken_class_name = taken_course.taken_course_name[taken_course[0]]
                print('[{0}] {1}학점: {2}'.format(taken_course.taken_class_name, taken_course.taken_course[1], taken_course.taken_course[2]))
            continue

        case '3':  # 조회
            continue

        case '4':  # 계산
            submit_credit, archive_credit, submit_gpa, archive_gpa = calculate_gpa()
            print('제출용: {0}학점 (GPA: {1})'.format(submit_credit, submit_gpa))
            print('열람용: {0}학점 (GPA: {1})'.format(archive_credit, archive_gpa))
            pass

        case '5':  # 종료
            pass

        case _:  # 예외 처리
            print("잘못된 입력입니다. 다시 시도해주세요.")
            continue

    print('프로그램을 종료합니다.')
    break
