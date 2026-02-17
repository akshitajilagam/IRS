def generate_ngrams(word, n):
  word = "#" + word + '#'
  return set(word[i:i+n] for i in range(len(word)-n+1))

def correct_spelling(word, dictionary, n_val):
  scores = []

  for d in dictionary:
    g1 = generate_ngrams(word,n_val)
    g2 = generate_ngrams(d,n_val)
    score = len(g1 & g2) / len(g1 | g2)
    scores.append((score,d))
  best_score, best_word = max(scores)
  return best_word, best_score

dictionary = ['computer', 'science', 'engineering', 'information', 'technology', 'spelling', 'correction', 'program']

misspelled = 'tecanalogya'

# Assuming n_val should be 3 for trigrams as a common choice for this type of problem
n_gram_size = 3 
result, score = correct_spelling(misspelled, dictionary, n_gram_size)

print("Misspelled word: ", misspelled)
print("Suggestion correction:", result)
print("Similarity score:", round(score, 2))
