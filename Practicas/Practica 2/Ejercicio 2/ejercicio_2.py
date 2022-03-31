from collections import Counter


texto = """The constants defined in this module are:The constants defined in,
this module are:

string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants,
described below. This value is not locale-dependent.

string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not,
locale-dependent and will not change.

string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not,
locale-dependent and will not change.""".lower().split()

cnt = Counter()
cnt1 = Counter(texto)

for palabra in texto:
    cnt[palabra] += 1
print(cnt)

print(cnt1)
cont = Counter(texto).most_common(1)

print(cont)
