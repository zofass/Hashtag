import string

user_input = input("Please enter a sentence: ")
def create_hashtag(sentence):
    words = sentence.split()
    words = [word.capitalize() for word in words]
    hashtag = ''.join(words)
    hashtag = ''.join(char for char in hashtag if char.isalnum())
    hashtag = hashtag[:140]
    hashtag = '#' + hashtag

    return hashtag

result_hashtag = create_hashtag(user_input)
print(result_hashtag)
