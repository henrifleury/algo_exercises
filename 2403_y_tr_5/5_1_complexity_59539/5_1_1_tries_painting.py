test_f_name = 'input.txt'
f = open(test_f_name, 'r')

v_start, v_delta = list(map(int, f.readline().split()))
m_start, m_delta = list(map(int, f.readline().split()))
#print(v_start, v_delta, m_start, m_delta)

v_max, v_min = v_start + v_delta, v_start - v_delta
m_max, m_min = m_start + m_delta, m_start - m_delta

#print(v_max, v_min, m_max, m_min)
((l_max, l_min), (r_max, r_min)) = ((v_max, v_min), (m_max, m_min)) if v_min < m_min else ((m_max, m_min), (v_max, v_min))
#print(l_max, l_min, r_max, r_min)

if l_max >= r_min:
    print(max(l_max, r_max) - l_min +1)
else:
    #print(123)
    print((l_max-l_min+1)+(r_max-r_min+1))





