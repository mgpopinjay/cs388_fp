from gensim.models import KeyedVectors
from gensim.models import FastText
from gensim.models import Word2Vec

print("\nPreloading...")
model = KeyedVectors.load_word2vec_format('bio_embedding_extrinsic', binary=True)
# model = FastText.load_fasttext_format('bio_embedding_intrinsic.bin')
print("\nLoaded model...")
# model = fasttext.load_model('bio_embedding_intrinsic')

print("model", model)

model.save_word2vec_format('bio_embedding_extrinsic.200d.txt', binary=False)

print("model text saved...")
