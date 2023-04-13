from random import randrange  # randrange(x이상,y미만)

result, count, countF = 0, 0, 0  # 평점 총합, 과목 수, F과목 수
total_open = total_submit = 0  # 열람용 학점합, 제출용 학점합
class_dic = {}  # key : 과목 코드 / Value : 과목 명
class_list = []  # 튜플(과목 코드, 학점, 평점)
loop = True  # 실행 유지

grade_num_dic = {}  # 과목 명 : 평점 숫자


def inp_grade():
    class_code = '%d' % randrange(10000, 100000)  # 임의의 코드 생성
    global count, countF, result, total_open, total_submit

    class_name = input("과목명을 입력하세요:\n")
    class_unit = int(input("학점을 입력하세요:\n"))
    class_grade_char = input("평점을 입력하세요:\n")

    match class_grade_char:
        case 'A+':
            class_grade = 4.5
        case 'A':
            class_grade = 4.0
        case 'B+':
            class_grade = 3.5
        case 'B':
            class_grade = 3.0
        case 'C+':
            class_grade = 2.5
        case 'C':
            class_grade = 2.0
        case 'D+':
            class_grade = 1.5
        case 'D':
            class_grade = 1.0
        case 'F':
            class_grade = 0.0
            countF += 1

    result = result + class_unit * class_grade  # 평점 합
    total_open += class_unit  # 학점 합

    if class_name in class_dic.values():  # 재수강 판별
        for i in range(0, len(class_list)):  # 튜플값 찾고 수정
            if class_grade > grade_num_dic[class_name]:
                class_list[i] = class_list[i][0:2] + (class_grade_char,)  # 슬라이싱해 평점 수정
            else:
                pass
    else:  # 재수강 아닐 때 값 추가
        class_dic[class_code] = class_name  # 사전 추가
        class_list.append((class_code, class_unit, class_grade_char))  # 과목 코드, 학점, 평점

    grade_num_dic[class_name] = class_grade  # 과목 명과 숫자 점수 기록

    if class_grade != 0:  # 평점이 F가 아닐 때 제출용 학점 추가
        total_submit += class_unit
    count += 1  # 과목 수 추가


def otp_grade():
    #print(class_list)
    for i in range(0, len(class_list)):
        print("[%s] %d학점: %s" % (class_dic[class_list[i][0]], class_list[i][1], class_list[i][2]))


def cal_grade():
    global loop
    print("제출용: %d학점 (GPA: %.2f)" % (total_submit, result / (count - countF)))
    print("열람용: %d학점 (GPA: %.2f)" % (total_open, result / count))

    print("\n프로그램을 종료합니다.\n")

    loop = False


while loop:  # 실행 창
    choice = input("작업을 선택하세요.\n1. 입력\n2. 출력\n3. 계산\n4. 종료\n")

    try:
        int(choice)  # 문자 입력 예외 처리
    except:
        print("다시 입력해주세요.\n")
        choice = input("작업을 선택하세요.\n1. 입력\n2. 출력\n3. 계산\n4. 종료\n")

    if int(choice) == 1:
        inp_grade()
    elif int(choice) == 2:
        otp_grade()
    elif int(choice) == 3:
        cal_grade()
    elif int(choice) == 4:
        print("프로그램을 종료합니다.\n")
        loop = False
    else:
        print("다시 입력해주세요.\n")
