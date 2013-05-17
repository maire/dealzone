import leaf,requests

class Deal:
  name = None
  new_price = None
  orig_price = None

  def __init__(self, name, new_price, orig_price):
    self.name = name
    self.new_price = new_price
    self.orig_price = orig_price

def getSteamDeals():
  deals = []
  page = requests.get('http://store.steampowered.com/search/?sort_by=Metascore&sort_order=DESC&specials=1')
  temp = leaf.parse(page.text)
  links = temp('.search_result_row.even') + temp('.search_result_row.odd')
  for link in links:
    deals.append(Deal(link('.col.search_name.ellipsis')[0]('h4')[0].text,
                       link('.col.search_price')[0]('br')[0].tail,
                       link('.col.search_price')[0]('strike')[0].text))
  return deals