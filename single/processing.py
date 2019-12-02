

tags = {'symptome':'HDM', 'antecedent':'ATD', 'modevie':'MDV', 'traitement':'TRT', 'sujetconsultation':'MTF', 'unknow':'UNK', 'personal':'PSN'}
with open('qa.txt') as f:
    i = 0
    for line in f:
        i = i + 1
        if line.strip().lower().startswith('q:'):
            line = line.strip().lower().replace('q:', '')
            line = line.split()
            dc = '{}{:04}'.format(tags[line[-1].strip('?')], i)
            with open('doctor.txt', 'a', encoding='utf8') as ff:
                ff.write('{} +++ {}\n'.format(dc,  ' '.join(line[:-1])))
        elif line.strip().lower().startswith('a:'):
            line = line.strip().lower().replace('a:', '')
            #line = line.split()
            pc = 'P{:04}'.format(i)
            with open('patient.txt', 'a', encoding='utf8') as ff:
                ff.write('{} +++ {}\n'.format(pc,  line))
                
            with open('d_p.txt', 'a', encoding='utf8') as ff:
                ff.write('{} +++ {}\n'.format(dc,  pc))
            
