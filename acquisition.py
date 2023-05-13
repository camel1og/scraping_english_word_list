import ssWrite
import random
import time

# スプシ情報取得
workbooks = ssWrite.accessSpleadSheet()
worksheet = workbooks.worksheet('中学一年生単語一覧')

# 中1の英単語全取得（449単語）
all_date = worksheet.get_all_values()

#正解数と間違い数
correct = 0
error = 0

for num in range(3):
    # 単語ランダム取得（4単語）
    question_lists = random.sample(all_date,4)
    print(f'題{num + 1}門')
    
    #ランダムで取得データの英単語のみ格納
    questions = []
    for question_list in question_lists:
        questions.append(question_list[0])

    #ランダムで取得データの日本語のみ格納
    ansers = []
    for question_list in question_lists:
        ansers.append(question_list[1])

    # 問題出題
    question = random.sample(questions,1)#4つの中から問題を選ぶ
    print(f'4つ中から「{question[0]}」の意味の選択をしてください')

    #4択選択表示
    for i, choice in enumerate(ansers):
        print(f'{i + 1}. {choice}' )

    #ユーザー入力
    user_anser = input("選択してください:1,2,3,4：")

    #答えとユーザー入力の判定
    if (questions.index(question[0]) + 1) == int(user_anser):
        print('正解です')
        correct = correct + 1
    else:
        print('不正解です')
        print(f'答えは：「{ansers[questions.index(question[0])]}」です')
        error = error + 1

#正解率
Accuracy_Rate = correct / 3
print(f'あなたの正解率は{round(Accuracy_Rate * 100, 1)}%です')
