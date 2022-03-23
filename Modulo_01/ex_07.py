import re

texto = 'Es@te t-exto!! t?em? c.a.r.a.c.t.e.r.e.s. e,,,speciais'
remover_caracteres_especiais = re.sub('[,.?!@-]', '', texto)
print(remover_caracteres_especiais)