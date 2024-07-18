'''notes_nbr = int(input())
prev_note = int(input())
next_notes = [input().split() for _ in range(notes_nbr-1)]
next_notes = [(int(w[0]), str(w[1])) for w in next_notes]
'''
MIN_FR = 30
MAX_FR = 4000

def get_intervals(min_fr, max_fr, prev_fr, next_notes):

    #for note, dist in next_notes:
    #print("beg", min_fr, prev_note, note, max_fr)
    if len(next_notes) == 0:
        return float(min_fr), float(max_fr)
    else:
        cur_fr, dist_change = next_notes[0]
        delta = prev_fr - cur_fr
        if delta == 0:
            return float(cur_fr), float(cur_fr)
        else:
            if dist_change == "closer":
                if delta > 0:
                    max_fr = min(MAX_FR, max_fr, cur_fr + abs(delta)/2)
                else:
                    min_fr = max(MIN_FR, min_fr, cur_fr - abs(delta) / 2)
            else:
                if delta > 0:
                    min_fr = max(MIN_FR, min_fr, prev_fr - abs(delta) / 2)
                else:
                    max_fr = min(MAX_FR, max_fr, prev_fr+abs(delta)/2)
        return get_intervals(min_fr, max_fr, cur_fr, next_notes[1:])



#print(get_intervals(MIN_FR, MAX_FR, prev_note, next_notes))



print(*get_intervals(MIN_FR, MAX_FR, 440, [(220,"closer"), (300, "futher")]))
print(*get_intervals(MIN_FR, MAX_FR, 440, [(880,"futher"), (440, "closer"), (622, "closer")]))
print(get_intervals(MIN_FR, MAX_FR, 2705, [(117, 'closer'), (3697, 'further'), (1565, 'closer')]))# == [30.0, 1411.0]