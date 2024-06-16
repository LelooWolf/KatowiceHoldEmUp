# J - 11, Q - 12, K - 13, A - 14
def get_value(card):
    return int(card[:-1])


def get_color(card):
    return card[-1]


def get_values_only(hand):
    hand_value = []
    for card in hand:
        hand_value.append(int(card[:-1]))
    return hand_value


def is_same_color(hand):
    # get color of the first card
    color = hand[0][-1]
    # check color of the first card against all other cards, return truth value
    return all(card[-1] == color for card in hand)


def is_in_sequence(hand):
    hand = get_values_only(hand)
    for i in range(0, len(hand[:-1])):
        # hand[:-1] protects loop from grabbing out of scope values
        if (int(hand[i]) - int(hand[i + 1])) != 1:
            # will check current card against the next card in hand
            return False
    return True


def is_multiple(hand):
    if type(hand[0]) is not int:
        hand = get_values_only(hand)
    for card in hand:
        if hand.count(card) > 1:
            return [hand.count(card), int(card)]
    return False

def card_check(hand):
    hand = hand.sort(reversed=True)
    if is_in_sequence(hand):
        if is_same_color(hand):



def what_hand(hand):
    print(f"Is straight flush: {is_same_color(hand) and is_in_sequence(hand)}")
    print(f"Is four: N/A")
    print(f"Is full house: N/A")
    print(f"Is flush: {is_same_color(hand)}")
    print(f"Is straight: {is_in_sequence(hand)}")
    print(f"Is three: N/A")
    print(f"Is two pairs: N/A")
    print(f"Is single pair: N/A")
    print(f"High card: {get_value(hand[0])}")


def update_score(new, current):
    if new[0] > current[0]: current = new
    return current


hand = ['7s', '8s', '9s', '5s', '5s']
hand_score = []
hand.sort(reverse=True, key=get_value)
print(hand)
print(f"Is same color: {is_same_color(hand)}")
print(f"Is in sequence: {is_in_sequence(hand)}")
check_1 = is_multiple(hand)
print(f"Check numbers first: {check_1}")
if check_1:
    hand_copy = get_values_only(hand)
    for _ in range(0, check_1[0]):
        hand_copy.remove(check_1[1])
    check_2 = is_multiple(hand_copy)
    print(f"Check numbers secnd: {check_2}")
    if check_2:
        if check_1[0]+check_2[0] == 4:
            # two pairs
            new_score = [2, check_2[1]]
        else:
            # two and three - full house
            new_score = [6, check_2[1]]
    else:
        if check_1[0] == 2:
            new_score = []
        else:
            new_score =
    update_score()

print("")
what_hand(hand)
