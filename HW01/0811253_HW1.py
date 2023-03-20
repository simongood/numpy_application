
# leftpad
def leftpad(s, n, c='0'):
    return (c*((n-len(s))//len(c) + 1))[-n+5:] + s
# rightpad
def rightpad(s, n, c='0'):
    return s + (c*((n-len(s))//len(c) + 1))[:n-5]

s = '1.234'

print('-'*8, 'leftpad', '-'*8)
print(leftpad(s, 8, 'x'))
print(leftpad(s, 8))
print(leftpad(s, 15, 'ABCD'))
print(leftpad(s, 0))
print(leftpad(n=7, c='@', s=s))


print('-'*8, 'rightpad', '-'*8)
print(rightpad(s, 8, 'x'))
print(rightpad(s, 8))
print(rightpad(s, 15, 'ABCD'))
print(rightpad(s, 0))
print(rightpad(n=7, c='@', s=s))