def playing_domino(cards, deck):
    
    max_count = 0
    max_card = None

    for card in cards:
        if card[0] in deck or card[1] in deck:
            count = cards.count(card)
            if count > max_count:
                max_count = count
                max_card = card

    return max_card if max_card else []


if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []