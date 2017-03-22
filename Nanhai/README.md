# NanhaiCorpus

The Nanhai Corpus is a collection of word-segmented Tibetan totalling some 1.2 million words. 

The Nanhai Corpus Folder contains (A) 4 subfolders & (B) 4 simple Python scripts: 

(A) 
(A.1-4) CORPUS_TEXT -- contains the raw, word-segmented data in two encodings (UTF-8-SIG [for AntConc], & UTF-16 [also called "Unicode", for WordSmith]). 

The corpus itself contains 3 main sections: 

(A.1-4.i) Natural Speech -- Labeled "K-R-XXXX", where XXXX is a topic/genre category, of natural speech (full days were recorded with a clip-on mic). 

(A.1-4.ii) Scripted & Prompted Speech -- Labeled "K-L-XXXX", which are transcripts of dialogs created for educational purposes; and "K-J-XXXX", which are transcripts of prompted speech, usually on topics of monastic life. 
  -- All speech data was collected in the Himalaya Diaspora (India/Nepal). ("K-UN-XXXX" means the tracking system between the audio and transcript has been misplaced; we are working to resolve these missing data tags). 
  
(A.1-4.iii) Modern Writing -- Labeled "C-D-PD-..." or "C-D-DL-X-YYYY", where X is the dialect/region represented by the data source (being A-AMDO, K-KHAM, L-LHASA, or U-CENTRAL) and YYYY is the topic/genre of the excerpt. 

A 4th section is under construction, representing Middle Tibetan texts (commonly called "Classical" Tibetan -- Old Tibetan, Middle Tibetan, Modern Tibetan just as Old English, Middle English, Modern English) and "Old Church Tibetan" texts (canonical texts that are Old Tibetan in Middle Tibetan spellings -- a term from Roy Andrew Miller). This section will be labeled "C-T-...". 

(A.5) FREQ_LISTS -- some rudimentary frequency lists, by level. The best-made thus far is "GSL_LevelA1.txt", which is the 300 most frequent headwords from a balanced subsection of the full corpus, representing 50% speech, 50% writing. 

(B) -- some rudimentary Python scripts that were used for "cleaning" the data for headword analysis (a basic stemmer, a tsheg-stripper). These may also be applied to other word-segmented data you might have. POS (part of speech) and true Lemma tagging are under construction... 

(B.1) convert_UTF_encode.py -- takes a Unicode text (or set of files of various Unicode encodings) and normalizes them -- outputs folders of 3 versions of the input, in the 3 most useful encodings (UTF-8, UTF-8-SIG, UTF-16). 

(B.2) stemmer.py -- strips words of their case-endings, normalizes particles / prepositions (techinically postpositions) to one form, and puts the most frequent verbs into a common stem. *VERY* rudimentary. Only useful for about the first 1,000-2,000 most-frequent words... 

(B.3) TshegRegex.py -- the TshegRegex uses regular expressions (regex) to strip corpus files of their final tshegs (so corpus analysis tools don't see token instances like ཡིན་ & ཡིན། as different words, for example). It also normalizes spacing (all return carriages, tabs, half-spaces, etc., to a regular white space). The output is a perfectly evenly spaced text. 

(B.4) Vertical_File_Creator.py -- takes input and puts it into simple "Verticle File" format. Useful if you want to use simple SketchEngine procedures, like concordancing. This will become more useful once we have POS tags and a Lemmatizer, which will "unlock" the real useful, advanced features of SketchEngine. 

Enjoy! Send feedback to the repo developer: thedirk[AT]gmail.com 

INSTRUCTIONS for USING the CORPUS
------------------------------------
Instructions for using SketchEngine for analysis: 

Make an account at: https://www.sketchengine.co.uk/ 

The CORPUS_TEXT_VERTICAL_FILES are for sketchengine. Compress a pre-selected sub-section into zips and follow the instructions at SketchEngine. 

Instructions for using WordSmith for analysis: 

The CORPUS_TEXT_UTF16 files are for WordSmith. WordSmith can't analyze UTF8 or UTF8-SIG encodings. There are still some kinks to work out, and I'll be updating this repo with any strides we make in that area. A better, FREE option, for analyzing Tibetan corpora is AntConc... 

Instructions for using AntConc for analysis (our top choice): 

Download AntConc from http://www.laurenceanthony.net/software.html 

The CORPUS_TEXT_UTF8SIG files are for AntConc (utf-8 is the default encoding for AntConc, though it can be set to others). 

To make it useful for Tibetan, there's a few things you NEED to do: 

(1) enter "Global Settings". 

(2) Go to "Token Definition Setup" ('Token' here basically means 'character'--what characters will AntConc recognize?) 

(3) At the bottom, select "User-Defined Token Class" -- "Use Following Definition" 

(4) In the space available, copy & paste the following (the entire unicode set of Tibetan characters): 

ༀ༁༂༃༸༹ཀཁགགྷངཅཆཇ཈ཉཊཋཌཌྷཎཏཐདདྷནཔཕབབྷམཙཚཛཛྷཝཞཟའཡརལཤཥསཧཨཀྵཪཫཬ཭཮཯཰ཱཱཱིིུུྲྀཷླྀཹེཻོཽཾཿ྄ཱྀྀྂྃ྅ྌྍྎྏྐྑྒྒྷྔྕྖྗ྘ྙྚྛྜྜྷྞྟྠྡྡྷྣྤྥྦྦྷྨྩྪྫྫྷྭྮྯྰྱྲླྴྵྶྷྸྐྵྺྻྼ

(5) In "Append Definition", add the 'tsheg' (་)

(6) Be sure to check the boxes! And hit "apply"... 

OR... check all "Letter"/"Punctuation"/"Symbol"/&"Mark" classes; hit "Apply". 
