import random


def freq_builder(sentence, n, corpus):

    # INSERT LINE FOR N == 1

    input_token = sentence[-1 * (n - 1) :]  # tokens to look at from sentence

    input_token_ct = "".join(input_token)

    count_input = 0

    i = 0

    corpus_last_index = len(corpus)  # stop point

    freq_dict = {}

    # print(input_token, input_token_ct)

    for i in range(0, len(corpus)):

        if i + n > corpus_last_index:

            i += 1

        else:

            token_match = corpus[i : i + n]

            # print(token_match)

            concat_match = "".join(token_match)

            if concat_match.startswith(input_token_ct):

                # print(concat_match, token_match[-1])

                if token_match[-1] not in freq_dict:

                    freq_dict[(token_match[-1])] = 1

                    count_input += 1

                else:

                    freq_dict[(token_match[-1])] += 1

                    count_input += 1

            i += 1

    return freq_dict, count_input, input_token


def unigram_handler():

    chaos = "chaos"

    return chaos


# modify function for n = 1 at the end


def finish_sentence(sentence, n, corpus, deterministic=False):

    # Error Checking

    if len(sentence) < n or n == 0:

        return print("N needs to be less than or equal to length of sentence tokens")

    # elif n == 1:

    #     unigram_handler(sentence,n, corpus, deterministic) #PLACEHOLDER -------------- CODE ME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # corpus and sentence are processed according to n, ngram for the tokens of the sentence ngram

    final_sentence = [i for i in sentence]  # Initializing final sentence

    while len(final_sentence) != 10 or final_sentence[-1] not in "?!.":

        token_dict, count_ngram, ngram = freq_builder(final_sentence, n, corpus)

        new_n = n

        if count_ngram == 0:  # stupid backoff, if necessary

            while count_ngram == 0:

                token_dict, count_ngram, ngram = freq_builder(
                    final_sentence, new_n - 1, corpus
                )

        # resetting new_n, this way we can return to our original ngram model,
        # only implementing stupid backoff when needed

        # new_n = n
        print("my ngram: ", ngram)
        print("my final sentence", final_sentence)
        if deterministic == True:

            new_token = max(token_dict, key=token_dict.get)

            final_sentence.append(new_token)

        else:

            for key in token_dict:

                token_dict[key] /= count_ngram

            token_choices = list(token_dict.keys())

            token_probabilities = list(token_dict.values())

            print(final_sentence)

            print(token_choices, token_probabilities)

            new_token = random.choices(token_choices, token_probabilities)
            print(new_token)

            final_sentence.append(new_token)

    return final_sentence
