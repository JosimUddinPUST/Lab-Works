% Define facts for diseases and symptoms
disease(cold).
disease(flu).
disease(covid_19).

symptom(cold, cough).
symptom(cold, sore_throat).
symptom(cold, no_fever).

symptom(flu, fever).
symptom(flu, cough).
symptom(flu, body_aches).
symptom(flu, fatigue).

symptom(covid_19, fever).
symptom(covid_19, cough).
symptom(covid_19, fatigue).
symptom(covid_19, shortness_of_breath).

% Define rules to diagnose based on symptoms
has_disease(Disease) :-
    disease(Disease),
    symptom(Disease, Symptom1),
    symptom(Disease, Symptom2),
    symptom(Disease, Symptom3),
    symptom(Symptom1),
    symptom(Symptom2),
    symptom(Symptom3).

% Example of user-defined symptoms to test
symptom(fever).
symptom(cough).
symptom(fatigue).

% Example Queries:
% ?- has_disease(Disease).
% This should match symptoms to diagnose 'Disease' if all required symptoms are inputted.
