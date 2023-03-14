"""Converting US spelling rules to
 NZ spelling"""

import easygui

word = easygui.enterbox("type in a sentence")
letters = list(word)
letters_to_remove = "u"
print(letters)
position = (word.find(letters_to_remove))

bj