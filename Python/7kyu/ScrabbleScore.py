#Scrabble Score
#https://www.codewars.com/kata/558fa34727c2d274c10000ae

def scrabble_score(st):
    ans = 0
    st = st.replace(' ','')
    if st == '':
        return ans

    for i in st.upper():
        ans += dict_scores[i]

    return ans
