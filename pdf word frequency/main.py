from PyPDF2 import PdfReader
import subprocess
reader = PdfReader("ExtremeBounds.pdf")
n = len(reader.pages)
page = reader.pages[0]
text=""
for page in reader.pages:
    text = text + page.extract_text()

text = text.encode('utf-8').decode('ascii', 'ignore')

with open("c.txt",'w') as textOut:
    textOut.write(text)

# cat b.txt | tr ' ' '\n' '?' ',' '.' | sort | uniq -c | sort -nr | head
# cat b.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | sed '1,/ 4 /d' | head -100

# final
# cat b.txt | tr -d '[:punct:]'  | tr ' ' '\n' | sort | uniq -ic | sort -nr | sed '1,/ 5 /d' | head -100



#subprocess.call(['wc','-l','textOut'])
