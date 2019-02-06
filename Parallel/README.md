# Parallel

A repo for parallel English/Tibetan corpora compiled by Esukhia

The folder "84000" is a work in progress. It contains all the English and Tibetan sub-sections of the Translated Words that have been done thus far. The have had some basic pre-processing (automatic alignment by sentence), but require more steps to be actually aligned in parallel. This README will be updated once that's completed... 

*UPATE* 

In 2018, 84000 and Esukhia collaborated to manually align the finished translations of the project. 

This repo was updated with the parallel corpus current as of 6 Feb 2019. 

Outdated README: 
------------------------------------
There are currently 2 files for "incomplete" parallel alignment and 4 files for "complete" parallel alignment. 

Incomplete alignment includes: 1) the Tibetan original, roughly aligned by "sentence"; 2) the English translation, roughly aligned by sentence. (With return carriages [new lines] being the unit defining lines in the plain text, UTF-8 documents). 

Complete alignment includes: 1) & 2) from above, aligned in parallel (equivalent return lines); 3) those parallel files were added to a spreadsheet format, saved here: https://docs.google.com/spreadsheets/d/1NLEluE81bj0JEXMVqBkNlGJUwqo_YIK7Eup8FKTurwI/edit?usp=sharing and downloaded as "tab-separated" .txt files; 4) which were then aligned into .tmx files using Olifant. 

In other words, completed documents include: 

1) A Tibetan original .txt and 2) an English translation .txt (aligned in parallel) 
3) that parallel alignment expressed as a single, tab-separated .txt 
4) that parallel alignment expressed as a single .tmx file

for Olifant, visit: 
http://okapi.sourceforge.net/downloads.html

for instructions, visit: https://www.pangeanic.com/diary-inhouse-translator/6-steps-to-create-tmx-file-from-excel-or-other-formats/ 

to use the TMX files, create an account at SmartCAT: https://smartcat.ai 

go to "Resources" > "Translation Memory" and "Create TM". upload the TMX files by following the instructions... 
