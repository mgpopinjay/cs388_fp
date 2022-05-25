# nlp-qa-outdomain-finetuning
Out-domain Question Answering (QA) on SQuAD with bi-directional LSTM

This project assessed the effect of applying out-domain(OD) and domain-specific word embeddings and OD fine-tuning to a [Question Answering(QA)](https://en.wikipedia.org/wiki/Question_answering) system.  

The experiment used [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/), based on general questions and answers generated from Wikipedia articles, as its baseline model, and a biomedical-focused QA dataset, [BioASQ](https://paperswithcode.com/dataset/bioasq), for OD QA evaluation. In building a model for OD QA, the performance contributions of non-domain specific ([GloVe](https://nlp.stanford.edu/projects/glove/)) and biomedical-focused (e.g. [BioReddit](https://github.com/basaldella/bioreddit), [BioWordVec](https://github.com/ncbi-nlp/BioWordVec), etc.) word embeddings are compared.  

The revised model, a SQuAD(BioReddit) baseline fine-tuned with OD BioASQ data, achieved a score gain of +7.22 F1 and +3.0 EM over the baseline model in OD performance on BioASQ data. Meanwhile, the OD fine-tuning of a SQuAD (GloVe) baseline led to a gain of +5.36 F1 and +.27 EM. Comparing both OD fine-tuning cases, the use of in-domain (ID) word embeddings led to less gain in the EM score compared to the use of OD word embeddings. 

These preliminary results show favorable evidence for OD fine-tuning as a technique for improving the F1 score in OD QA task, and mild evidence for OD word-embedding in improving the EM score. 

