Introduction à Python
======================

Pourquoi Apprendre Python ?
---------------------------

Python est un langage de programmation puissant et polyvalent, parfait pour une multitude d'applications telles que l'automatisation, le développement de jeux, et la création d'applications graphiques (GUI). Sa simplicité, sa compatibilité multi-plateforme, et sa capacité à permettre un développement rapide et efficace en font un choix privilégié pour les développeurs de tous niveaux.

Avantages de Python
-------------------

- **Simplicité d'utilisation** : Python se distingue par sa syntaxe claire et intuitive, facilitant l'apprentissage pour les débutants et les professionnels.
- **Disponibilité** : Accessible sur Windows, macOS et Linux, Python bénéficie d'une large portée d'utilisation.
- **Développement rapide** : Grâce à ses types de données de haut niveau et à sa vaste bibliothèque standard, Python permet un développement rapide et efficace.
- **Langage interprété** : L'absence de compilation préalable accélère le cycle de développement, permettant des tests et des itérations rapides.
- **Extensibilité** : Python permet l'intégration de modules C pour optimiser les performances lors d'opérations critiques.

Installation de Python
======================

Téléchargement de Python
-------------------------

Pour télécharger Python, suivez ces étapes :

1. Visitez le site officiel de Python : `https://www.python.org`.
2. Choisissez votre système d'exploitation (Windows, macOS ou Linux).
3. Téléchargez l'installateur correspondant.

Installation de Python
----------------------

Ouvrez l'installateur téléchargé et suivez les instructions à l'écran :

1. Assurez-vous de cocher l'option *Add Python to PATH* lors de l'installation.
2. Cliquez sur *Install Now* et suivez les instructions.

Vérification de l'installation
-------------------------------

Pour vérifier que Python est correctement installé :

1. Ouvrez la ligne de commande (Terminal sur macOS/Linux, Command Prompt sur Windows).
2. Tapez la commande suivante :

   .. code-block:: bash

       python --version

3. Si cela ne fonctionne pas, essayez :

   .. code-block:: bash

       python3 --version

Ajouter Python au PATH
-----------------------

Si Python n'est pas reconnu, vous devrez l'ajouter manuellement au PATH :

- **Sur Windows** :
  1. Appuyez sur `Win + R`, tapez `sysdm.cpl`, et appuyez sur `Entrée`.
  2. Dans l'onglet *Avancé*, cliquez sur *Variables d'environnement*.
  3. Dans la section *Variables système*, trouvez et sélectionnez la variable *Path*, puis cliquez sur *Modifier*.
  4. Cliquez sur *Nouveau* et ajoutez le chemin d'installation de Python (par exemple, `C:\\Users\\VotreNom\\AppData\\Local\\Programs\\Python\\Python39\\`).
  5. Cliquez sur *OK* pour fermer toutes les fenêtres.

- **Sur macOS/Linux** :
  1. Ouvrez le fichier de configuration de votre shell (par exemple, `.bashrc`, `.zshrc`).
  2. Ajoutez la ligne suivante :

     .. code-block:: bash

         export PATH="/usr/local/bin/python3:$PATH"

  3. Sauvegardez le fichier et rechargez la configuration du shell :

     .. code-block:: bash

         source ~/.bashrc  # ou source ~/.zshrc

Choix et Installation d'un IDE
===============================

Qu'est-ce qu'un IDE ?
---------------------

Un IDE (Environnement de Développement Intégré) est un logiciel qui fournit des outils complets pour le développement de logiciels, incluant un éditeur de code, un débogueur et des outils de gestion de projets.

Meilleurs IDE pour Python
--------------------------

- **Visual Studio Code (VS Code)** : Léger, extensible, et très populaire, avec de nombreuses extensions pour Python.
- **PyCharm** : Un IDE puissant spécialement conçu pour Python, offrant de nombreuses fonctionnalités avancées.
- **Jupyter Notebook** : Idéal pour les projets de data science et les tutoriels interactifs.

Installation de Visual Studio Code (VS Code)
----------------------------------------------

Pour installer Visual Studio Code :

1. Rendez-vous sur le site `https://code.visualstudio.com`.
2. Téléchargez l'installateur pour votre système d'exploitation.
3. Suivez les étapes d'installation.
4. Ouvrez VS Code et installez l'extension Python depuis le Marketplace.

Installation de PyCharm
------------------------

Pour installer PyCharm :

1. Rendez-vous sur le site `https://www.jetbrains.com/pycharm`.
2. Téléchargez l'installateur pour votre système d'exploitation.
3. Suivez les étapes d'installation.
4. Ouvrez PyCharm et configurez votre interpréteur Python.

Installation de Jupyter Notebook
--------------------------------

Pour installer Jupyter Notebook :

1. Installez Jupyter Notebook via Anaconda ou pip.
2. Ouvrez la ligne de commande et tapez :

   .. code-block:: bash

       pip install notebook

   ou téléchargez Anaconda depuis `https://www.anaconda.com`.
3. Lancez Jupyter Notebook en tapant :

   .. code-block:: bash

       jupyter notebook

Utilisation de l'Interpréteur Python
=====================================

Lancer l'Interpréteur
----------------------

### Sur Unix/Linux/MacOS

1. **Installation par défaut** :
   - L'interpréteur Python est généralement installé dans le répertoire `/usr/local/bin/`.
   - Pour vérifier si Python est installé, ouvrez votre terminal et tapez :

     .. code-block:: bash

         python3 --version

2. **Lancer l'interpréteur** :
   - Pour lancer l'interpréteur Python, tapez simplement :

     .. code-block:: bash

         python3

   - Vous verrez le prompt interactif de Python, qui ressemble à ceci :

     .. code-block::

         Python 3.13 (default, Apr 4 2023, 09:25:04)
         [GCC 10.2.0] on linux
         Type "help", "copyright", "credits" or "license" for more information.
         >>> 

### Sur Windows

1. **Installation par défaut** :
   - Si vous avez installé Python depuis le Microsoft Store, la commande `python3` sera disponible.
   - Vous pouvez également utiliser le lanceur `py.exe` si vous l'avez installé.

2. **Lancer l'interpréteur** :
   - Ouvrez l'invite de commandes (Command Prompt) en appuyant sur `Win + R`, tapez `cmd`, et appuyez sur `Entrée`.
   - Tapez la commande suivante pour vérifier si Python est installé :

     .. code-block:: bash

         python --version

   - Pour lancer l'interpréteur Python, tapez simplement :

     .. code-block:: bash

         python

   - Vous verrez alors le prompt interactif de Python :

     .. code-block::

         Python 3.13 (default, Apr 4 2023, 09:25:04)
         [GCC 10.2.0] on win32
         Type "help", "copyright", "credits" or "license" for more information.
         >>> 

Quitter l'Interpréteur
-----------------------

- **Sur Unix/Linux/MacOS** :
  - Tapez `Control-D` pour quitter l'interpréteur.

- **Sur Windows** :
  - Tapez `Control-Z` suivi de `Entrée` pour signaler la fin de l'entrée.
  - Vous pouvez également quitter l'interpréteur en tapant l'une des commandes suivantes :

    .. code-block:: python

        quit()
        exit()

Exemple de Session Interactive
-------------------------------

Voici un exemple de ce à quoi ressemble une session interactive avec l'interpréteur Python :

.. code-block::

    $ python3
    Python 3.13 (default, Apr 4 2023, 09:25:04)
    [GCC 10.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> the_world_is_flat = True
    >>> if the_world_is_flat:
    ...     print("Be careful not to fall off!")
    ...
    Be careful not to fall off!
    >>> quit()
    $

Édition de Ligne de Commande
-----------------------------

L'interpréteur Python prend en charge l'édition interactive, la substitution d'historique et la complétion de code sur les systèmes qui supportent la bibliothèque GNU Readline. Pour vérifier si l'édition de ligne de commande est supportée, tapez `Control-P` au premier prompt Python. Si cela émet un bip, l'édition de ligne de commande est activée.

Les fonctionnalités d'édition de ligne de commande incluent :
- **Édition interactive** : Navigation et modification du texte à l'aide des touches fléchées.
- **Substitution d'historique** : Accès aux commandes précédentes via les touches fléchées haut et bas.
- **Complétion de code** : Complétion des noms de variables et de fonctions en appuyant sur la touche `Tab`.

Pour plus de détails sur l'édition de ligne de commande, consultez l'annexe : `Interactive Input Editing and History Substitution <https://docs.python.org/3.13/tutorial/interactive.html#tut-interacting>`.

Modes de Fonctionnement
-----------------------

L'interpréteur Python peut être exécuté dans différents modes :

1. **Mode interactif** : Exécution de commandes une par une. C'est le mode que nous avons abordé.
2. **Mode script** : Exécution de fichiers Python (scripts). Tapez `python <nom_du_script.py>` pour exécuter le fichier.
3. **Mode aide** : Pour obtenir de l'aide sur les modules ou les fonctions, utilisez `python -m pydoc <nom_module>`.
