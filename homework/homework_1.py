# find jupyter notebook here: https://github.com/TripLLL/py_sowi/blob/master/homework/homework_1.py.ipynb
# coding: utf-8

# 1) **Schreibe folgenden Satz einmal vorwärts, einmal rückwärts (und lese ihn laut vor):**
# 
# Eins nutzt uns: Amore. Die Rederei da, die Rederei der Omas, nutzt uns nie.
# 

# In[1]:

a = 'Eins nutzt uns: Amore. Die Rederei da, die Rederei der Omas, nutzt uns nie.'

print("1.1 vorwärts: " + a)
print("1.2 rückwärts: " + a[::-1])


# 2) **Schreibe folgende Regel 100 Mal untereinander auf den Bildschirm:**
# 
# Ich darf meine Arbeit nicht abkürzen!
# 
# 
# 

# In[2]:

for i in range(100):
    print(i+1 , ": " + "Ich darf meine Arbeit nicht abkürzen!")


# 3)  **Schreibe a groß und b klein**
# 
# string functions: https://docs.python.org/2/library/string.html
# 
# 

# In[3]:

a = 'apfel' 
b = 'ESSEN'

print(a.upper())
print(b.lower())


# 4) Erzeuge/schreibe einen String, in dem sowohl einfache (') als auch doppelte (")  als auch dreifach-einfache (''') als auch dreifach-doppelte (""") Anführungszeichen vorkommen.

# In[4]:

print("Anführungszeichen gibt es in verschiedenen Ausführeungen: \nsie können \'einfach\' vorkommen, oder \"doppelt-einfach\", \naber auch \'''dreifach\''' oder \"\"\"dreifach-doppelt\"\"\" auftauchen. ")


# 5) **Erstelle ein Handbuch soziologischer "Grundbegriffe". Darin sollten sich mindestens drei Grundbegriffe (deiner Wahl) nachschlagen lassen. Zu jedem dieser Begriffe sollten sich wiederum zwei Dinge nachschlagen lassen:**
# 
# a) eine kurze "Definition" in zwei, drei Sätzen
# 
# b) eine Liste mit Namen der wichtigsten "Autor_innen" zu diesem Begriff, z.B. <print Grundbegriffe['Soziale Systeme']['Autor_innen']> gibt <['Luhmann', 'Parsons']> zurück
# 

# In[23]:

Grundbegriffe = {'soziale Interaktion' : {'Autor_innen': 'Mead, Robert',
                                         'Definition1': 'kurze def 1'},
                 'feminismus' : {'Autor_innen': 'hooks, bell',
                                 'Definition2': 'kurze def 2'},
                 'dritter Grundbegriff' : {'Autor_innen': 'dritte Autorin',
                                          'Definition3': 'kurze def 3'}
                }

print(Grundbegriffe['soziale Interaktion']['Definition1'])


# 6) **Challenge: zerlege folgenden soziologischen Grundbegriff in seine Einzelteile (gemeint sind hier natürlich die Zeichen des Strings!), sortiere diese alphabetisch (und zwar unabhängig von Groß- und Kleinschreibung!) und gebe sie als einen neuen String wieder aus, in dem wieder nur das erste Zeichen groß geschieben ist:**
# 
# *Tipp 1: schau dir dazu mal sowohl die list() Funktion als auch die join() Funktion für strings an*
# 
# Super challenge: schreib die Lösung für 6) in einen einzigen Print Befehl
# 
# 
# list of functions: https://docs.python.org/2/library/functions.html#func-list
# join doku: https://www.tutorialspoint.com/python/string_join.htm
# 

# In[58]:

# multi line

a = "Signifier"
b = sorted(a.lower())
c = "".join(b)
print("multiline:",  c.title())

# one- line <3
print("one-line:", "".join(sorted(a.lower())).title())


# In[ ]:



