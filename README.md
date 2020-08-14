# Doc - Plateforme Kedge

## 0. Structure de l'outil

```
.   
│
└───generate_student_csv
│   │─  create_student_csv.py
│   └─  generate_test_csv.py
│
└───generate_steps_pdf
│   │─  create_form_pdf.py
│   │─  install_mactex.sh
│   │─  logo.png
│   │─  template.tex
│   │
│   └───steps_csv
│       │─  step1.csv
│       │─  step2.csv
│       └─  ...
```

- `generate_student_csv` : 
    - `create_student_csv.py` : permet de générer le fichier CSV qui sera chargé sur MemberStack. Il se base sur le CSV extrait du tableur fourni par l'ecole.
    - `generate_test_csv.py` : à utiliser dans un but de test seulement. Génère un CSV de X étudiants, semblable à celui qui sera généré par le tableur de l'école.
- `generate_steps_pdf` : 
    - `create_form_pdf.py` : permet de générer les PDFs compulsant les réponses des groupes aux différents formulaires de fin d'étape, sur base des CSVs fournis par TypeForm.
    - `install_mactex.sh` : script Bash permettant d'installer MacTeX, outil indispensable à la création d'un PDF (sur Mac).
    - `logo.png` : logo en en-tête des PDFs générés.
    - `template.tex` : format des documents PDFs.
    - `steps_csv` : dossier contenant 5 fichiers CSV de test.


## 1. CSV étudiants

### 1.1 Format de données

#### 1.1.1 Entrée

Le script `create_student_csv.py`, contenu dans le dossier `generate_student_csv`, prend en entrée un CSV au format suivant : 

```
nom1,prenom1,mail1,langue1
nom2,prenom2,mail2,langue2
```

#### 1.1.2 Sortie

Et fourni en sortie un autre CSV au format : 

```
Prénom,Nom,Email,Password,Numéro de groupe,Langue,Membres de Groupe,Mentor,
Membership ID
prenom1,nom1,password1,[1-999],langue1,membre1|membre2|membre3|...,[1-999],
membershipId
```

> **Note :** La 1ière ligne est l'en-tête.

> **Important :** Le mot de passe est une chaîne aléatoire de 6 caractères alphabétiques.

### 1.2 Utilisation

L'outil est utilisable sur un système Mac ou Linux. Pour l'exécuter, suivre les étapes suivantes : 

1. Ouvrir un Terminal
    - Sur Mac :apple: : Command + Espace et taper "Terminal", puis Enter.
    - Sur Ubuntu : Control + Alt + T
2. Dans le Terminal, naviguez jusqu'au dossier contenant le script `create_student_csv.py`, à l'aide de la commande `cd`.
> **Exemple :** `cd Documents/super_scripts/generate_student_csv/`

3. Repérez le chemin vers le fichier CSV initial, tout frais extrait du tableur.
> **Exemple :** **~/Documents/mon/dossier/mon_fichier.csv**

> **Note :** Le préfixe `~/` permet de trouver le dossier Documents depuis n'importe quel autre dossier.

> **Note :** Pour plus de simplicité, copiez le fichier `mon_fichier.csv` directement dans le dossier des scripts. Ainsi le chemin devient seulement **mon_fichier.csv**.

4. Tapez la commande suivante, en remplaçant `<mon_fichier>` par le chemin récupéré durant l'étape 3 : 
```
python create_student_csv.py <mon_fichier>
```

5. Une fois que le Terminal vous aura rendu la main, le fichier `processed_students.csv` a été créé. Vous le trouverez dans le dossier `generate_student_csv`, sous le nom `processed_students.csv`.

### 1.3 Tests

Pour tester le fonctionnement de l'outil sans posséder de fichier CSV fourni par l'école, il est possible d'en générer un via le script `generate_test_csv.py`.

Comme pour `create_student_csv.py`, placez vous dans le dossier contenant les scripts et lancez la commande suivante, en remplaçant <nombre_d_etudiants> par un entier en 5 et 36 000 : 
```
python generate_test_csv.py <nombre_d_etudiants>
```

## 2. PDFs des questionnaires

Le script `create_form_pdf.py`, contenu dans le dossier `generate_steps_pdf`, prend les 5 fichiers CSVs issus de TypeForm (un pour chaque questionnaire) et en extrait un fichier PDF récapitulatif des questions/réponses pour chaque groupe.

### 2.1 Utilisation

#### 2.1.1 Installer `pdflatex`

Afin de créer un PDF, l'outil a besoin d'avoir `pdflatex` d'installé sur l'ordinateur où il tourne.

- Sur Mac :apple: : Utiliser le script `install_mactex.sh` de la manière suivante, toujours dans le Terminal et depuis le dossier `generate_steps_pdf` : 
```
./install_mactex.sh
```
- Sur Ubuntu : Taper la commande suivante dans le Terminal : 
```
sudo apt-get install texlive
```

> **Important :** Gardez un oeil sur votre Terminal durant le processus d'installation, il est plus que probable que vous deviez taper votre mot de passe un ou plusieurs fois.

> **Note :** Rien n'apparaît lors de l'entrée du mot de passe, c'est normal.

#### 2.1.2 Lancer le script

Une fois `pdflatex` installé, suivez les étapes : 

1. Ouvrir un Terminal
    - Sur Mac :apple: : Command + Espace et taper "Terminal", puis Enter.
    - Sur Ubuntu : Control + Alt + T
2. Dans le Terminal, naviguez jusqu'au dossier contenant le script `create_form_pdf.py`, à l'aide de la commande `cd`.
> **Exemple :** `cd Documents/super_scripts/generate_steps_pdf/`

3. Repérez le chemin vers les fichiers CSVs, tout frais extraits de TypeForm.
> **Exemple :** **~/Documents/mon/dossier/etape1.csv**, **~/Documents/mon/dossier/etape2.csv**, ...

> **Note :** Le préfixe `~/` permet de trouver le dossier Documents depuis n'importe quel autre dossier.

> **Note :** Pour plus de simplicité, copiez les fichiers `etape[1-5].csv` directement dans le dossier `generate_steps_pdf`. Ainsi le chemin devient seulement **mon_fichier.csv**.

4. Tapez la commande suivante, en remplaçant `<fichier_etape[1-5]>` par les chemins récupérés durant l'étape 3 : 
```
python create_form_pdf.py <fichier_etape1> <fichier_etape2> <fichier_etape3> <fichier_etape4> <fichier_etape5>
```

5. Une fois que le Terminal vous aura rendu la main, vous trouverez dans le dossier `generate_steps_pdf` tous les fichiers PDFs des différents groupes, nommés de la manière suivante : `<nom_de_groupe>.pdf`

### 2.2 Personnalisation

#### 2.2.1 Format général du PDF
Le fichier `template.tex` peut être modifié pour coller à l'identité visuelle souhaitée. En ouvrant n'importe quel éditeur LateX en ligne (ex: **Overleaf**), il suffit de modifier la disposition, télécharger le fichier `.tex` et remplacer l'ancien `template.tex` par le nouveau.

Seuls deux champs sont nécessaires dans le fichier de template : 
- `<group_number>` : durant l'exécution du script, cette balise sera remplacée par le nom du groupe.
- `<text>` : durant l'exécution du script, cette balise sera remplacée par le long enchainement d'étapes, questions et réponses de la retranscription.

#### 2.2.2 Logo de l'en-tête

Le fichier `logo.png` peut être remplacé par tout autre `png` portant le même nom et sera affiché convenablement dans les différents PDFs générés.