Exo1:
Q1. D'après le message de hello-world, Docker réalise ces étapes :

Le client Docker contacte le démon Docker.
Le démon télécharge l'image hello-world depuis Docker Hub, car elle n'existe pas en local.
Le démon crée un conteneur à partir de cette image et exécute le programme qu'elle contient.
Le démon envoie la sortie du programme au client, qui l'affiche dans le terminal.

Q2. -i garde STDIN ouvert, ce qui permet de taper des commandes. -t alloue un pseudo-terminal, ce qui donne un affichage de terminal normal. On les utilise ensemble pour un shell interactif.

Q3. Un conteneur vit tant que son processus principal (PID 1) tourne. Ici c'est sh. Quand tu fais exit, le shell se termine, donc le conteneur s'arrête.

Q4. Oui, /fichier-test existe toujours. Le conteneur a été arrêté, pas supprimé. Sa couche inscriptible, qui contient le fichier, est conservée, et docker start la réutilise.

Q5. Non, le fichier n'existe plus. docker rm supprime le conteneur et sa couche inscriptible. Le nouveau docker run crée un conteneur neuf à partir de l'image alpine, qui n'a jamais été modifiée. On en conclut que les données d'un conteneur sont éphémères : elles disparaissent avec lui, et l'image reste immuable. D'où l'intérêt des volumes (exercice 2).

Q6. --rm supprime automatiquement le conteneur à sa sortie. Après exit, il n'apparaît donc pas dans docker ps -a, ce qui évite d'accumuler des conteneurs arrêtés.

Q7. L'adresse IP est celle que tu lis dans docker inspect (typiquement 172.17.0.2, sur le réseau bridge par défaut). Le mapping de ports est 80/tcp -> 0.0.0.0:8080 : le port 80 du conteneur est publié sur le port 8080 de l'hôte.

Q8. docker run crée un nouveau conteneur à partir d'une image et exécute une commande dedans. docker exec exécute une commande dans un conteneur déjà en cours d'exécution : il ne crée rien de nouveau (on s'en sert pour ouvrir un shell dans web, par exemple).

Q9. Non, la modification n'est pas conservée. Elle avait été écrite dans la couche inscriptible de l'ancien conteneur. En faisant docker rm, cette couche est supprimée. Le nouveau conteneur repart de l'image nginx, qui n'a pas changé. Les volumes (exercice 2) permettent de conserver ce type de modification.

Q10. Sans -it, le conteneur n'a pas d'entrée standard ouverte ni de terminal. Le programme attend une réponse au clavier (input()), ne reçoit rien (fin de fichier), et se termine, souvent avec une erreur. Dans docker ps -a, il apparaît avec le statut Exited. 

Q11. Une image est un modèle en lecture seule (le programme et ses dépendances empaquetés). Un conteneur est une instance en cours d'exécution (ou arrêtée) créée à partir d'une image, avec en plus une couche inscriptible. On peut créer plusieurs conteneurs à partir d'une même image, comme plusieurs objets à partir d'une même classe.