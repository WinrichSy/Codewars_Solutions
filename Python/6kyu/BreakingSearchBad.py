#Breaking Search Bad
#https://www.codewars.com/kata/52cd53948d673a6e66000576

def search(titles, term):
    return list(filter(lambda title: term in title.lower(), titles))
