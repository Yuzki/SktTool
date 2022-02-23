def ngram(sent, n):
    word_list = list(sent)
    # word_list.append('$')
    # word_list.insert(0, '#')
    ngram_list = [word_list[idx: idx + n] for idx in range(len(word_list) - n + 1)]

    return([''.join(s) for s in ngram_list])


# samhita = 'y;o jAt;a ev;a praTam;o m;anasvAn'
# pada = 'y;aH jAt;aH ev;a praTam;aH m;anasvAn'
# print(' '.join(ngram(samhita.replace(' ', 'Z'), 5)))
# print(ngram(pada, 5))
sent = 'y/o+hatv/āhim'
print(' '.join(ngram(sent, 3)))
