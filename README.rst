##############################
put_stress_rus
##############################

Python package to convert a russian word to IPA transcription (International Phonetic Alphabet) powered by the trained neural network with 0.9996 accuracy

* Version 0.0.1
* Date: 2022, August, 27
* Developer: Eugene Proskulikov
* License: MIT
* Contact: `LinkedIn <https://www.linkedin.com/in/eugene-proskulikov-168050a4/>`_.
* Home: https://github.com/EugenefedorovPro/word2ipa_rus



-------------
Dependencies
-------------

* tensorflow==2.9.1
* numpy==1.23.1 


--------
Install
--------

:: 

    pip install git+https://github.com/EugenefedorovPro/word2ipa_rus.git
    

------------
Quick start
------------

::
    
    from word2ipa_rus.word2ipa import word2ipa
    
    word2ipa("молоко'")

Output::

> 'məlˠɐˈko'


input - russian word with a stressed mark "'" after the accented vowel 

output - transcription of the word in International Phonetic Alphabet (IPA)

-----------------------
Neuron Network training
-----------------------
`nn_training <https://github.com/EugenefedorovPro/word2ipa_rus/tree/main/nn_training>`_ directory contains files, requested for training neural network, which is used in `word2ipa_rus`:
 
* *stressed_word_2_ipa.ipynb* - preprocessing data, model compile, save, validate, predict. The file demands Jupyter editor (JupyterLab, VS Code with Jupyter extension, PyCharm Professional, etc.)
* *requirements.txt* - list of dependecies, including the two critical ones:
    * `ipapy <https://github.com/pettarin/ipapy>`_ is `my modifications <https://github.com/EugenefedorovPro/ipapy_eugene/tree/forpython310>`_ of the library for working with the Russin language within the framework of International Phonetic Alphabet (IPA)
    * `*wiktionary_rus* <https://github.com/EugenefedorovPro/wiktionary_rus>`_ is my Python package with Russian wiktionary preprocessed for neural networks
    
* *all_ipa_as_array_with_accents_short.pickle* - file containing preprocessed data for the model training

------------
NN accuracy
------------
Categorical accuracy of the `word2ipa_rus` is 0.9996. The model was trained on the basis of `specially parsed Russian wiktionary <https://github.com/EugenefedorovPro/wiktionary_rus>`_, encompassing 422821 word-stems and word-forms. Every written character or combination of characters exactly match sound(s) represented by IPA transcription. That is why the NN enjoys so high accuracy