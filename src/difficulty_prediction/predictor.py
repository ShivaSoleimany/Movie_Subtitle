from src.difficulty_prediction import MODEL_DIR
import src.difficulty_prediction.model_util as model_util
import src.difficulty_prediction.preprocess as preprocess
import keras


model = ''
def predictor(word):
    model_weights_path = 'src/difficulty_prediction/params/crepe_model_weights_with_test_v1.0.h5'

    # Maximum length. Longer gets chopped. Shorter gets padded.
    maxlen = 21
    # Filters for conv layers
    nb_filter = 32
    # Number of units in the dense layer
    dense_outputs = 256
    # Conv layer kernel size
    filter_kernels = [3, 3, 2, 2, 2, 2]
    # Number of units in the final output layer. Number of classes.
    cat_output = 3

    print('Creating vocab...')
    vocab, reverse_vocab, vocab_size, alphabet = preprocess.create_vocab_set()

    print('Build model...')
    model = model_util.create_model(filter_kernels, dense_outputs, maxlen, vocab_size,
                                nb_filter, cat_output)
    model.load_weights(model_weights_path)
    prediction = model.predict(preprocess.encode_data([word], maxlen, vocab))
    return prediction