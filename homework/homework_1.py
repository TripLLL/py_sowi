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

# In[22]:

Grundbegriffe = {'Symbolischer Interaktionismus' : {'Autor_innen': 'Mead, Weber, Parsons',
                                         'Definition': 'Interaktion ist im symbolischen Interaktionismus ein permanenter Prozess des Handelns, \n\
Beobachtens und Entwerfens weiterer Handlungen, in dem ego und alter wechselseitig die vermuteten Rollenerwartungen \
des anderen übernehmen oder ablehnen, darauf reagieren und weiteres Handeln antizipieren. \
Wechselseitige Interpretationen definieren die Situation, bestimmen, worum es geht oder nicht gehen soll, \
und leiten das Handeln an. Nicht vorgegebene Normen ermöglichen die Interaktion, sondern die gemeinsame Festlegung, \
welchen Sinn die Interaktion hat. Voraussetzung für das Gelingen von Interaktion ist die Fähigkeit zur Perspektivenübernahme. \
Diese Auffassung von Interaktion vertritt gegen das normative Paradigma das interpretative Paradigma. (Wikipedia)'},
                 'social norms' : {'Autor_innen': 'Cialdini, Baumeister',
                                 'Definition': 'There are two types of social norms that are identified in social psychology literature: \
descriptive norms and injunctive norms. „Descriptive norms refer to what most people \
in a group think, feel, or do“ (e.g. „Most Germans are punctual“), while „prescriptive or \
injunctive norms refer to what most people in a group approve of (e.g. „You shouldn’t \
come late to work“) (Baumeister & Vohs, 2007, p. 629). The distinction here is between \
what is true of group members (descriptive) and what ought to be true of group \
members (injunctive) (Baumeister & Vohs, 2007, p. 629). Both types of norms have \
been found to encourage norm-consistent behavior (Reno, Cialdini, & Kallgren, 1993).'},
                 'Alltagsrassismus' : {'Autor_innen': 'Hall, Balibar, Miles, Essed, Terkessides, Sow, Jäger',
                                       'Definition': 'Philomena Essed definiert Rassismus als ein alltägliches Phänomen. \
Es umfasst „eine Ideologie, eine Struktur und ein[en] Prozess, mittels derer bestimmte Gruppierungen \
auf der Grundlage tatsächlicher oder zugeschriebener biologischer oder kultureller Eigenschaften als wesensmäßig \
andersgeartete und minderwertige ‚Rassen‘ oder ethnische Gruppen angesehen werden (Essed 1992: 375).“ \
Dieser Definition liegt ein sehr breites Verständnis von Rassismus zugrunde, das neben biologischen und \
kulturellen Argumentationen die Rolle von Strukturen und Institutionen hervorhebt, \
die Rassismen re- und produzieren. Essed macht mit ihrem "Konzept des alltäglichen Rassismus" \
aus dem Jahr 1991 Rassismus als ideologisches Phänomen und \
als Teil der sozialen Struktur verständlich und erfasst dadurch Rassismus als ein alltägliches Phänomen, \
das die individuelle Wahrnehmung und somit die persönlichen Erfahrungen und \
Vorstellungen auf einer individuellen Ebene alltäglich stark beeinflusst (vgl. Essed 1991: 156ff.)'}
                                      }

print(Grundbegriffe['Alltagsrassismus']['Definition'])


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



