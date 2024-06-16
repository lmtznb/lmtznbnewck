import random

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def determine_bet_result(bet, dice, bet_amount):
    dice_sum = sum(dice)
    if bet == 1 and dice_sum <= 10:
        return "压中了小！", 1.5 * bet_amount
    elif bet == 2 and dice_sum >= 11:
        return "压中了大！", 1.5 * bet_amount
    elif bet == 3 and len(set(dice)) == 1:
        return "压中了豹子！", 2.25 * bet_amount
    else:
        return "没有压中。", 0 * bet_amount

def calculate_bet_amount(fund, bet_type):
    if bet_type == 1:
        return fund // 3
    elif bet_type == 2:
        return (2 * fund) // 3
    elif bet_type == 3:
        return fund
    return 0

def play_dice_game():
    fund = 200
    fuzhai = 0
    shouzhi = 10
    gebo = 2
    erduo = 2
    yanjing = 2
    yaozhi = 2
    niuzhi = 1

    while fund > -5000000:
        bet = int(input("请输入压注类型（1: 小，2: 大，3: 豹子）："))
        bet_type = int(input("请输入压注金额类型（1: 压三分之一，2: 压三分之二，3: 全部）："))

        bet_amount = calculate_bet_amount(fund, bet_type)
        if bet_amount <= 0 or bet not in [1, 2, 3] or bet_type not in [1, 2, 3]:
            print("无效的压注类型或金额，不进行压注。")
            continue

        dice = roll_dice()
        print("摇骰子结果：", dice)

        result, win_amount = determine_bet_result(bet, dice, bet_amount)
        fund -= bet_amount
        fund += win_amount
        print(f"资金更新：{fund}元")

        if fund < 10:
            fuzhai += 10000
            fund += 10000
            print("资金不足已贷款")
            print("贷款总额：", fuzhai)
            print("当前资金：", fund)

            # 检查并处理身体部位的丧失
            if fuzhai > 100000 and shouzhi > 0:
                shouzhi -= 1
                print(f"你已经失去了一根手指，剩余手指：{shouzhi}")
            if fuzhai > 200000 and gebo > 0:
                fuzhai = fuzhai + 90000
                gebo = gebo - 1
                geboa = 2 - gebo
                print(f"你已经失去了{geboa}条胳膊！")
            if fuzhai > 400000 and erduo > 0:
                fuzhai = fuzhai + 90000
                erduo = erduo - 1
                erduoa = 2 - erduo
                print(f"你已经失去了{erduoa}个耳朵！")
            if fuzhai > 600000 and yanjing > 0:
                fuzhai = fuzhai + 90000
                yanjing = yanjing - 1
                yanjinga = 2 - yanjing
                print(f"你已经失去了{yanjinga}个眼睛！")
            if fuzhai > 800000 and yaozhi > 0:
                fuzhai = fuzhai + 90000
                yaozhi = yaozhi - 1
                yaozhia = 2 - yaozhi
                print(f"你已经失去了{yaozhia}个腰子！")
            if fuzhai > 1000000 and niuzhi > 0:
                fuzhai = fuzhai + 90000
                niuzhi = niuzhi - 1
                niuzhia = 1 - niuzhi
                print(f"你已经失去了{niuzhia}个牛至！")

        print(result)

play_dice_game()