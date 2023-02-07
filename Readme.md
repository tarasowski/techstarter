# Was sind Git Diffs 🛠️

## git diff

- Git Diffs sind eine der wichtigsten Funktionen von Git und ermöglichen es Ihnen, **Änderungen** an Ihrem Code zu sehen. 

- Mit Git Diffs können Sie sehen, **was** in Ihren Dateien geändert wurde, seit Sie sie zuletzt gepusht oder gezogen haben.

- Um Git Diffs zu verwenden, können Sie den Befehl `git diff` auf der Kommandozeile ausführen. 

- Sie können Git Diffs auch für einen bestimmten **Branch** oder für einen bestimmten Zeitpunkt verwenden. 

```sh
git diff #shows the changes in your working tree relative to the last commit, only for tracked files

git diff HEAD #shows the changes in your working tree relative to the last commit (includes files that are not tracked)

git diff --staged #(or its synonym git diff --cached) shows the changes you staged for the next commit relative to the last commit
```

## git diff-highlight

- Dies ist ein Skript, das die Lesbarkeit von Git Diffs verbessert, indem es die Änderungen in Farbe hervorhebt. 

- Dies kann sehr hilfreich sein, wenn Sie Änderungen **schnell** erkennen möchten, ohne den gesamten Diff-Text durchzusehen.

- Es ist jedoch wichtig zu beachten, dass Git Diffs für binäre Daten nicht so nützlich sind wie für Textdateien, da die Änderungen nicht als Text angezeigt werden können.

```sh
git diff-highlight
```
![https://miro.medium.com/v2/resize:fit:4800/format:webp/1*Kk0Bl4JTj5ByTDwOaciaHw.png]

![https://miro.medium.com/v2/resize:fit:4800/format:webp/1*h8zPouTxZDyvIbRyjTMFqg.png]

Source: [https://maximsmol.medium.com/improving-git-diffs-4519a6541cd1](git
                                                                        highlight)

## binary data 
- Wenn Sie mit binären Daten arbeiten, kann es schwierig sein, Git Diffs zu verwenden. (Git ist jedoch darauf ausgelegt, mit binären Daten umzugehen, und Sie können Git Diffs auch für binäre Daten verwenden.)




