from collections import Counter

card_order_part1 = "23456789TJQKA"
card_order_part2 = "J23456789TQKA"

def upgrade_hand(hand):
    if hand == "JJJJJ": return hand
    hand_i = map(card_order_part2.index, [c for c in hand if c != "J"])
    occurences = sorted(Counter(hand_i).items(), key=lambda c: (-c[1], -c[0]))
    return hand.replace("J", card_order_part2[occurences[0][0]])

def score_hand(hand, card_order, upgrade):
    card_values = tuple(map(card_order.index, hand))
    count = sorted(Counter(hand if not upgrade else upgrade_hand(hand)).values(), reverse=True)
    return count, card_values

lines = open("input.txt").read().splitlines()
hands_values = [line.split() for line in lines]
hands, values = zip(*hands_values)
values = list(map(int, values))

scores_part1 = map(lambda hand: score_hand(hand, card_order_part1, False), hands)
combined_part1 = sorted(list(zip(scores_part1, hands, values)))
part1 = sum( [ (f+1) * c[2] for f, c in enumerate(combined_part1)] )
print(part1)

scores_part2 = map(lambda hand: score_hand(hand, card_order_part2, True), hands)
combined_part2 = sorted(list(zip(scores_part2, hands, values)))
part2 = sum( [ (f+1) * c[2] for f, c in enumerate(combined_part2)] )
print(part2)