users = ['john', 'becca', 'filip']

print(users)

users.insert(0, 'bob')

print(users)

users[2] = 'julie'

print(users)

users[2:2] = 'fred', 'joe'

print(users)

users[2:2] = ['adam', 'jamie']  # ['john', 'becca', 'fred', 'joe]'fred', 'joe'

print(users)

users[2:4] = 'felix', 'george'

print(users)

users.remove('julie')

print(users)

del users[0:2]

print(users)

users.sort()

print(users)

users[2:2] = 'jamie', 'jack'

print(users)

newUsers = list(users)

newUsers.reverse()

print(newUsers)

print(type(newUsers))

mytuple = (2, 3, 'fere', 3, 2, 3, 'fere')

print(mytuple.index('fere'))

newUsers[2:2] = 'gia', 'abel'

print(users)