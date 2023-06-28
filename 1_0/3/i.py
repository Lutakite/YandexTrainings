n = int(input())
langs = dict()
for i in range(n):
    m = int(input())
    for i in range(m):
        lang = input()
        langs[lang] = langs.get(lang, 0) + 1

everyonelangs = set()
for lang in langs:
    if langs[lang] == n:
        everyonelangs.add(lang)
print(len(everyonelangs))
for lang in everyonelangs:
    print(lang)
print(len(langs))
for lang in langs:
    print(lang)