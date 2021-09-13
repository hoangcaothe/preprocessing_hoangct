from preprocessing_hoangct import utils

__version__ = '0.0.1'

def get_words_count(x):
    return utils._get_words_count(x)


def get_chars_count(x):
    return utils._get_chars_count(x)


def get_avg_wordlength(x):
    return utils._get_avg_wordlength(x)


def get_stopwords_count(x):
    return utils._get_stopwords_count(x)


def get_hashtags_count(x):
    return utils._get_hashtags_count(x)


def get_mentions_count(x):
    return utils._get_mentions_count(x)


def get_digits_count(x):
    return utils._get_digits_count(x)


def get_uppercase_count(x):
    return utils._get_uppercase_count(x)


def get_cont_exp(x):
    return utils._get_cont_exp(x)


def get_emails(x):
    return utils._get_emails(x)


def remove_emails(x):
    return utils._remove_emails(x)


def get_urls(x):
    return utils._get_urls(x)


def remove_urls(x):
    return utils._remove_urls(x)


def remove_rt(x):
    return utils._remove_rt(x)


def remove_special_chars(x):
    return utils._remove_special_chars(x)


def remove_html_tags(x):
    return utils._remove_html_tags(x)


def remove_accented_chars(x):
    return utils._remove_accented_chars(x)


def remove_stopwords(x):
    return utils._remove_stopwords(x)


def make_base(x):
    return utils._make_base(x)


def remove_common_words(x, n=20):
    return utils._remove_common_words(x, n)


def remove_rare_words(x, n=20):
    return utils._remove_rare_words(x, n)


def spelling_correction(x):
    return utils._spelling_correction(x)



