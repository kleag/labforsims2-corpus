import sys
from sklearn.feature_extraction.text import CountVectorizer
tags = {'symptome':'05', 'antecedent':'04', 'modevie':'02', 'traitement':'03', 'sujetconsultation':'00', 'unknow':'06', 'personal':'01'}

tags_2 = {'HDM':'05', 'ATD':'04', 'MDV':'02', 'TRT':'03', 'MTF':'00', 'UNK':'06', 'PSN':'01'}

categories = {'symptome': {'beginning_of_pain':'debut', 'has_fever':'fievre', 'fever': 'fievre', 'take_temperature':'fievre', 'pain_elsewhere_abdomen':'changement', 'kind_of_pain':'type', 'dark_urine':'description', 'pale_stools':'description', 'place_of_pain':'localisation', 'has_vomited':'description', 'normal_stools':'description', 'other_diseases':'description', 'rate_pain':'description', 'has_changed':'changement', 'position_calm_pain':'evolution', 'no':'autre', 'reason_consultation':'description', 'after_diner':'declencheur', 'has_eaten':'declencheur', 'still_badly':'evolution', 'has_gas':'description', 'breath_well':'description', 'jaunisse':'description', 'medecine_calm_pain':'evolution', 'has_nausea':'description', 'burns_pee':'description', 'diner':'declencheur', 'description':'description', 'other':'description', 'localisation':'localisation'}, 
              'antecedent': {'medical_history':'maladie', 'contraceptions':'contraceptions', 'operations':'chrirugie', 'atcd_health':'maladie', 'beginning_of_pain':'maladie', 'atcd_heath':'maladie', 'no':'autre', 'last_period':'grossesse', 'other_diseases':'maladie', 'allergies':'allergie', 'atcd_family':'famille', 'exams_before_coming':'examen', 'has_pregnancy':'grossesse', 'has_child':'grossesse', 'regime':'regime', 'pregnancy':'grossesse', 'kind_of_pain':'maladie'},
              'modevie': {'addictions':'addictions', 'traveled_recently':'voyages', 'sport':'sport', 'voyages':'voyages', 'no':'autre', 'patient_address':'adresse', 'has_child':'habitation', 'origine':'autre'},
              'traitement':{'medecine_calm_pain':'mode', 'no':'type', 'mode':'mode', 'type':'type', 'contraceptions':'mode'},
              'sujetconsultation':{'sujetconsultation':'objet', 'reason_consultation':'objet', 'kind_of_pain':'objet'},
              'personal': {'address':'adresse', 'married':'etat_civil', 'childreen':'enfant', 'no':'autre', 'patient_age':'age', 'patient_profession':'profession', 'patient_address':'adresse', 'patient_name':'nom', 'has_child':'enfant', 'family':'origine', 'weigth':'poids', 'patient_origin':'origine', 'has_married':'etat_civil'}}
              #'unknow':'autre'}

categories_ids = {'symptome_debut': '000', 'symptome_fievre': '001', 'symptome_changement': '002', 'symptome_type': '003', 'symptome_description': '004', 'symptome_localisation': '005', 'symptome_evolution': '006', 'symptome_autre': '007', 'symptome_declencheur': '008', 'antecedent_maladie': '000', 'antecedent_contraceptions': '001', 'antecedent_chrirugie': '002', 'antecedent_autre': '003', 'antecedent_grossesse': '004', 'antecedent_allergie': '005', 'antecedent_famille': '006', 'antecedent_examen': '007', 'antecedent_regime': '008', 'modevie_addictions': '000', 'modevie_voyages': '001', 'modevie_sport': '002', 'modevie_autre': '003', 'modevie_adresse': '004', 'modevie_habitation': '005', 'traitement_mode': '000', 'traitement_type': '001', 'sujetconsultation_objet': '000', 'personal_adresse': '000', 'personal_etat_civil': '001', 'personal_enfant': '002', 'personal_autre': '003', 'personal_age': '004', 'personal_profession': '005', 'personal_nom': '006', 'personal_origine': '007', 'personal_poids': '008', 'unknow_autre':'000'}

#cat = dict()
#for i in range(1,10):
    #data = "Interne {}/data".format(i)
    #output = "Interne{}/dialogues".format(i)
    #with open(data) as f:
        #for j, line in enumerate(f):
            #sc = None
            #line = line.strip()
            #if len(line) > 0:
                #line = line.split('==>')
                #q = line[0]
                #r = line[2].split()
                #cl = line[1].strip()
                #if '.' in r[-1]:
                    #sc = r[-1].split('.')[-1]
                #elif cl != 'unknow':
                    #print('from {} at {} {}'.format(data, j, q))
                    
                #if cl not in tags.keys():
                    #print('error classe from {} at {} {}'.format(data, j, q))
                #elif sc is not None and cl in cat.keys() and sc not in cat[cl]:
                    #cat[cl].append(sc)
                #elif sc is not None and not cl in cat.keys():
                    #cat[cl] = [sc]
                ##if cl == 'unknow' and sc == 'sujetconsultation':
                    ##print('from {} at {} {}'.format(data, j, q))
                    
#for c, ct in cat.items():
    #print('{} :: {}'.format(c, ct))
##print('stats {}'.format(cat))
                    
###categories_ids = dict()
###for cat, ssc in categories.items():
    ###v = 0
    ###for a , b in ssc.items():
        ###c = '{}_{}'.format(cat, b)
        ###vv = '{:03d}'.format(v)
        ###if c not in categories_ids.keys():
            ###v = v + 1
            ###categories_ids[c] = vv
###print(categories_ids)

#for i in range(1,10):
    #data = "Interne {}/data".format(i)
    #output = "Interne {}/dialogues".format(i)
    #responses_ = "Interne {}/reponses.txt".format(i)
    #resp_ = list()
    #with open(responses_) as f:
        #for line in f:
            #resp_.append(line.strip())
    #with open(data) as f:
        #for j, line in enumerate(f):
            #sc = None
            #line = line.strip()
            #if len(line) > 0:
                #line = line.split('==>')
                #q = line[0]
                #cl = line[1].strip()
                #r = line[2].split()
                #if cl != 'unknow' and '.' in r[-1]:
                    #sc = r[-1].split('.')[-1]
                    #print(cl, sc)
                    #sc = categories[cl][sc]
                    #r = ' '.join(r[:-1])
                #elif cl == 'unknow':
                    #sc = 'autre'
                    #r = ' '.join(r)
                #if sc is not None:
                    ##print(categories[cl])
                    
                    #code_sc = categories_ids['{}_{}'.format(cl, sc)]
                #else:
                    #sys.exit('from {} at {} {}'.format(data, j, q))
                #code_q = 'd{:02d}{}{}{}'.format(i, tags[cl], code_sc, j)
                #code_r = 'p{:02d}{}{}{}'.format(i, tags[cl], code_sc, j)
                
                #with open(output, 'a', encoding='utf8') as ff:
                    #ff.write('{} {}\n'.format(code_q, q))
                    #ff.write('{} {}\n'.format(code_r, resp_[j]))

tags = {'symptome':'05', 'antecedent':'04', 'modevie':'02', 'traitement':'03', 'sujetconsultation':'00', 'unknow':'06', 'personal':'01'}


cat_numbers = dict()
# compter les occurences
dialogues_data = list()
mots_par_phrases_par_categories_doctor = dict()
mots_par_phrases_par_categories_patient = dict()
mots_par_dialogues_doctor = dict()
mots_par_dialogues_patient = dict()
phrases_dialogues_doctor = list()
phrases_dialogues_patient = list()
for i in range(1,42):
    #data = "Interne{}/data".format(i)
    if i < 10:
        data = "Interne0{}/dialogues".format(i)
    else:
        data = "Interne{}/dialogues".format(i)
    with open(data) as f:
        for j, line in enumerate(f):
            if line.strip().startswith('d'):
                cat = line.strip().split()[0][3:5]
                if cat in cat_numbers.keys():
                    cat_numbers[cat] = cat_numbers[cat] + 1
                else:
                    cat_numbers[cat] = 1
                if cat in mots_par_phrases_par_categories_doctor.keys():
                    mots_par_phrases_par_categories_doctor[cat].append(len(line.split())-1)
                else:
                    mots_par_phrases_par_categories_doctor[cat] = [len(line.split())-1]
                    
                if i in mots_par_dialogues_doctor.keys():
                    mots_par_dialogues_doctor[i].append(' '.join(line.split()[1:]))
                else:
                    mots_par_dialogues_doctor[i] = [' '.join(line.split()[1:])]
                phrases_dialogues_doctor.append(' '.join(line.split()[1:]))
            else:
                if cat in mots_par_phrases_par_categories_patient.keys():
                    mots_par_phrases_par_categories_patient[cat].append(len(line.split())-1)
                else:
                    mots_par_phrases_par_categories_patient[cat] = [len(line.split())-1]
                    
                if i in mots_par_dialogues_patient.keys():
                    mots_par_dialogues_patient[i].append(' '.join(line.split()[1:]))
                else:
                    mots_par_dialogues_patient[i] = [' '.join(line.split()[1:])]
                phrases_dialogues_patient.append(' '.join(line.split()[1:]))
                
            dialogues_data.append(' '.join(line.strip().split()[1:]))
                    
print('for dialogues \n')
somme = 0
for t, t_ in tags.items():
    print('{} : total {} mean {}'.format(t, cat_numbers[t_]*2, cat_numbers[t_]*2/1416*100))
    somme = somme + cat_numbers[t_]*2
print('for dialogues: total sentences: {}'.format(somme))
#print(mots_par_phrases_par_categories_patient)
nbr_mots_doctor = 0
nbr_mots_patient = 0

for t, t_ in tags.items():
    lst_t = mots_par_phrases_par_categories_doctor[t_]
    print('Doctor - {} nbre de mots/phrases {}'.format(t, sum(lst_t)/len(lst_t)))
    nbr_mots_doctor = nbr_mots_doctor + sum(lst_t)
    
    lst_t = mots_par_phrases_par_categories_patient[t_]
    print('patient - {} nbre de mots/phrases {}'.format(t, sum(lst_t)/len(lst_t)))
    nbr_mots_patient = nbr_mots_patient + sum(lst_t)

print("dialogues patient - nombres de mots au total {}".format(nbr_mots_patient))
print("dialogues doctor - nombres de mots au total {}".format(nbr_mots_doctor))
#with tags_2
cat_numbers = dict()
data = "../doctor.txt"
with open(data) as f:
    for j, line in enumerate(f):
        c = line[0:3]
        if tags_2[c] in cat_numbers.keys():
            cat_numbers[tags_2[c]] = cat_numbers[tags_2[c]] + 1
        else:
            cat_numbers[tags_2[c]] = 1
print('single-turns \n')  
somme = 0
for t, t_ in tags.items():
    print('{} : total {} mean {}'.format(t, cat_numbers[t_]*2, cat_numbers[t_]*2/5402*100))
    somme = somme + cat_numbers[t_]*2
print(' single-turns: total sentences: {}'.format(somme))
    
import spacy, string
from spacy.vocab import Vocab
from collections import Counter
word_counter = Counter()
dataq = "../doctor.txt"
datar = "../patient.txt"
dp_text = "../d_p.txt"
responses = list()
def get_data(filename, type_data=0, dp=None):
    data = list()
    with open(filename) as f:
        for j, line in enumerate(f):
            if type_data == 0 and dp is None: # questions 
                data.append(' '.join(line.strip().split()[2:]))
            elif type_data == 1 and dp is not None:
                if line.strip().startswith(dp):
                    data.append(' '.join(line.strip().split()[1:]))
            elif type_data == 2 and dp is None:
                data.append(line.strip())
    return data
print('single-turn')
questions = get_data(dataq)
responses = get_data(datar)
responses_with_ids = get_data(datar, type_data=2)
dp_qr = get_data(dp_text, type_data=2)
dps = dict()
for line in dp_qr:
    line = line.strip().split('+++')
    dps[line[0].strip()] = line[1].strip()
resp_ids = dict()
for line in responses_with_ids:
    line = line.strip().split()
    resp_ids[line[0].strip()] = ' '.join(line[2:])
    
    
    
questions_with_label = get_data(dataq, type_data=2)

nlp = spacy.load('fr')
def get_vocab(data):
    cv=CountVectorizer()
    word_count_vector=cv.fit_transform(data)
    #cv.get_feature_names()
    #vocab = Vocab(strings=data, lemmatizer=True)
    #print(list(vocab.strings))
    return cv.get_feature_names()

single_data = get_vocab(questions)
single_data.extend(get_vocab(responses))
#for s in questions:
    #word_counter.update(s.split())
#for s in responses:
    #word_counter.update(s.split())
#print(word_counter)
print('vocabulary single turn = {}'.format(len(set(single_data))))
# vocabulary of dialogues
print('vocabulary dialogues = {}'.format(len(get_vocab(dialogues_data))))

# le nombre de mots par phrases par catégories
# single-turns
mots_par_phrases_single_doctor = dict()
mots_par_phrases_single_patient = dict()
for i, q in enumerate(questions_with_label):
    cat = q[0:3]
    #print(cat)
    ques = ' '.join(q.split()[2:])
    #print(ques)
    res = resp_ids[dps[q.split()[0].strip()]]
    if cat in mots_par_phrases_single_doctor.keys():
        mots_par_phrases_single_doctor[cat].append(len(ques.split()))
    else:
        mots_par_phrases_single_doctor[cat] = [len(ques.split())]
    if cat in mots_par_phrases_single_patient.keys():
        mots_par_phrases_single_patient[cat].append(len(res.split()))
    else:
        mots_par_phrases_single_patient[cat] = [len(res.split())]
        
for cat, lst in mots_par_phrases_single_doctor.items():
    print('Single Doctor - {} nbre de mots/phrases {}'.format(cat, sum(lst)/len(lst)))
    lst_t = mots_par_phrases_single_patient[cat]
    print('Single patient - {} nbre de mots/phrases {}'.format(cat, sum(lst_t)/len(lst_t)))
    
print("\n\n Vocabulary \n\n")
#print("Vocabulary about single turn \n\n")
#q = get_vocab(questions)
#r = get_vocab(responses)
#print("doctor vocabulary {}\n".format(len(get_vocab(questions))))
#print("patient vocabulary {}\n\n".format(len()))
print("Vocabulary about dialogues \n\n")
with open('data.dat', 'a', encoding='utf8') as f:
    f.write("D T doctorW patientW Vd Vp Vdp\n")
moy = list()
for i, lst_lines in mots_par_dialogues_doctor.items():
    lines_q = set(' '.join(lst_lines).split())
    lines_r = set(' '.join(mots_par_dialogues_patient[i]).split())
    with open('data.dat', 'a', encoding='utf8') as f:
        f.write("{} {} {} {} {} {} {}\n".format(i, len(lines_q) + len(lines_r), len(lines_q)/(len(lines_q) + len(lines_r))*100, len(lines_r)/(len(lines_q) + len(lines_r))*100, len(set(get_vocab(lst_lines)) - set(get_vocab(mots_par_dialogues_patient[i]))), len( set(get_vocab(mots_par_dialogues_patient[i])) - set(get_vocab(lst_lines)) ),  len( set(get_vocab(mots_par_dialogues_patient[i])) & set(get_vocab(lst_lines))) ))
    moy.append(len(lines_q) + len(lines_r))
    print("nbre de mots total in {} est égal : {}".format(i, len(lines_q) + len(lines_r)))
    print("nbre de mots doctor in {} est égal : {}".format(i, len(lines_q)))
    print("nbre de mots patient in {} est égal : {}".format(i, len(lines_r)))
    print("vocab specific doctor in {} est égal : {}".format(i, len(set(get_vocab(lst_lines)) - set(get_vocab(mots_par_dialogues_patient[i]))) ))
    print("vocab specific patient in {} est égal : {}".format(i, len( set(get_vocab(mots_par_dialogues_patient[i])) - set(get_vocab(lst_lines)) ) ))
    print("vocab common to patient and doctor in {} est égal : {}".format(i, len( set(get_vocab(mots_par_dialogues_patient[i])) & set(get_vocab(lst_lines)) ) ))
print('moy {}'.format(sum(moy)/len(moy)))
#print("doctor vocabulary {}\n".format(len(get_vocab(phrases_dialogues_doctor))))
#print("patient vocabulary {}\n".format(len(get_vocab(phrases_dialogues_patient))))

### entities
#all_data = dialogues_data + questions + responses
#nytimes = nlp(' '.join(all_data))
#entities=[i.label_ for i in nytimes.ents]
#print(set(entities))
    
    


#print(doc.vocab.length)
#print(len(vocab_patient))
#print(list(doc.vocab.strings))
#print(doc.vocab['traitement'])
#punctuation = string.punctuation  
#lst_words = [w for q in questions for w in q.split()]
#lst_words = [' '.join(w.split('-')) if '-' in w else w for w in lst_words ]
#lst_words2 = list()
#for w in lst_words:
    #if len(w.split()) > 0:
        #for ww in w.split():
            #lst_words2.append(ww)
    #else:
        #lst_words2.append(w)
#lst_words = lst_words2
##lst_words = [' '.join(w.split('-')) if '-' in w else w for w in lst_words ]
#lst_words = [''.join(c for c in s if c not in punctuation) for s in lst_words]
#any(punctuation in ww for punctuation in string.punctuation)
#for ww in lst_words:
    #if any(punctuation in ww for punctuation in string.punctuation):
        
#lst_words = [w for ]
#questions = set(lst_words)
#print(questions)
#print(len(questions))

        
                
