from markovchain import *
from training_algorithms import *

# Builds a formatted string from the generator
def write_tweets(screen_name):
    mkv = MarkovChain()
    mkv.load_training('stored_data\\%s\\training01.txt' % screen_name)
    tweet = ''.join([w for w in mkv.generate_formatted(word_wrap=130, soft_wrap=True, start_with=None, max_len=30,
                                                       verbose=True)])
    return tweet

def save_tweets(screen_name, number):
    mkv = MarkovChain()
    mkv.load_training('stored_data\\%s\\training01.txt' % screen_name)
    fname = 'output_text\\%s_predicted_tweets.txt' %screen_name

    with open(fname, 'w', encoding='utf-8') as f:
        for i in range(number):
            words = [w for w in mkv.generate_formatted(word_wrap=280, soft_wrap=True, start_with=None,
                                                               max_len=30, verbose=True)]
            word = words[0]
            tweet = ''.join([w for w in mkv.generate_formatted(word_wrap=280, soft_wrap=True, start_with=None,
                                                               max_len=30, verbose=True)])
            f.write('\n')
            f.write('Generated a tweet starting with %s' % word)
            f.write('\n')
            f.write(tweet)

    f.close()
    print('{0} tweets saved to {1}_predicted_tweets.txt'.format(number, screen_name))





def train_chain(screen_name):
    mkv = MarkovChain()
    mkv.bulk_train('training_data\\%s_tweets_text.txt' % screen_name, verbose=True)
    # Or,``
    # mkv.load_training('training01.txt')

    # Store this information for later, so that there's no need to re-train the next time.
    mkv.save_training('stored_data\\%s\\training.txt' % screen_name)
    # Adjust the weights with the help of some fitness functions.
    mkv.bulk_adjust_weights(fitness_functions=[aw_favor_alternating_complexity, aw_mul(aw_favor_punctuation, 0.5)],
                                iterations=1000000,
                                verbose=True)
    # Save the new state to a different file, to prevent feedback loops.
    mkv.save_training('stored_data\\%s\\training01.txt' % screen_name)

    print('weights saved')
