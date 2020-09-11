from datetime import datetime
datum = datetime.now()
import locale
locale.setlocale(locale.LC_TIME, 'nl_NL')
print("Hello You!, ik ben Aidan")
print("De datum en tijd is: ", datum.strftime('%A %d %B %Y'))
print("Wie ben jij?")
naamvanandere = input()
print("Hello " + naamvanandere)
