
def split_tweet(in_text):

    tweet_length = 140
    post_length = 10

    if len(in_text) < tweet_length:
        return [in_text]

    text_arr = in_text.split(' ');

    out_text = [[]]
    curr_idx = 0
    curr_len = 0;
    for text in text_arr:
        if curr_len + len(text) > tweet_length - post_length:
            out_text.append([text])
            curr_len = len(text)+1
            curr_idx += 1
        else:
            out_text[curr_idx].append(text)
            curr_len += len(text)+1

    X = [' '.join(o) for o in out_text]
    for i in range(0,len(X)):
        X[i] += ' (%d of %d)'%(i+1, len(X))

    return X


if __name__ == '__main__':
    X = split_tweet("For if, because of one man's trespass, death reigned through that one man, much more will those who receive the abundance of grace and the free gift of righteousness reign in life through the one man Jesus Christ.")
    print([len(x) for x in X])
    print(X)
