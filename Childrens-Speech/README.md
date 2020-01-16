# Children's Speech 

The Children's Story Speech Corpus is a collection of transcripts of children's speech. They are based on audio recordings from 2019. The children are native Tibetan speakers from Dharamsala, India, ages 4 to 7. Most of these stories are ones that they told unprompted; a few of the transcripts were prompted by pictures. 

The folders here contain: 

(A) Original-Transcripts (for documentation) -- SRT format timing files from the SayMore sessions. These contain time codes to the original WAVs, and inline codes for speech words (Tibetan brackets, ex. ༼ཨ་ནས་༽, a connective); "ungrammatical" words (again, Tibetan brackets, ex. ༼གི་༽ after a vowel); pronunciation-based spellings (regular brackets, ex. (ར) for how "རེད་བ" is pronounced by some speakers); and loanwords (square brackets, ex. [ཐ་ལིང་], Hindi "thali", "dishes"). 

(B) Spaced (for reading ease / analysis) -- TXT format versions of the transcripts, cleaned of time codes and punctuation. Word-spacing follows the rule of thumb that "a word" consists of the smallest unit of phonemes that can be uttered in isolation, yet still retain practical meaning. Practically speaking, that means the "spaced" version considers affixes like the འབྲེལ་སྒྲ་ as morphemic (as evidenced by a lack of practical meaning in isolation, and the fact that even traditional spelling rules show morphemic variation based on pronunciation, ex. "ངའི", "mine", "ཁོང་གི", "his", and "བྱེད་གི", "doing"), as well as the negative "མ་" or "མི་" (ex. "མི་འདུག", "[it] isn't", is one word, versus "མི འདུག", "[there] are people", is two). 

The current Spaced version does not retain the bracket-coding for speech, pronunciation, and loanwords; these are currently being organized. (It was necessary, from a practical standpoint, to remove them, as brackets did not consistantly surround "one word", but often contained syllable / morphemic word-bits, or multiple words). This repo will be updated with a word list to allow users to identify them, and tags may also be re-inserted later. 

(C) Spaced-Normalized (for analysis) -- A rough, automated version that has been partially normalized is also uploaded. In this version, affixes have been separated out to allow for a partial lemmatization. For example, the word "ཡོད་རེད་ད" is the lexicalized compound verb "ཡོད་རེད" with an emphasis / hedge marker of "ད"; this is given in the normalized format: "ཡོད་རེད_ -ད་", allowing "ཡོད་རེད" to be counted with other forms of that verb, and the emphasis "ད་" to be marked as distinct from the word "ད", "now". Again, this is partial normalization, because of course, there is also the pronunciation-based spelling variation of "དང", "and", as "ད". A version that was both fully normalized, and also conatained POS (Part of Speech) tags would be necessary to account for these sorts of ambiguities... Until then, we recommend using both or either of the Spaced and Normalized corpus versions, depending on the researchers goals and needs. 

We hope to update this repo soon with both the Speech Words list and some Frequency Lists for graded reading applications. 