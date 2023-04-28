import random

def create_deck():
    """生成一副扑克牌"""
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(f"{card} of {suit}")
    return deck

def deal_card(deck):
    """从牌堆中随机发一张牌"""
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_score(cards):
    """计算扑克牌的点数总和"""
    score = 0
    num_aces = 0

    for card in cards:
        if card.startswith("Ace"):
            score += 11
            num_aces += 1
        elif card.startswith("King") or card.startswith("Queen") or card.startswith("Jack"):
            score += 10
        else:
            score += int(card.split()[0])

    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1

    return score

def play_game():
    """开始21点游戏"""
    deck = create_deck()
    player_cards = [deal_card(deck), deal_card(deck)]
    dealer_cards = [deal_card(deck), deal_card(deck)]

    is_game_over = False

    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"你的牌：{player_cards}, 当前总点数：{player_score}")
        print(f"庄家的牌：{dealer_cards[0]}")

        if player_score == 21 or dealer_score == 21:
            is_game_over = True
        else:
            choice = input("要牌吗？请输入 y 或 n: ").lower()
            if choice == "y":
                player_cards.append(deal_card(deck))
            else:
                is_game_over = True

        if dealer_score < 17 and not is_game_over:
            dealer_cards.append(deal_card(deck))
        else:
            is_game_over = True

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"你的最终牌：{player_cards}, 最终总点数：{player_score}")
    print(f"庄家最终牌：{dealer_cards}, 最终总点数：{dealer_score}") 

    if player_score == 21 and dealer_score == 21:
        print("平局！")
    elif player_score == 21:
        print("恭喜，你赢了！")
    elif dealer_score == 21:
        print("很遗憾，你输了！")
    elif player_score > 21:
        print("很遗憾，你输了！")
    elif dealer_score > 21:
        print("恭喜，你赢了！")
    elif player_score > dealer_score:
        print("恭喜，你赢了！")
    else:
        print("很遗憾，你输了！")

# 开始游戏
play_game()
