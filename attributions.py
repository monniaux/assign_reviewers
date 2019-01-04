import random
random.seed("Christelle")

nr_dossiers = 142
nr_examinateurs = 8
nr_examinateurs_par_dossier = 2

nr_dossiers_par_examinateur_base = (nr_dossiers*nr_examinateurs_par_dossier) / nr_examinateurs
examinateurs_avec_extra = (nr_dossiers*nr_examinateurs_par_dossier) % nr_examinateurs

nr_dossiers_pour_examinateurs = [((nr_dossiers_par_examinateur_base+1) if examinateur < examinateurs_avec_extra else nr_dossiers_par_examinateur_base) for examinateur in range(nr_examinateurs)]
while True:
    try:
        disponibilites = list(nr_dossiers_pour_examinateurs)
        choix=[]
        for dossier in range(nr_dossiers):
            examinateurs_disponibles = [i for i in range(nr_examinateurs) if disponibilites[i]>0]
            examinateurs = random.sample(examinateurs_disponibles, nr_examinateurs_par_dossier)
            for i in examinateurs:
                disponibilites[i] -= 1
            choix.append(examinateurs)
    except ValueError:
        pass
    else:
        break

print choix
