school_clases = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                  {'school_class': '4б', 'scores': [3,4,4,5,2]},
                  {'school_class': '4в', 'scores': [3,4,4,5,2]},
                  {'school_class': '4г', 'scores': [3,4,4,5,2]}]


student_list = []
score_list = []



def created_list():
    for i in school_clases:
        all_scores = i['scores']
        sum_scores_in_class = sum(all_scores)
        score_list.append(sum_scores_in_class)
        student_list.append(len(all_scores))

        
created_list()


print(sum(score_list) / sum(student_list))



