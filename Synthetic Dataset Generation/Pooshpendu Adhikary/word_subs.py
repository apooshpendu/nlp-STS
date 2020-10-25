import os
import nlpaug.augmenter.word as naw
from nlpaug.util import Action

os.environ["MODEL_DIR"] = '../model'
model_dir = os.environ.get("MODEL_DIR");

aug = naw.AntonymAug()
_text = 'The quick brown fox jumps over the lazy dog'
augmented_text = aug.augment(_text)
print("Original:")
print(_text)
print("Antonym Text:")
print(augmented_text)

aug = naw.SynonymAug(aug_src='wordnet')
text = 'The quick brown fox jumps over the lazy dog.'
augmented_text = aug.augment(text)
print("Original:")
print(text)
print("Synonym Text:")
print(augmented_text)

aug = naw.ContextualWordEmbsAug(
    model_path='bert-base-uncased', action="substitute")
text = 'The quick brown fox jumps over the lazy dog.'
augmented_text = aug.augment(text)
print("Original:")
print(text)
print("BeRT Embed Text:")
print(augmented_text)