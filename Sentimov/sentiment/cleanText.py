import re
from nltk.corpus import wordnet

def replace_via(str):
    str = str.replace("via", "")
    return str

def replace_hashtag(str, movie_name):
    str = str.replace(movie_name, "movie")
    return str

def replaceEmoji(str):
    dict = {u'\U0001f923': 'laugh_emo',
            u'\U0001f924': 'drooling_emo',
            u'\U0001f910': 'zipper_emo',
            u'\U0001f911': 'money_emo',
            u'\U0001f913': 'nerd_emo',
            u'\U0001f914': 'thinking_emo',
            u'\U0001f917': 'hug_emo',
            u'\U0001f644': 'rolling_emo',
            u'\U0001f641': 'frown_emo',
            u'\U0001f643': 'upside-down_emo',
            u'\U0001f642': 'smile_emo',
            u'\U0001f44d': 'thumbs-up_emo',
            u'\U0001f44e': 'thumbs-down_emo',
            u'\U0001f635': 'dizzy_emo',
            u'\U0001f634': 'sleep_emo',
            u'\U0001f636': 'silent_emo',
            u'\U0001f631': 'scream_emo',
            u'\U0001f630': 'sweat_emo',
            u'\U0001f633': 'flushed_emo',
            u'\U0001f632': 'astonished_emo',
            u'\U0001f44d\U0001f3fb': 'thumbs-up_emo',
            u'\U0001f44d\U0001f3fe': 'thumbs-up_emo',
            u'\U0001f44d\U0001f3ff': 'thumbs-up_emo',
            u'\U0001f44d\U0001f3fc': 'thumbs-up_emo',
            u'\U0001f44d\U0001f3fd': 'thumbs-up_emo',
            u'\U0001f625': 'whew_emo',
            u'\U0001f624': 'won_emo',
            u'\U0001f627': 'anguished_emo',
            u'\U0001f626': 'frown_emo',
            u'\U0001f621': 'angry_emo',
            u'\U0001f623': 'persevere_emo',
            u'\U0001f622': 'cry_emo',
            u'\U0001f62d': 'cry_emo',
            u'\U0001f62c': 'grimace_emo',
            u'\U0001f62f': 'hushed_emo',
            u'\U0001f62e': 'sympathy_emo',
            u'\U0001f629': 'weary_emo',
            u'\U0001f628': 'scared_emo',
            u'\U0001f62b': 'tired_emo',
            u'\U0001f62a': 'sleep_emo',
            u'\U0001f615': 'confused_emo',
            u'\U0001f614': 'pensive_emo',
            u'\U0001f617': 'kiss_emo',
            u'\U0001f616': 'confounded_emo',
            u'\U0001f611': 'expressionless_emo',
            u'\U0001f610': 'deadpan_emo',
            u'\U0001f613': 'cold sweat_emo',
            u'\U0001f612': 'unhappy_emo',
            u'\U0001f61d': 'tongue_emo',
            u'\U0001f61c': 'joke_emo',
            u'\U0001f61f': 'worried_emo',
            u'\U0001f61e': 'disappointed_emo',
            u'\U0001f619': 'kiss_emo',
            u'\U0001f618': 'kiss_emo',
            u'\U0001f61b': 'tongue_emo',
            u'\U0001f61a': 'kiss_emo',
            u'\U0001f605': 'cold sweat_emo',
            u'\U0001f604': 'smile_emo',
            u'\U0001f606': 'smile_emo',
            u'\U0001f601': 'grin_emo',
            u'\U0001f600': 'grin_emo',
            u'\U0001f603': 'smile_emo',
            u'\U0001f602': 'laugh_emo',
            u'\U0001f60d': 'heart-eye_emo',
            u'\U0001f60c': 'relieved_emo',
            u'\U0001f60f': 'smirk_emo',
            u'\U0001f60e': 'cool sun glasses_emo',
            u'\U0001f609': 'wink_emo',
            u'\U0001f60b': 'yum_emo',
            u'\U0001f60a': 'smile_emo',
            u'\U0001f9e1': 'heart_emo',
            u'\U0001f495': 'heart_emo',
            u'\U0001f494': 'heart_emo',
            u'\U0001f497': 'heart_emo',
            u'\U0001f496': 'heart_emo',
            u'\U0001f493': 'heart_emo',
            u'\U0001f49d': 'heart_emo',
            u'\U0001f49c': 'heart_emo',
            u'\U0001f49f': 'heart_emo',
            u'\U0001f49e': 'heart_emo',
            u'\U0001f499': 'heart_emo',
            u'\U0001f498': 'heart_emo',
            u'\U0001f49b': 'heart_emo',
            u'\U0001f49a': 'heart_emo',
            u'\u263a': 'smile_emo',
            u'\u2764': 'heart_emo',
            u'\u2639': 'frown_emo',
            u'\U0001f44e\U0001f3fb': 'thumbs-down_emo',
            u'\U0001f44e\U0001f3fd': 'thumbs-down_emo',
            u'\U0001f44e\U0001f3fc': 'thumbs-down_emo',
            u'\U0001f44e\U0001f3ff': 'thumbs-down_emo',
            u'\U0001f44e\U0001f3fe': 'thumbs-down_emo',
            u'\U0001f5a4': 'heart_emo'
            }
    for emoji in dict.keys():
        str = str.replace(emoji.encode('utf-8'), " "+dict[emoji])

    emoji_pattern = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]|[\u2600-\u26FF\u2700-\u27BF]+',flags=re.UNICODE)
    data=str.decode('utf-8')
    data = emoji_pattern.sub(r'', data)
    data = re.sub(r'[\:\;\=][\)\]]','smile',data)
    data = re.sub(r'[\:\;\=][\(\[]', 'sad', data)
    return data.encode('utf-8')

def removeURL(str):
    str = re.sub(r'https\S+','',str)
    return str

def removeRT(str):
    str = re.sub(r'rt\W@\S+: ', '', str)
    return str

def removeAcc(str):
    str = re.sub(r'@\S+','some_acc',str)
    return str

def remove_repeated_characters(tokens):
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'
    def replace(old_word):
        if wordnet.synsets(old_word):
            return old_word
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word
    correct_tokens = [replace(word) for word in tokens]
    return correct_tokens
