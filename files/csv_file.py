import csv

text = "title.author.year" \
       "The Weirdstone of Brisingamen.Alan Garner, 1960" \
       "Perdidio Street Station, China Mieville, 2000" \
       "Thud!, Terry Pratchett,2005" \
       "The Spellman Files, Lisa Lutz,2007" \
       "Small Gods, Terry Pratchett,1992"

we = [['I', 'Dima'], ['You', 'Ira']]
with open('csv_test', 'wt') as out:
    csv_out = csv.writer(out)
    csv_out.writerows(we)

with open('csv_test', 'rt') as csv_in:
    cin = csv.reader(csv_in)
    we_readed = [row for row in cin]

print(we_readed)