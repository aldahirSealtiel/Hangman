nickname = input()
profession = input()
dominio = "http://example.com"
print('{dominio}/{nickname}/desirable/{profession}/profile'.format(dominio=dominio,
                                                                   nickname=nickname,
                                                                   profession=profession))
