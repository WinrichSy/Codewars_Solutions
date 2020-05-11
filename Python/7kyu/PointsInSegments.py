#Points in Segments
#https://www.codewars.com/kata/5baa25f3246d071df90002b7

def segments(m, a):
    seg_list = []
    for i in a:
        for j in range(i[0], i[1]+1):
            seg_list.append(j)

    seg_list = list(set(seg_list))

    ans = []
    m_range = [i for i in range(m+1)]
    for i in m_range:
        if i not in seg_list:
            ans.append(i)

    return ans
