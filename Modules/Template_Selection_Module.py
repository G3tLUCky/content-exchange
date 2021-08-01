import random
import numpy as np
import Ruleset_module as Ruleset
import copy

def Template_Selection(leg, temp, data, idx):
    sentence_types = ['Title', 'Tests', 'Infections', 'Admissions', 'Clinique', 'IC', 'Deaths', 'Vaccines']
    possible_titles = []
    possible_tests = []
    possible_infections = []
    possible_admissions = []
    possible_clinique = []
    possible_ic = []
    possible_deaths = []
    possible_vaccines = []
    text = []

    template_combinations = [['gen_sentence', 'numbers', 'comparison'], ['gen_sentence', 'num_comparison'],\
                                     ['numbers', 'comparison'], ['num_comparison'], ['gen_sentence', 'gen_numbers', 'comparison'],\
                                         ['gen_numbers', 'comparison'], ['gen_num_comparison'], ['gen_sentence', 'gen_num_comparison'],\
                                             ['total_numbers', 'comparison']]  
    for comb in template_combinations[:8]:
        new_comb = copy.deepcopy(comb)
        new_comb.append('total')
        template_combinations.append(new_comb)



    template_combinations_constants = [['gen_sentence', 'numbers'], ['numbers'],\
                                   ['gen_sentence', 'gen_numbers', 'num_previous'], ['gen_numbers', 'num_previous'],\
                                      ['total_numbers', 'num_previous']]
    

    for s in sentence_types:
        if s == 'Title':
            general_template = random.choice(temp[leg.index("Title, general (general)")])
            general_title = [('Tests', 0.1), ('Infections', 0.5), ('Admissions', 0.2), ('Clinique', 0.2), ('IC', 0.2), ('Deaths', 0.3), ('Vaccines', 0.3)]
            general_choice = random.choice(general_title)
            possible_titles.append([general_template, general_choice[1], general_choice[0]])
        
            if Ruleset.Tests_Yesterday(data, idx) == "increase" or Ruleset.Tests_Week(data, idx) == "increase":
                template = random.choice(temp[leg.index("Title, increase (general)")])
                possible_titles.append([template, 0.1, 'Tests', 'increase'])
            if Ruleset.Infections_Yesterday(data, idx) == "increase" or Ruleset.Infections_Week(data, idx) == "increase":
                template = random.choice(temp[leg.index("Title, increase (general)")])
                peak_template = random.choice(temp[leg.index("Title, peaks (general)")])
                possible_titles.append([template, 0.5, 'Infections', 'increase'])
                possible_titles.append([peak_template, 0.2, 'Infections', 'increase'])
            if Ruleset.Admissions_Yesterday(data, idx) == "increase" or Ruleset.Admissions_Week(data, idx) == "increase":
                template = random.choice(temp[leg.index("Title, increase (general)")])
                peak_template = random.choice(temp[leg.index("Title, peaks (general)")])
                possible_titles.append([template, 0.2, 'Admissions', 'increase'])
                possible_titles.append([peak_template, 0.1, 'Admissions', 'increase'])
            if Ruleset.Clinique_Yesterday(data, idx) == "increase" or Ruleset.Clinique_Week(data, idx) == "increase":
                template = random.choice(temp[leg.index("Title, increase (general)")])
                possible_titles.append([template, 0.2, 'Clinique', 'increase'])
            if Ruleset.IC_Yesterday(data, idx) == "increase" or Ruleset.IC_Week(data, idx) == "increase":
                template = random.choice(temp[leg.index("Title, increase (general)")])
                possible_titles.append([template, 0.2, 'IC', 'increase'])
            if Ruleset.Deaths_Yesterday(data, idx) == "increase" or Ruleset.Deaths_Week(data, idx) == "increase":
                template = random.choice(temp[leg.index("Title, increase (general)")])
                peak_template = random.choice(temp[leg.index("Title, peaks (general)")])
                possible_titles.append([template, 0.3, 'Deaths', 'increase'])
                possible_titles.append([peak_template, 0.1, 'Deaths', 'increase'])
            if Ruleset.Vaccines_Yesterday(data, idx) == "increase" or Ruleset.Vaccines_Week(data, idx) == "increase":
                template = random.choice(temp[leg.index("Title, increase (general)")])
                possible_titles.append([template, 0.3, 'Vaccines', 'increase'])
            
            if Ruleset.Tests_Yesterday(data, idx) == "decrease" or Ruleset.Tests_Week(data, idx) == "decrease":
                template = random.choice(temp[leg.index("Title, decrease (general)")])
                possible_titles.append([template, 0.1, 'Tests', 'decrease'])
            if Ruleset.Infections_Yesterday(data, idx) == "decrease" or Ruleset.Infections_Week(data, idx) == "decrease":
                template = random.choice(temp[leg.index("Title, decrease (general)")])
                peak_template = random.choice(temp[leg.index("Title, peaks (general)")])
                possible_titles.append([template, 0.5, 'Infections', 'decrease'])
                possible_titles.append([peak_template, 0.2, 'Infections', 'decrease'])
            if Ruleset.Admissions_Yesterday(data, idx) == "decrease" or Ruleset.Admissions_Week(data, idx) == "decrease":
                template = random.choice(temp[leg.index("Title, decrease (general)")])
                peak_template = random.choice(temp[leg.index("Title, peaks (general)")])
                possible_titles.append([template, 0.2, 'Admissions', 'decrease'])
                possible_titles.append([peak_template, 0.1, 'Admissions', 'decrease'])
            if Ruleset.Clinique_Yesterday(data, idx) == "decrease" or Ruleset.Clinique_Week(data, idx) == "decrease":
                template = random.choice(temp[leg.index("Title, decrease (general)")])
                possible_titles.append([template, 0.2, 'Clinique', 'decrease'])
            if Ruleset.IC_Yesterday(data, idx) == "decrease" or Ruleset.IC_Week(data, idx) == "decrease":
                template = random.choice(temp[leg.index("Title, decrease (general)")])
                possible_titles.append([template, 0.2, 'IC', 'decrease'])
            if Ruleset.Deaths_Yesterday(data, idx) == "decrease" or Ruleset.Deaths_Week(data, idx) == "decrease":
                template = random.choice(temp[leg.index("Title, decrease (general)")])
                peak_template = random.choice(temp[leg.index("Title, peaks (general)")])
                possible_titles.append([template, 0.3, 'Deaths', 'decrease'])
                possible_titles.append([peak_template, 0.1, 'Deaths', 'decrease'])
            if Ruleset.Vaccines_Yesterday(data, idx) == "decrease" or Ruleset.Vaccines_Week(data, idx) == "decrease":
                template = random.choice(temp[leg.index("Title, decrease (general)")])
                possible_titles.append([template, 0.3, 'Vaccines', 'decrease'])
            
            if Ruleset.Tests_Yesterday(data, idx) == "constant" or Ruleset.Tests_Week(data, idx) == "constant":
                template = random.choice(temp[leg.index("Title, constants (general)")])
                possible_titles.append([template, 0.1, 'Tests', 'constant'])
            if Ruleset.Infections_Yesterday(data, idx) == "constant" or Ruleset.Infections_Week(data, idx) == "constant":
                template = random.choice(temp[leg.index("Title, constants (general)")])
                possible_titles.append([template, 0.3, 'Infections', 'constant'])
            if Ruleset.Admissions_Yesterday(data, idx) == "constant" or Ruleset.Admissions_Week(data, idx) == "constant":
                template = random.choice(temp[leg.index("Title, constants (general)")])
                possible_titles.append([template, 0.1, 'Admissions', 'constant'])
            if Ruleset.Clinique_Yesterday(data, idx) == "constant" or Ruleset.Clinique_Week(data, idx) == "constant":
                template = random.choice(temp[leg.index("Title, constants (general)")])
                possible_titles.append([template, 0.1, 'Clinique', 'constant'])
            if Ruleset.IC_Yesterday(data, idx) == "constant" or Ruleset.IC_Week(data, idx) == "constant":
                template = random.choice(temp[leg.index("Title, constants (general)")])
                possible_titles.append([template, 0.1, 'IC', 'constant'])
            if Ruleset.Deaths_Yesterday(data, idx) == "constant" or Ruleset.Deaths_Week(data, idx) == "constant":
                template = random.choice(temp[leg.index("Title, constants (general)")])
                possible_titles.append([template, 0.2, 'Deaths', 'constant'])
            if Ruleset.Vaccines_Yesterday(data, idx) == "constant" or Ruleset.Vaccines_Week(data, idx) == "constant":
                template = random.choice(temp[leg.index("Title, constants (general)")])
                possible_titles.append([template, 0.2, 'Vaccines', 'constant'])
            
            titles = [i[0] for i in possible_titles]
            weights = [i[1] for i in possible_titles]
            titles_normalized = [i/sum(weights) for i in weights]
            title = np.random.choice(titles, p = titles_normalized)
            if len(possible_titles[titles.index(title)]) > 3:
                title_and_type = [title, possible_titles[titles.index(title)][2], possible_titles[titles.index(title)][3]]
                text.append(title_and_type)
            else:
                title_and_type = [title, possible_titles[titles.index(title)][2]]
                text.append(title_and_type)
        
        
        if s == 'Tests' and Ruleset.Tests_Yesterday(data, idx) != "error":
            if Ruleset.Tests_Yesterday(data, idx) == "increase" or Ruleset.Tests_Week(data, idx) == "increase":
                temp_combination = random.choice(template_combinations[:8])
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        valid_temps = temp[leg.index("Body, increase (general)")] + temp[leg.index("Body, increase (general, tests)")] 
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, increase (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Tests_Yesterday(data, idx) == 'increase':
                            valid_temps = temp[leg.index("Body, increase (general comparison)")] + temp[leg.index("Body, increase (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, increase (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Tests_Yesterday(data, idx) == 'increase':
                        template = random.choice(temp[leg.index("Body, increase (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (tests, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+total)")])
                        templates_combined.append(template)
                    elif 'total' == t:
                        template = random.choice(temp[leg.index("Body, general (total)")])
                        templates_combined.append(template)
                possible_tests.append([templates_combined, 0.5, 'increase'])
                                    
            if Ruleset.Tests_Yesterday(data, idx) == "decrease" or Ruleset.Tests_Week(data, idx) == "decrease":
                temp_combination = random.choice(template_combinations[:8])
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        valid_temps = temp[leg.index("Body, decrease (general)")] + temp[leg.index("Body, decrease (general, tests)")] 
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, decrease (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Tests_Yesterday(data, idx) == 'decrease':
                            valid_temps = temp[leg.index("Body, decrease (general comparison)")] + temp[leg.index("Body, decrease (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, decrease (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Tests_Yesterday(data, idx) == 'decrease':
                        template = random.choice(temp[leg.index("Body, decrease (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (tests, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+total)")])
                        templates_combined.append(template)
                    elif 'total' == t:
                        template = random.choice(temp[leg.index("Body, general (total)")])
                        templates_combined.append(template)
                possible_tests.append([templates_combined, 0.5, 'decrease'])
            
            if Ruleset.Tests_Yesterday(data, idx) == "constant" or Ruleset.Tests_Week(data, idx) == "constant":
                temp_combination = random.choice(template_combinations_constants[:4])
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, constants (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers)")])
                        templates_combined.append(template)
                    elif 'num_previous' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers previous sentence)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (tests, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+total)")])
                        templates_combined.append(template)
                    elif 'total' == t:
                        template = random.choice(temp[leg.index("Body, general (total)")])
                        templates_combined.append(template)      
                possible_tests.append([templates_combined, 0.3, 'constant'])
            
            tests = [i for i, j in enumerate(possible_tests)]
            weights = [i[1] for i in possible_tests]
            tests_normalized = [i/sum(weights) for i in weights]
            sentences = np.random.choice(tests, p = tests_normalized)
            tests_and_type = [possible_tests[tests.index(sentences)][0], possible_tests[tests.index(sentences)][2]]
            text.append(tests_and_type)

    
        if s == 'Infections' and Ruleset.Infections_Yesterday(data, idx) != "error":
            if Ruleset.Infections_Yesterday(data, idx) == "increase" or Ruleset.Infections_Week(data, idx) == "increase":
                temp_combination = random.choice(template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, increase (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, increase (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Infections_Yesterday(data, idx) == 'increase':
                            valid_temps = temp[leg.index("Body, increase (general comparison)")] + temp[leg.index("Body, increase (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, increase (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Infections_Yesterday(data, idx) == 'increase':
                        template = random.choice(temp[leg.index("Body, increase (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (infections, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+total)")])
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (infections, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                chance = random.random()
                if chance > 0.3:
                    valid_temps = temp[leg.index("Body, peaks (general)")] + temp[leg.index("Body, peaks (only max)")]
                    template = random.choice(valid_temps)
                    templates_combined.append(template)
                possible_infections.append([templates_combined, 0.5, 'increase'])
                                    
            if Ruleset.Infections_Yesterday(data, idx) == "decrease" or Ruleset.Infections_Week(data, idx) == "decrease":
                temp_combination = random.choice(template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, decrease (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, decrease (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Infections_Yesterday(data, idx) == 'decrease':
                            valid_temps = temp[leg.index("Body, decrease (general comparison)")] + temp[leg.index("Body, decrease (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, decrease (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Infections_Yesterday(data, idx) == 'decrease':
                        template = random.choice(temp[leg.index("Body, decrease (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (infections, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+total)")])
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (infections, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                chance = random.random()
                if chance > 0.3:
                    template = random.choice(temp[leg.index("Body, peaks (general)")])
                    templates_combined.append(template)
                possible_infections.append([templates_combined, 0.5, 'decrease'])
            
            if Ruleset.Infections_Yesterday(data, idx) == "constant" or Ruleset.Infections_Week(data, idx) == "constant":
                temp_combination = random.choice(template_combinations_constants)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, constants (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers)")])
                        templates_combined.append(template)
                    elif 'num_previous' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers previous sentence)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (infections, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+total)")])
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (infections, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                possible_infections.append([templates_combined, 0.3, 'constant'])
            
            infections = [i for i, j in enumerate(possible_infections)]
            weights = [i[1] for i in possible_infections]
            infections_normalized = [i/sum(weights) for i in weights]
            sentences = np.random.choice(infections, p = infections_normalized)
            infections_and_type = [possible_infections[infections.index(sentences)][0], possible_infections[infections.index(sentences)][2]]
            text.append(infections_and_type)
                

        if s == 'Admissions' and Ruleset.Admissions_Yesterday(data, idx) != "error":
            if Ruleset.Admissions_Yesterday(data, idx) == "increase" or Ruleset.Admissions_Week(data, idx) == "increase":
                temp_combination = random.choice(template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        valid_temps = temp[leg.index("Body, increase (general)")] + temp[leg.index("Body, increase (general, admissions)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, increase (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Admissions_Yesterday(data, idx) == 'increase':
                            valid_temps = temp[leg.index("Body, increase (general comparison)")] + temp[leg.index("Body, increase (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, increase (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Admissions_Yesterday(data, idx) == 'increase':
                        template = random.choice(temp[leg.index("Body, increase (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (admissions, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (admissions, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (admissions, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                chance = random.random()
                if chance > 0.3:
                    valid_temps = temp[leg.index("Body, peaks (general)")] + temp[leg.index("Body, peaks (only max)")]
                    template = random.choice(valid_temps)
                    templates_combined.append(template)
                possible_admissions.append([templates_combined, 0.5, 'increase'])
                                    
            if Ruleset.Admissions_Yesterday(data, idx) == "decrease" or Ruleset.Admissions_Week(data, idx) == "decrease":
                temp_combination = random.choice(template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        valid_temps = temp[leg.index("Body, decrease (general)")] + temp[leg.index("Body, decrease (general, admissions)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, decrease (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Admissions_Yesterday(data, idx) == 'decrease':
                            valid_temps = temp[leg.index("Body, decrease (general comparison)")] + temp[leg.index("Body, decrease (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, decrease (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Admissions_Yesterday(data, idx) == 'decrease':
                        template = random.choice(temp[leg.index("Body, decrease (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (admissions, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (admissions, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (admissions, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                chance = random.random()
                if chance > 0.3:
                    template = random.choice(temp[leg.index("Body, peaks (general)")])
                    templates_combined.append(template)
                possible_admissions.append([templates_combined, 0.5, 'decrease'])
            
            if Ruleset.Admissions_Yesterday(data, idx) == "constant" or Ruleset.Admissions_Week(data, idx) == "constant":
                temp_combination = random.choice(template_combinations_constants)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, constants (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        valid_temps = temp[leg.index("Body, constants (numbers)")] + temp[leg.index("Body, constants (admissions)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'num_previous' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers previous sentence)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (admissions, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (admissions, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (admissions, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                possible_admissions.append([templates_combined, 0.3, 'constant'])
            
            admissions = [i for i, j in enumerate(possible_admissions)]
            weights = [i[1] for i in possible_admissions]
            admissions_normalized = [i/sum(weights) for i in weights]
            sentences = np.random.choice(admissions, p = admissions_normalized)
            admissions_and_type = [possible_admissions[admissions.index(sentences)][0], possible_admissions[admissions.index(sentences)][2]]
            text.append(admissions_and_type)
                
            
        if s == 'Clinique' and Ruleset.Clinique_Yesterday(data, idx) != "error":
            if Ruleset.Clinique_Yesterday(data, idx) == "increase" or Ruleset.Clinique_Week(data, idx) == "increase":
                new_template_combinations = template_combinations[2:4]+template_combinations[5:7]
                new_template_combinations.append(list(template_combinations[12]))
                new_template_combinations.append(list(template_combinations[15]))
                new_template_combinations.append(list(template_combinations[8]))
                #print(new_template_combinations)
                temp_combination = random.choice(new_template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        valid_temps = temp[leg.index("Body, increase (general)")] + temp[leg.index("Body, increase (general, admissions)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, increase (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Clinique_Yesterday(data, idx) == 'increase':
                            valid_temps = temp[leg.index("Body, increase (general comparison)")] + temp[leg.index("Body, increase (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, increase (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Clinique_Yesterday(data, idx) == 'increase':
                        template = random.choice(temp[leg.index("Body, increase (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (admissions, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (admissions, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (admissions, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                possible_clinique.append([templates_combined, 0.5, 'increase'])
                                    
            if Ruleset.Clinique_Yesterday(data, idx) == "decrease" or Ruleset.Clinique_Week(data, idx) == "decrease":
                new_template_combinations = template_combinations[2:4]+template_combinations[5:7]
                new_template_combinations.append(list(template_combinations[12]))
                new_template_combinations.append(list(template_combinations[15]))
                new_template_combinations.append(list(template_combinations[8]))
                temp_combination = random.choice(new_template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        valid_temps = temp[leg.index("Body, decrease (general)")] + temp[leg.index("Body, decrease (general, admissions)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, decrease (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Clinique_Yesterday(data, idx) == 'decrease':
                            valid_temps = temp[leg.index("Body, decrease (general comparison)")] + temp[leg.index("Body, decrease (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, decrease (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Clinique_Yesterday(data, idx) == 'decrease':
                        template = random.choice(temp[leg.index("Body, decrease (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (admissions, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (admissions, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (admissions, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                possible_clinique.append([templates_combined, 0.5, 'decrease'])
            
            if Ruleset.Clinique_Yesterday(data, idx) == "constant" or Ruleset.Clinique_Week(data, idx) == "constant":
                new_combinations_constants = template_combinations_constants[3:]
                new_combinations_constants.append(list(template_combinations_constants[1]))
                temp_combination = random.choice(new_combinations_constants)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, constants (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        valid_temps = temp[leg.index("Body, constants (numbers)")] + temp[leg.index("Body, constants (admissions)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'num_previous' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers previous sentence)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (admissions, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (admissions, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (admissions, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                possible_clinique.append([templates_combined, 0.3, 'constant'])
            
            clinique = [i for i, j in enumerate(possible_clinique)]
            weights = [i[1] for i in possible_clinique]
            clinique_normalized = [i/sum(weights) for i in weights]
            sentences = np.random.choice(clinique, p = clinique_normalized)  
            clinique_and_type = [possible_clinique[clinique.index(sentences)][0], possible_clinique[clinique.index(sentences)][2]]
            text.append(clinique_and_type)
                

        if s == 'IC' and Ruleset.IC_Yesterday(data, idx) != "error":
            if Ruleset.IC_Yesterday(data, idx) == "increase" or Ruleset.IC_Week(data, idx) == "increase":
                new_template_combinations = template_combinations[2:4]+template_combinations[5:7]
                new_template_combinations.append(list(template_combinations[12]))
                new_template_combinations.append(list(template_combinations[15]))
                new_template_combinations.append(list(template_combinations[8]))
                temp_combination = random.choice(new_template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        valid_temps = temp[leg.index("Body, increase (general)")] + temp[leg.index("Body, increase (general, admissions)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, increase (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.IC_Yesterday(data, idx) == 'increase':
                            valid_temps = temp[leg.index("Body, increase (general comparison)")] + temp[leg.index("Body, increase (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, increase (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.IC_Yesterday(data, idx) == 'increase':
                        template = random.choice(temp[leg.index("Body, increase (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (admissions, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (admissions, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (admissions, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                possible_ic.append([templates_combined, 0.5, 'increase'])
                                    
            if Ruleset.IC_Yesterday(data, idx) == "decrease" or Ruleset.IC_Week(data, idx) == "decrease":
                new_template_combinations = template_combinations[2:4]+template_combinations[5:7]
                new_template_combinations.append(list(template_combinations[12]))
                new_template_combinations.append(list(template_combinations[15]))
                new_template_combinations.append(list(template_combinations[8]))
                temp_combination = random.choice(new_template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        valid_temps = temp[leg.index("Body, decrease (general)")] + temp[leg.index("Body, decrease (general, admissions)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, decrease (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.IC_Yesterday(data, idx) == 'decrease':
                            valid_temps = temp[leg.index("Body, decrease (general comparison)")] + temp[leg.index("Body, decrease (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, decrease (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.IC_Yesterday(data, idx) == 'decrease':
                        template = random.choice(temp[leg.index("Body, decrease (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (admissions, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (admissions, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (admissions, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                possible_ic.append([templates_combined, 0.5, 'decrease'])
            
            if Ruleset.IC_Yesterday(data, idx) == "constant" or Ruleset.IC_Week(data, idx) == "constant":
                new_combinations_constants = template_combinations_constants[3:]
                new_combinations_constants.append(list(template_combinations_constants[1]))
                temp_combination = random.choice(new_combinations_constants)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, constants (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        valid_temps = temp[leg.index("Body, constants (numbers)")] + temp[leg.index("Body, constants (admissions)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'num_previous' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers previous sentence)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (admissions, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (admissions, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (admissions, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                possible_ic.append([templates_combined, 0.3, 'constant'])
            
            ic = [i for i, j in enumerate(possible_ic)]
            weights = [i[1] for i in possible_ic]
            ic_normalized = [i/sum(weights) for i in weights]
            sentences = np.random.choice(ic, p = ic_normalized)    
            ic_and_type = [possible_ic[ic.index(sentences)][0], possible_ic[ic.index(sentences)][2]]
            text.append(ic_and_type)
                
            
        if s == 'Deaths' and Ruleset.Deaths_Yesterday(data, idx) != "error":
            if Ruleset.Deaths_Yesterday(data, idx) == "increase" or Ruleset.Deaths_Week(data, idx) == "increase":
                temp_combination = random.choice(template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        valid_temps = temp[leg.index("Body, increase (general)")] + temp[leg.index("Body, increase (general, deaths)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, increase (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Deaths_Yesterday(data, idx) == 'increase':
                            valid_temps = temp[leg.index("Body, increase (general comparison)")] + temp[leg.index("Body, increase (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, increase (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Deaths_Yesterday(data, idx) == 'increase':
                        template = random.choice(temp[leg.index("Body, increase (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (deaths, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (deaths, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (deaths, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                chance = random.random()
                if chance > 0.3:
                    valid_temps = temp[leg.index("Body, peaks (general)")] + temp[leg.index("Body, peaks (only max)")] + temp[leg.index("Body, peaks (deaths)")]
                    template = random.choice(valid_temps)
                    templates_combined.append(template)
                possible_deaths.append([templates_combined, 0.5, 'increase'])
                                    
            if Ruleset.Deaths_Yesterday(data, idx) == "decrease" or Ruleset.Deaths_Week(data, idx) == "decrease":
                temp_combination = random.choice(template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        valid_temps = temp[leg.index("Body, decrease (general)")] + temp[leg.index("Body, decrease (general, deaths)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, decrease (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Deaths_Yesterday(data, idx) == 'decrease':
                            valid_temps = temp[leg.index("Body, decrease (general comparison)")] + temp[leg.index("Body, decrease (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, decrease (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Deaths_Yesterday(data, idx) == 'decrease':
                        template = random.choice(temp[leg.index("Body, decrease (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (deaths, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (deaths, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (deaths, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                chance = random.random()
                if chance > 0.3:
                    valid_temps = temp[leg.index("Body, peaks (general)")] + temp[leg.index("Body, peaks (deaths)")]
                    template = random.choice(valid_temps)
                    templates_combined.append(template)
                possible_deaths.append([templates_combined, 0.5, 'decrease'])
            
            if Ruleset.Deaths_Yesterday(data, idx) == "constant" or Ruleset.Deaths_Week(data, idx) == "constant":
                temp_combination = random.choice(template_combinations_constants)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, constants (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers)")])
                        templates_combined.append(template)
                    elif 'num_previous' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers previous sentence)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (deaths, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers+total)")] + temp[leg.index("Body, general (deaths, numbers+total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total' == t:
                        valid_temps = temp[leg.index("Body, general (total)")] + temp[leg.index("Body, general (deaths, total)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                possible_deaths.append([templates_combined, 0.3, 'constant'])
            
            deaths = [i for i, j in enumerate(possible_deaths)]
            weights = [i[1] for i in possible_deaths]
            deaths_normalized = [i/sum(weights) for i in weights]
            sentences = np.random.choice(deaths, p = deaths_normalized)    
            deaths_and_type = [possible_deaths[deaths.index(sentences)][0], possible_deaths[deaths.index(sentences)][2]]            
            text.append(deaths_and_type)
                
                        
        if s == 'Vaccines' and Ruleset.Vaccines_Yesterday(data, idx) != "error":
            if Ruleset.Vaccines_Yesterday(data, idx) == "increase" or Ruleset.Vaccines_Week(data, idx) == "increase":
                temp_combination = random.choice(template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, increase (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, increase (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Vaccines_Yesterday(data, idx) == 'increase':
                            valid_temps = temp[leg.index("Body, increase (general comparison)")] + temp[leg.index("Body, increase (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, increase (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Vaccines_Yesterday(data, idx) == 'increase':
                        template = random.choice(temp[leg.index("Body, increase (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (vaccines, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+total)")])
                        templates_combined.append(template)
                    elif 'total' == t:
                        template = random.choice(temp[leg.index("Body, general (total)")])
                        templates_combined.append(template)
                possible_vaccines.append([templates_combined, 0.5, 'increase'])
                                    
            if Ruleset.Vaccines_Yesterday(data, idx) == "decrease" or Ruleset.Vaccines_Week(data, idx) == "decrease":
                temp_combination = random.choice(template_combinations)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, decrease (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, decrease (numbers)")])
                        templates_combined.append(template)
                    elif 'comparison' == t:
                        if Ruleset.Vaccines_Yesterday(data, idx) == 'decrease':
                            valid_temps = temp[leg.index("Body, decrease (general comparison)")] + temp[leg.index("Body, decrease (comparison yesterday)")]                   
                            template = random.choice(valid_temps)
                            templates_combined.append(template)
                        else:      
                            template = random.choice(temp[leg.index("Body, decrease (general comparison)")])
                            templates_combined.append(template)
                    elif 'num_comparison' == t and Ruleset.Vaccines_Yesterday(data, idx) == 'decrease':
                        template = random.choice(temp[leg.index("Body, decrease (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (vaccines, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'gen_num_comparison' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+general comparison)")])
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+total)")])
                        templates_combined.append(template)
                    elif 'total' == t:
                        template = random.choice(temp[leg.index("Body, general (total)")])
                        templates_combined.append(template)
                possible_vaccines.append([templates_combined, 0.5, 'decrease'])
            
            if Ruleset.Vaccines_Yesterday(data, idx) == "constant" or Ruleset.Vaccines_Week(data, idx) == "constant":
                temp_combination = random.choice(template_combinations_constants)
                templates_combined = []
                for t in temp_combination:
                    if 'gen_sentence' == t:
                        template = random.choice(temp[leg.index("Body, constants (general)")])
                        templates_combined.append(template)
                    elif 'numbers' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers)")])
                        templates_combined.append(template)
                    elif 'num_previous' == t:
                        template = random.choice(temp[leg.index("Body, constants (numbers previous sentence)")])
                        templates_combined.append(template)
                    elif 'gen_numbers' == t:
                        valid_temps = temp[leg.index("Body, general (numbers)")] + temp[leg.index("Body, general (vaccines, numbers)")]
                        template = random.choice(valid_temps)
                        templates_combined.append(template)
                    elif 'total_numbers' == t:
                        template = random.choice(temp[leg.index("Body, general (numbers+total)")])
                        templates_combined.append(template)
                    elif 'total' == t:
                        template = random.choice(temp[leg.index("Body, general (total)")])
                        templates_combined.append(template)
                possible_vaccines.append([templates_combined, 0.3, 'constant'])
            
            vaccines = [i for i, j in enumerate(possible_vaccines)]
            weights = [i[1] for i in possible_vaccines]
            vaccines_normalized = [i/sum(weights) for i in weights]
            sentences = np.random.choice(vaccines, p = vaccines_normalized)        
            vaccines_and_type = [possible_vaccines[vaccines.index(sentences)][0], possible_vaccines[vaccines.index(sentences)][2]]            
            text.append(vaccines_and_type)
         

    return text
                        
            
                        
            
                            
            
            
            
                                   
                        
            
                            
            
            
            
                       
            
            
            
            
            
            
            
            
            