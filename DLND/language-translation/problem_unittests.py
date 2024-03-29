import numpy as np
import tensorflow as tf
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
from tensorflow.python.layers.core import Dense
>>>>>>> bbae529... Original from Udacity
=======
>>>>>>> 307c83c... submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
import itertools
import collections
import helper


def _print_success_message():
    print('Tests Passed')


def test_text_to_ids(text_to_ids):
    test_source_text = 'new jersey is sometimes quiet during autumn , and it is snowy in april .\nthe united states is usually chilly during july , and it is usually freezing in november .\ncalifornia is usually quiet during march , and it is usually hot in june .\nthe united states is sometimes mild during june , and it is cold in september .'
    test_target_text = 'new jersey est parfois calme pendant l\' automne , et il est neigeux en avril .\nles états-unis est généralement froid en juillet , et il gèle habituellement en novembre .\ncalifornia est généralement calme en mars , et il est généralement chaud en juin .\nles états-unis est parfois légère en juin , et il fait froid en septembre .'

    test_source_text = test_source_text.lower()
    test_target_text = test_target_text.lower()

    source_vocab_to_int, source_int_to_vocab = helper.create_lookup_tables(test_source_text)
    target_vocab_to_int, target_int_to_vocab = helper.create_lookup_tables(test_target_text)

    test_source_id_seq, test_target_id_seq = text_to_ids(test_source_text, test_target_text, source_vocab_to_int, target_vocab_to_int)

    assert len(test_source_id_seq) == len(test_source_text.split('\n')),\
        'source_id_text has wrong length, it should be {}.'.format(len(test_source_text.split('\n')))
    assert len(test_target_id_seq) == len(test_target_text.split('\n')), \
        'target_id_text has wrong length, it should be {}.'.format(len(test_target_text.split('\n')))

    target_not_iter = [type(x) for x in test_source_id_seq if not isinstance(x, collections.Iterable)]
    assert not target_not_iter,\
        'Element in source_id_text is not iteratable.  Found type {}'.format(target_not_iter[0])
    target_not_iter = [type(x) for x in test_target_id_seq if not isinstance(x, collections.Iterable)]
    assert not target_not_iter, \
        'Element in target_id_text is not iteratable.  Found type {}'.format(target_not_iter[0])

    source_changed_length = [(words, word_ids)
                             for words, word_ids in zip(test_source_text.split('\n'), test_source_id_seq)
                             if len(words.split()) != len(word_ids)]
    assert not source_changed_length,\
        'Source text changed in size from {} word(s) to {} id(s): {}'.format(
            len(source_changed_length[0][0].split()), len(source_changed_length[0][1]), source_changed_length[0][1])

    target_missing_end = [word_ids for word_ids in test_target_id_seq if word_ids[-1] != target_vocab_to_int['<EOS>']]
    assert not target_missing_end,\
        'Missing <EOS> id at the end of {}'.format(target_missing_end[0])

    target_bad_size = [(words.split(), word_ids)
                       for words, word_ids in zip(test_target_text.split('\n'), test_target_id_seq)
                       if len(word_ids) != len(words.split()) + 1]
    assert not target_bad_size,\
        'Target text incorrect size.  {} should be length {}'.format(
            target_bad_size[0][1], len(target_bad_size[0][0]) + 1)

    source_bad_id = [(word, word_id)
                     for word, word_id in zip(
                        [word for sentence in test_source_text.split('\n') for word in sentence.split()],
                        itertools.chain.from_iterable(test_source_id_seq))
                     if source_vocab_to_int[word] != word_id]
    assert not source_bad_id,\
        'Source word incorrectly converted from {} to id {}.'.format(source_bad_id[0][0], source_bad_id[0][1])

    target_bad_id = [(word, word_id)
                     for word, word_id in zip(
                        [word for sentence in test_target_text.split('\n') for word in sentence.split()],
                        [word_id for word_ids in test_target_id_seq for word_id in word_ids[:-1]])
                     if target_vocab_to_int[word] != word_id]
    assert not target_bad_id,\
        'Target word incorrectly converted from {} to id {}.'.format(target_bad_id[0][0], target_bad_id[0][1])

    _print_success_message()


def test_model_inputs(model_inputs):
    with tf.Graph().as_default():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        input_data, targets, lr, keep_prob = model_inputs()
=======
        input_data, targets, lr, keep_prob, target_sequence_length, max_target_sequence_length, source_sequence_length = model_inputs()
>>>>>>> bbae529... Original from Udacity
=======
        input_data, targets, lr, keep_prob = model_inputs()
>>>>>>> 307c83c... submission_01
=======
        input_data, targets, lr, keep_prob = model_inputs()
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

        # Check type
        assert input_data.op.type == 'Placeholder',\
            'Input is not a Placeholder.'
        assert targets.op.type == 'Placeholder',\
            'Targets is not a Placeholder.'
        assert lr.op.type == 'Placeholder',\
            'Learning Rate is not a Placeholder.'
        assert keep_prob.op.type == 'Placeholder', \
            'Keep Probability is not a Placeholder.'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        assert target_sequence_length.op.type == 'Placeholder', \
            'Target Sequence Length is not a Placeholder.'
        assert max_target_sequence_length.op.type == 'Max', \
            'Max Target Sequence Length is not a Placeholder.'
        assert source_sequence_length.op.type == 'Placeholder', \
            'Source Sequence Length is not a Placeholder.'
>>>>>>> bbae529... Original from Udacity
=======
>>>>>>> 307c83c... submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

        # Check name
        assert input_data.name == 'input:0',\
            'Input has bad name.  Found name {}'.format(input_data.name)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        assert target_sequence_length.name == 'target_sequence_length:0',\
            'Target Sequence Length has bad name.  Found name {}'.format(target_sequence_length.name)
        assert source_sequence_length.name == 'source_sequence_length:0',\
            'Source Sequence Length has bad name.  Found name {}'.format(source_sequence_length.name)
>>>>>>> bbae529... Original from Udacity
=======
>>>>>>> 307c83c... submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
        assert keep_prob.name == 'keep_prob:0', \
            'Keep Probability has bad name.  Found name {}'.format(keep_prob.name)

        assert tf.assert_rank(input_data, 2, message='Input data has wrong rank')
        assert tf.assert_rank(targets, 2, message='Targets has wrong rank')
        assert tf.assert_rank(lr, 0, message='Learning Rate has wrong rank')
        assert tf.assert_rank(keep_prob, 0, message='Keep Probability has wrong rank')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        assert tf.assert_rank(target_sequence_length, 1, message='Target Sequence Length has wrong rank')
        assert tf.assert_rank(max_target_sequence_length, 0, message='Max Target Sequence Length has wrong rank')
        assert tf.assert_rank(source_sequence_length, 1, message='Source Sequence Lengthhas wrong rank')
>>>>>>> bbae529... Original from Udacity
=======
>>>>>>> 307c83c... submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

    _print_success_message()


def test_encoding_layer(encoding_layer):
    rnn_size = 512
    batch_size = 64
    num_layers = 3
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    with tf.Graph().as_default():
        rnn_inputs = tf.placeholder(tf.float32, [batch_size, 22, 1000])
        keep_prob = tf.placeholder(tf.float32)
        states = encoding_layer(rnn_inputs, rnn_size, num_layers, keep_prob)
=======
    source_sequence_len = 22
    source_vocab_size = 20
    encoding_embedding_size = 30
=======
>>>>>>> 307c83c... submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

    with tf.Graph().as_default():
        rnn_inputs = tf.placeholder(tf.float32, [batch_size, 22, 1000])
        keep_prob = tf.placeholder(tf.float32)
<<<<<<< HEAD
<<<<<<< HEAD

        enc_output, states = encoding_layer(rnn_inputs, rnn_size, num_layers, keep_prob,
                   source_sequence_length, source_vocab_size,
                   encoding_embedding_size)

>>>>>>> bbae529... Original from Udacity
=======
        states = encoding_layer(rnn_inputs, rnn_size, num_layers, keep_prob)
>>>>>>> 307c83c... submission_01
=======
        states = encoding_layer(rnn_inputs, rnn_size, num_layers, keep_prob)
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

        assert len(states) == num_layers,\
            'Found {} state(s). It should be {} states.'.format(len(states), num_layers)

        bad_types = [type(state) for state in states if not isinstance(state, tf.contrib.rnn.LSTMStateTuple)]
        assert not bad_types,\
            'Found wrong type: {}'.format(bad_types[0])

        bad_shapes = [state_tensor.get_shape()
                      for state in states
                      for state_tensor in state
                      if state_tensor.get_shape().as_list() not in [[None, rnn_size], [batch_size, rnn_size]]]
        assert not bad_shapes,\
            'Found wrong shape: {}'.format(bad_shapes[0])

    _print_success_message()


def test_decoding_layer(decoding_layer):
    batch_size = 64
    vocab_size = 1000
    embedding_size = 200
    sequence_length = 22
    rnn_size = 512
    num_layers = 3
    target_vocab_to_int = {'<EOS>': 1, '<GO>': 3}

    with tf.Graph().as_default():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        dec_embed_input = tf.placeholder(tf.float32, [batch_size, 22, embedding_size])
=======


        target_sequence_length_p = tf.placeholder(tf.int32, (None,), name='target_sequence_length')
        max_target_sequence_length = tf.reduce_max(target_sequence_length_p, name='max_target_len')

        dec_input = tf.placeholder(tf.int32, [batch_size, sequence_length])
        dec_embed_input = tf.placeholder(tf.float32, [batch_size, sequence_length, embedding_size])
>>>>>>> bbae529... Original from Udacity
=======
        dec_embed_input = tf.placeholder(tf.float32, [batch_size, 22, embedding_size])
>>>>>>> 307c83c... submission_01
=======
        dec_embed_input = tf.placeholder(tf.float32, [batch_size, 22, embedding_size])
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
        dec_embeddings = tf.placeholder(tf.float32, [vocab_size, embedding_size])
        keep_prob = tf.placeholder(tf.float32)
        state = tf.contrib.rnn.LSTMStateTuple(
            tf.placeholder(tf.float32, [None, rnn_size]),
            tf.placeholder(tf.float32, [None, rnn_size]))
        encoder_state = (state, state, state)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        train_output, inf_output = decoding_layer(dec_embed_input, dec_embeddings, encoder_state, vocab_size,
                                                  sequence_length, rnn_size, num_layers, target_vocab_to_int, keep_prob)

        assert isinstance(train_output, tf.Tensor),\
            'Train Logits is wrong type: {}'.format(type(train_output))
        assert isinstance(inf_output, tf.Tensor), \
            'Inference Logits is wrong type: {}'.format(type(inf_output))

        assert train_output.get_shape().as_list() == [batch_size, None, vocab_size],\
            'Train Logits is the wrong shape: {}'.format(train_output.get_shape())
        assert inf_output.get_shape().as_list() == [None, None, vocab_size], \
            'Inference Logits is the wrong shape: {}'.format(inf_output.get_shape())
=======
        train_decoder_output, infer_logits_output = decoding_layer( dec_input,
                                                   encoder_state,
                                                   target_sequence_length_p,
                                                   max_target_sequence_length,
                                                   rnn_size,
                                                   num_layers,
                                                   target_vocab_to_int,
                                                   vocab_size,
                                                   batch_size,
                                                   keep_prob,
                                                   embedding_size)



        assert isinstance(train_decoder_output, tf.contrib.seq2seq.BasicDecoderOutput),\
            'Found wrong type: {}'.format(type(train_decoder_output))
        assert isinstance(infer_logits_output, tf.contrib.seq2seq.BasicDecoderOutput),\
            'Found wrong type: {}'.format(type(infer_logits_output))

        assert train_decoder_output.rnn_output.get_shape().as_list() == [batch_size, None, vocab_size], \
            'Wrong shape returned.  Found {}'.format(train_decoder_output.rnn_output.get_shape())
        assert infer_logits_output.sample_id.get_shape().as_list() == [batch_size, None], \
             'Wrong shape returned.  Found {}'.format(infer_logits_output.sample_id.get_shape())
=======
        train_output, inf_output = decoding_layer(dec_embed_input, dec_embeddings, encoder_state, vocab_size,
                                                  sequence_length, rnn_size, num_layers, target_vocab_to_int, keep_prob)
>>>>>>> 307c83c... submission_01
=======
        train_output, inf_output = decoding_layer(dec_embed_input, dec_embeddings, encoder_state, vocab_size,
                                                  sequence_length, rnn_size, num_layers, target_vocab_to_int, keep_prob)
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

        assert isinstance(train_output, tf.Tensor),\
            'Train Logits is wrong type: {}'.format(type(train_output))
        assert isinstance(inf_output, tf.Tensor), \
            'Inference Logits is wrong type: {}'.format(type(inf_output))

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbae529... Original from Udacity
=======
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
        assert train_output.get_shape().as_list() == [batch_size, None, vocab_size],\
            'Train Logits is the wrong shape: {}'.format(train_output.get_shape())
        assert inf_output.get_shape().as_list() == [None, None, vocab_size], \
            'Inference Logits is the wrong shape: {}'.format(inf_output.get_shape())
<<<<<<< HEAD
>>>>>>> 307c83c... submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

    _print_success_message()


def test_seq2seq_model(seq2seq_model):
    batch_size = 64
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    target_vocab_size = 300
=======
    vocab_size = 300
    embedding_size = 100
>>>>>>> bbae529... Original from Udacity
=======
    target_vocab_size = 300
>>>>>>> 307c83c... submission_01
=======
    target_vocab_size = 300
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    sequence_length = 22
    rnn_size = 512
    num_layers = 3
    target_vocab_to_int = {'<EOS>': 1, '<GO>': 3}

    with tf.Graph().as_default():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        input_data = tf.placeholder(tf.int32, [64, 22])
        target_data = tf.placeholder(tf.int32, [64, 22])
        keep_prob = tf.placeholder(tf.float32)
        train_output, inf_output = seq2seq_model(input_data, target_data, keep_prob, batch_size, sequence_length,
                                                 200, target_vocab_size, 64, 80, rnn_size, num_layers, target_vocab_to_int)

        assert isinstance(train_output, tf.Tensor),\
            'Train Logits is wrong type: {}'.format(type(train_output))
        assert isinstance(inf_output, tf.Tensor), \
            'Inference Logits is wrong type: {}'.format(type(inf_output))

        assert train_output.get_shape().as_list() == [batch_size, None, target_vocab_size],\
            'Train Logits is the wrong shape: {}'.format(train_output.get_shape())
        assert inf_output.get_shape().as_list() == [None, None, target_vocab_size], \
            'Inference Logits is the wrong shape: {}'.format(inf_output.get_shape())

=======

        dec_input = tf.placeholder(tf.int32, [batch_size, sequence_length])
        dec_embed_input = tf.placeholder(tf.float32, [batch_size, sequence_length, embedding_size])
        dec_embeddings = tf.placeholder(tf.float32, [vocab_size, embedding_size])
=======
        input_data = tf.placeholder(tf.int32, [64, 22])
        target_data = tf.placeholder(tf.int32, [64, 22])
>>>>>>> 307c83c... submission_01
=======
        input_data = tf.placeholder(tf.int32, [64, 22])
        target_data = tf.placeholder(tf.int32, [64, 22])
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
        keep_prob = tf.placeholder(tf.float32)
        train_output, inf_output = seq2seq_model(input_data, target_data, keep_prob, batch_size, sequence_length,
                                                 200, target_vocab_size, 64, 80, rnn_size, num_layers, target_vocab_to_int)

        assert isinstance(train_output, tf.Tensor),\
            'Train Logits is wrong type: {}'.format(type(train_output))
        assert isinstance(inf_output, tf.Tensor), \
            'Inference Logits is wrong type: {}'.format(type(inf_output))

        assert train_output.get_shape().as_list() == [batch_size, None, target_vocab_size],\
            'Train Logits is the wrong shape: {}'.format(train_output.get_shape())
        assert inf_output.get_shape().as_list() == [None, None, target_vocab_size], \
            'Inference Logits is the wrong shape: {}'.format(inf_output.get_shape())

<<<<<<< HEAD
<<<<<<< HEAD
        input_data = tf.placeholder(tf.int32, [batch_size, sequence_length])
        target_data = tf.placeholder(tf.int32, [batch_size, sequence_length])
        keep_prob = tf.placeholder(tf.float32)
        source_sequence_length = tf.placeholder(tf.int32, (None,), name='source_sequence_length')
        target_sequence_length_p = tf.placeholder(tf.int32, (None,), name='target_sequence_length')
        max_target_sequence_length = tf.reduce_max(target_sequence_length_p, name='max_target_len')

        train_decoder_output, infer_logits_output = seq2seq_model(  input_data,
                                                   target_data,
                                                   keep_prob,
                                                   batch_size,
                                                   source_sequence_length,
                                                   target_sequence_length_p,
                                                   max_target_sequence_length,
                                                   vocab_size,
                                                   vocab_size,
                                                   embedding_size,
                                                   embedding_size,
                                                   rnn_size,
                                                   num_layers,
                                                   target_vocab_to_int)

        # input_data, target_data, keep_prob, batch_size, sequence_length,
        # 200, target_vocab_size, 64, 80, rnn_size, num_layers, target_vocab_to_int)

        assert isinstance(train_decoder_output, tf.contrib.seq2seq.BasicDecoderOutput),\
            'Found wrong type: {}'.format(type(train_decoder_output))
        assert isinstance(infer_logits_output, tf.contrib.seq2seq.BasicDecoderOutput),\
            'Found wrong type: {}'.format(type(infer_logits_output))

        assert train_decoder_output.rnn_output.get_shape().as_list() == [batch_size, None, vocab_size], \
            'Wrong shape returned.  Found {}'.format(train_decoder_output.rnn_output.get_shape())
        assert infer_logits_output.sample_id.get_shape().as_list() == [batch_size, None], \
             'Wrong shape returned.  Found {}'.format(infer_logits_output.sample_id.get_shape())
>>>>>>> bbae529... Original from Udacity
=======
>>>>>>> 307c83c... submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

    _print_success_message()


def test_sentence_to_seq(sentence_to_seq):
    sentence = 'this is a test sentence'
    vocab_to_int = {'<PAD>': 0, '<EOS>': 1, '<UNK>': 2, 'this': 3, 'is': 6, 'a': 5, 'sentence': 4}

    output = sentence_to_seq(sentence, vocab_to_int)

    assert len(output) == 5,\
        'Wrong length. Found a length of {}'.format(len(output))

    assert output[3] == 2,\
        'Missing <UNK> id.'

    assert np.array_equal(output, [3, 6, 5, 2, 4]),\
        'Incorrect ouput. Found {}'.format(output)

    _print_success_message()


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def test_process_decoding_input(process_decoding_input):
=======
def test_process_encoding_input(process_encoding_input):
>>>>>>> bbae529... Original from Udacity
=======
def test_process_decoding_input(process_decoding_input):
>>>>>>> 307c83c... submission_01
=======
def test_process_decoding_input(process_decoding_input):
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    batch_size = 2
    seq_length = 3
    target_vocab_to_int = {'<GO>': 3}
    with tf.Graph().as_default():
        target_data = tf.placeholder(tf.int32, [batch_size, seq_length])
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        dec_input = process_decoding_input(target_data, target_vocab_to_int, batch_size)
=======
        dec_input = process_encoding_input(target_data, target_vocab_to_int, batch_size)
>>>>>>> bbae529... Original from Udacity
=======
        dec_input = process_decoding_input(target_data, target_vocab_to_int, batch_size)
>>>>>>> 307c83c... submission_01
=======
        dec_input = process_decoding_input(target_data, target_vocab_to_int, batch_size)
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

        assert dec_input.get_shape() == (batch_size, seq_length),\
            'Wrong shape returned.  Found {}'.format(dec_input.get_shape())

        test_target_data = [[10, 20, 30], [40, 18, 23]]
        with tf.Session() as sess:
            test_dec_input = sess.run(dec_input, {target_data: test_target_data})

        assert test_dec_input[0][0] == target_vocab_to_int['<GO>'] and\
               test_dec_input[1][0] == target_vocab_to_int['<GO>'],\
            'Missing GO Id.'

    _print_success_message()


def test_decoding_layer_train(decoding_layer_train):
    batch_size = 64
    vocab_size = 1000
    embedding_size = 200
    sequence_length = 22
    rnn_size = 512
    num_layers = 3

    with tf.Graph().as_default():
        with tf.variable_scope("decoding") as decoding_scope:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            dec_cell = tf.contrib.rnn.MultiRNNCell([tf.contrib.rnn.BasicLSTMCell(rnn_size)] * num_layers)
            output_fn = lambda x: tf.contrib.layers.fully_connected(x, vocab_size, None, scope=decoding_scope)
            dec_embed_input = tf.placeholder(tf.float32, [batch_size, 22, embedding_size])
            keep_prob = tf.placeholder(tf.float32)
            state = tf.contrib.rnn.LSTMStateTuple(
                tf.placeholder(tf.float32, [None, rnn_size]),
                tf.placeholder(tf.float32, [None, rnn_size]))
            encoder_state = (state, state, state)

            train_logits = decoding_layer_train(encoder_state, dec_cell, dec_embed_input, sequence_length,
                                 decoding_scope, output_fn, keep_prob)

            assert train_logits.get_shape().as_list() == [batch_size, None, vocab_size], \
                'Wrong shape returned.  Found {}'.format(train_logits.get_shape())
=======
            # dec_cell = tf.contrib.rnn.MultiRNNCell([tf.contrib.rnn.BasicLSTMCell(rnn_size)] * num_layers)

            dec_embed_input = tf.placeholder(tf.float32, [batch_size, sequence_length, embedding_size])
=======
            dec_cell = tf.contrib.rnn.MultiRNNCell([tf.contrib.rnn.BasicLSTMCell(rnn_size)] * num_layers)
            output_fn = lambda x: tf.contrib.layers.fully_connected(x, vocab_size, None, scope=decoding_scope)
            dec_embed_input = tf.placeholder(tf.float32, [batch_size, 22, embedding_size])
>>>>>>> 307c83c... submission_01
=======
            dec_cell = tf.contrib.rnn.MultiRNNCell([tf.contrib.rnn.BasicLSTMCell(rnn_size)] * num_layers)
            output_fn = lambda x: tf.contrib.layers.fully_connected(x, vocab_size, None, scope=decoding_scope)
            dec_embed_input = tf.placeholder(tf.float32, [batch_size, 22, embedding_size])
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
            keep_prob = tf.placeholder(tf.float32)
            state = tf.contrib.rnn.LSTMStateTuple(
                tf.placeholder(tf.float32, [None, rnn_size]),
                tf.placeholder(tf.float32, [None, rnn_size]))
            encoder_state = (state, state, state)

            train_logits = decoding_layer_train(encoder_state, dec_cell, dec_embed_input, sequence_length,
                                 decoding_scope, output_fn, keep_prob)

<<<<<<< HEAD
<<<<<<< HEAD

            assert isinstance(train_decoder_output, tf.contrib.seq2seq.BasicDecoderOutput),\
                'Found wrong type: {}'.format(type(train_decoder_output))

            assert train_decoder_output.rnn_output.get_shape().as_list() == [batch_size, None, vocab_size], \
                'Wrong shape returned.  Found {}'.format(train_decoder_output.rnn_output.get_shape())
>>>>>>> bbae529... Original from Udacity
=======
            assert train_logits.get_shape().as_list() == [batch_size, None, vocab_size], \
                'Wrong shape returned.  Found {}'.format(train_logits.get_shape())
>>>>>>> 307c83c... submission_01
=======
            assert train_logits.get_shape().as_list() == [batch_size, None, vocab_size], \
                'Wrong shape returned.  Found {}'.format(train_logits.get_shape())
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

    _print_success_message()


def test_decoding_layer_infer(decoding_layer_infer):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    batch_size = 64
>>>>>>> bbae529... Original from Udacity
=======
>>>>>>> 307c83c... submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    vocab_size = 1000
    sequence_length = 22
    embedding_size = 200
    rnn_size = 512
    num_layers = 3

    with tf.Graph().as_default():
        with tf.variable_scope("decoding") as decoding_scope:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            dec_cell = tf.contrib.rnn.MultiRNNCell([tf.contrib.rnn.BasicLSTMCell(rnn_size)] * num_layers)
            output_fn = lambda x: tf.contrib.layers.fully_connected(x, vocab_size, None, scope=decoding_scope)
            dec_embeddings = tf.placeholder(tf.float32, [vocab_size, embedding_size])
            keep_prob = tf.placeholder(tf.float32)
            state = tf.contrib.rnn.LSTMStateTuple(
                tf.placeholder(tf.float32, [None, rnn_size]),
                tf.placeholder(tf.float32, [None, rnn_size]))
            encoder_state = (state, state, state)

            infer_logits = decoding_layer_infer(encoder_state, dec_cell, dec_embeddings, 10, 20,
                                sequence_length, vocab_size, decoding_scope, output_fn, keep_prob)

            assert infer_logits.get_shape().as_list() == [None, None, vocab_size], \
                 'Wrong shape returned.  Found {}'.format(infer_logits.get_shape())
=======

            dec_embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size]))

            dec_embed_input = tf.placeholder(tf.float32, [batch_size, sequence_length, embedding_size])
=======
            dec_cell = tf.contrib.rnn.MultiRNNCell([tf.contrib.rnn.BasicLSTMCell(rnn_size)] * num_layers)
            output_fn = lambda x: tf.contrib.layers.fully_connected(x, vocab_size, None, scope=decoding_scope)
            dec_embeddings = tf.placeholder(tf.float32, [vocab_size, embedding_size])
>>>>>>> 307c83c... submission_01
=======
            dec_cell = tf.contrib.rnn.MultiRNNCell([tf.contrib.rnn.BasicLSTMCell(rnn_size)] * num_layers)
            output_fn = lambda x: tf.contrib.layers.fully_connected(x, vocab_size, None, scope=decoding_scope)
            dec_embeddings = tf.placeholder(tf.float32, [vocab_size, embedding_size])
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
            keep_prob = tf.placeholder(tf.float32)
            state = tf.contrib.rnn.LSTMStateTuple(
                tf.placeholder(tf.float32, [None, rnn_size]),
                tf.placeholder(tf.float32, [None, rnn_size]))
            encoder_state = (state, state, state)

            infer_logits = decoding_layer_infer(encoder_state, dec_cell, dec_embeddings, 10, 20,
                                sequence_length, vocab_size, decoding_scope, output_fn, keep_prob)

<<<<<<< HEAD
<<<<<<< HEAD
            assert infer_logits_output.sample_id.get_shape().as_list() == [batch_size, None], \
                 'Wrong shape returned.  Found {}'.format(infer_logits_output.sample_id.get_shape())
>>>>>>> bbae529... Original from Udacity
=======
            assert infer_logits.get_shape().as_list() == [None, None, vocab_size], \
                 'Wrong shape returned.  Found {}'.format(infer_logits.get_shape())
>>>>>>> 307c83c... submission_01
=======
            assert infer_logits.get_shape().as_list() == [None, None, vocab_size], \
                 'Wrong shape returned.  Found {}'.format(infer_logits.get_shape())
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

    _print_success_message()
