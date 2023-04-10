import Cards


def detect_cards(videostream, ranks, suits):
    image = videostream.read()
    processed_image = Cards.preprocess_image(image)
    cnts_sort, cnt_is_card = Cards.find_cards(processed_image)

    if len(cnts_sort) == 0:
        return [[], []]
    cards = []
    k = 0
    for i in range(len(cnts_sort)):
        if (cnt_is_card[i] == 1):
            cards.append(Cards.preprocess_card(cnts_sort[i], image))
            cards[k].best_rank_match, cards[k].best_suit_match, cards[k].rank_diff, cards[k].suit_diff = Cards.match_card(cards[k], ranks, suits)
            k = k + 1
    retval = [[x.best_suit_match, x.best_rank_match] for x in cards]
    return retval
