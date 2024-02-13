import gettext

# Set language
lang = 'en_US'
_ = gettext.translation('messages', localedir='locale', languages=[lang]).gettext
print(_("Hello, World!"))