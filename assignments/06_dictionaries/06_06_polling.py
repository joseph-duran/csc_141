'''Joseph Duran
Chapter 6
This program will show people's favorite programming languages.
6/10
'''

favorite_languages = {
    'Joseph': 'Python',
    'Brad': 'JavaScript',
    'Kate': 'C++',
    'Hailee': 'Java',
    'Mike': 'C#'}
for favorite_Language in favorite_languages.keys():
    print(favorite_Language.title() + "'s favorite language is " + favorite_languages[favorite_Language].title() + ".")
    