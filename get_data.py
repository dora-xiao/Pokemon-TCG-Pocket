import json

regex_used = """<tr>
<td class="center"><\/td>
<td class="center"><b class='a-bold'>([A-Za-z0-9-]{2,3}) ([0-9]{3})<\/b><\/td>

<td class="center">
  <div class='imageLink js-archive-open-image-modal' data-image-url='(https:\/\/img\.game8\.co\/.+)' data-micromodal-trigger='js-archive-open-image-modal' data-archive-url=''><img src='.+>([a-zA-Z- '0-9.]+)<\/a>
 
 
 <\/td>

<td class="center"><img src='.+' class='a-img lazy lazy-non-square' alt='Pokemon TCG Pocket - (◇*|☆*|♛*|Promo) rarity' data-src='.*'.*<hr class="a-table__line">.*

.*<\/b> <br> *([ a-zA-Z-]+)<\/td>"""

cardfile = open("data/cards.txt", "r", encoding='utf-8')
lines = cardfile.readlines()

result = {"A1": {}, "A1a": {}, "A2": {}, "P-A": {}}
for i in range(len(lines) // 6):
    rarity_type = ""
    if("◇" in lines[6*i+4]):
        rarity_type = "diamond"
    elif("☆" in lines[6*i+4]):
        rarity_type = "star"
    elif("Promo" in lines[6*i+4]):
        rarity_type = "promo"
    else:
        rarity_type = "crown"

    result[lines[6*i].replace("\n","")][(lines[6*i+1].replace("\n",""))] = {
        "img": lines[6*i+2].replace("\n",""),
        "name": lines[6*i+3].replace("\n",""),
        "rarity": {
            "type": rarity_type,
            "count": len(lines[6*i+4].replace("\n","")) 
        },
        "pack": lines[6*i+5].replace("\n","")
    }

with open('data/cards.json', 'w') as f:
    json.dump(result, f)
