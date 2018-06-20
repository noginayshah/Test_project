def get_talk(calltype='shout'):
    def shout(word='Yes'):
        return word.upper() + '!!!'
    def whisper(word='Yes'):
        return word.lower() + '...'
    if calltype == 'shout':
        return shout
    else:
        return whisper
# print(get_talk())
print(get_talk()('Hello'))
# ren = get_talk()
# print(ren())