from keras import backend as K
from keras.models import Model
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
from keras.layers import (BatchNormalization, Conv1D, Dense, Input,
    TimeDistributed, Activation, Bidirectional, SimpleRNN, GRU, LSTM, Dropout)

def simple_rnn_model(input_dim, output_dim=29):
    """ Build a recurrent network for speech
<<<<<<< HEAD
=======
from keras.layers import (BatchNormalization, Conv1D, Dense, Input, 
    TimeDistributed, Activation, Bidirectional, SimpleRNN, GRU, LSTM)

def simple_rnn_model(input_dim, output_dim=29):
    """ Build a recurrent network for speech 
>>>>>>> 35908f4... Base Code
=======
from keras.layers import (BatchNormalization, Conv1D, Dense, Input,
    TimeDistributed, Activation, Bidirectional, SimpleRNN, GRU, LSTM, Dropout)

def simple_rnn_model(input_dim, output_dim=29):
    """ Build a recurrent network for speech
>>>>>>> 6271737... Submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    # Add recurrent layer
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    simp_rnn = GRU(output_dim, return_sequences=True,
=======
    simp_rnn = GRU(output_dim, return_sequences=True, 
>>>>>>> 35908f4... Base Code
=======
    simp_rnn = GRU(output_dim, return_sequences=True,
>>>>>>> 6271737... Submission_01
=======
    simp_rnn = GRU(output_dim, return_sequences=True,
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
                 implementation=2, name='rnn')(input_data)
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(simp_rnn)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: x
    print(model.summary())
    return model

def rnn_model(input_dim, units, activation, output_dim=29):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    """ Build a recurrent network for speech
=======
    """ Build a recurrent network for speech 
>>>>>>> 35908f4... Base Code
=======
    """ Build a recurrent network for speech
>>>>>>> 6271737... Submission_01
=======
    """ Build a recurrent network for speech
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    # Add recurrent layer
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6271737... Submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    simp_rnn = GRU(units, activation=activation, return_sequences=True, implementation=2, name='rnn')(input_data)
    # TODO: Add batch normalization

    #bn_rnn = BatchNormalization(epsilon=1e-06, mode=0, momentum=0.9, weights=None)(simp_rnn)
    bn_rnn = BatchNormalization()(simp_rnn)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(time_dense)
    #y_pred = Activation('softmax', name='softmax')(simp_rnn)
<<<<<<< HEAD
=======
    simp_rnn = GRU(units, activation=activation,
        return_sequences=True, implementation=2, name='rnn')(input_data)
    # TODO: Add batch normalization 
    bn_rnn = ...
=======
>>>>>>> 6271737... Submission_01
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(time_dense)
<<<<<<< HEAD
>>>>>>> 35908f4... Base Code
=======
    #y_pred = Activation('softmax', name='softmax')(simp_rnn)
>>>>>>> 6271737... Submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: x
    print(model.summary())
    return model


def cnn_rnn_model(input_dim, filters, kernel_size, conv_stride,
    conv_border_mode, units, output_dim=29):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    """ Build a recurrent + convolutional network for speech
=======
    """ Build a recurrent + convolutional network for speech 
>>>>>>> 35908f4... Base Code
=======
    """ Build a recurrent + convolutional network for speech
>>>>>>> 6271737... Submission_01
=======
    """ Build a recurrent + convolutional network for speech
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    # Add convolutional layer
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    conv_1d = Conv1D(filters, kernel_size,
                     strides=conv_stride,
=======
    conv_1d = Conv1D(filters, kernel_size, 
                     strides=conv_stride, 
>>>>>>> 35908f4... Base Code
=======
    conv_1d = Conv1D(filters, kernel_size,
                     strides=conv_stride,
>>>>>>> 6271737... Submission_01
=======
    conv_1d = Conv1D(filters, kernel_size,
                     strides=conv_stride,
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
                     padding=conv_border_mode,
                     activation='relu',
                     name='conv1d')(input_data)
    # Add batch normalization
    bn_cnn = BatchNormalization(name='bn_conv_1d')(conv_1d)
    # Add a recurrent layer
    simp_rnn = SimpleRNN(units, activation='relu',
        return_sequences=True, implementation=2, name='rnn')(bn_cnn)
    # TODO: Add batch normalization
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    bn_rnn = BatchNormalization(name='bn_simp_rnn')(simp_rnn)
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
=======
    bn_rnn = ...
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = ...
>>>>>>> 35908f4... Base Code
=======
    bn_rnn = BatchNormalization(name='bn_simp_rnn')(simp_rnn)
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
>>>>>>> 6271737... Submission_01
=======
    bn_rnn = BatchNormalization(name='bn_simp_rnn')(simp_rnn)
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(time_dense)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: cnn_output_length(
        x, kernel_size, conv_border_mode, conv_stride)
    print(model.summary())
    return model

def cnn_output_length(input_length, filter_size, border_mode, stride,
                       dilation=1):
    """ Compute the length of the output sequence after 1D convolution along
        time. Note that this function is in line with the function used in
        Convolution1D class from Keras.
    Params:
        input_length (int): Length of the input sequence.
        filter_size (int): Width of the convolution kernel.
        border_mode (str): Only support `same` or `valid`.
        stride (int): Stride size used in 1D convolution.
        dilation (int)
    """
    if input_length is None:
        return None
    assert border_mode in {'same', 'valid'}
    dilated_filter_size = filter_size + (filter_size - 1) * (dilation - 1)
    if border_mode == 'same':
        output_length = input_length
    elif border_mode == 'valid':
        output_length = input_length - dilated_filter_size + 1
    return (output_length + stride - 1) // stride

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0


def deep_rnn_model(input_dim, units, recur_layers, output_dim=29):
    """ Build a deep recurrent network for speech
<<<<<<< HEAD
=======
def deep_rnn_model(input_dim, units, recur_layers, output_dim=29):
    """ Build a deep recurrent network for speech 
>>>>>>> 35908f4... Base Code
=======


def deep_rnn_model(input_dim, units, recur_layers, output_dim=29):
    """ Build a deep recurrent network for speech
>>>>>>> 6271737... Submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    # TODO: Add recurrent layers, each with batch normalization
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6271737... Submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    # Add a recurrent layer
    #if recur_layers == 1:

    bn_rnn = BatchNormalization(name='bn_rnn')(input_data)

    for layer in range(recur_layers):
        rnn_name = 'rnn_%d' % layer
        bn_rnn_name = 'bn_'+rnn_name
        units = int(units/(layer + 1))
        rnn = GRU(units, activation='relu',
                  return_sequences=True, implementation=2,
                  name=rnn_name)(bn_rnn)
        bn_rnn = BatchNormalization(name=bn_rnn_name)(rnn)


<<<<<<< HEAD
<<<<<<< HEAD
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
=======
    ...
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = ...
>>>>>>> 35908f4... Base Code
=======
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
>>>>>>> 6271737... Submission_01
=======
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(time_dense)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: x
    print(model.summary())
    return model

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD


=======
>>>>>>> 35908f4... Base Code
=======


>>>>>>> 6271737... Submission_01
=======


>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
def bidirectional_rnn_model(input_dim, units, output_dim=29):
    """ Build a bidirectional recurrent network for speech
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    # TODO: Add bidirectional recurrent layer
    bidir_rnn = Bidirectional(GRU(units, activation='relu', return_sequences=True, implementation=2, name='bidir_rnn'))(input_data)
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bidir_rnn)
=======
=======

>>>>>>> 6271737... Submission_01
    # TODO: Add bidirectional recurrent layer
    bidir_rnn = Bidirectional(GRU(units, activation='relu', return_sequences=True, implementation=2, name='bidir_rnn'))(input_data)
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
<<<<<<< HEAD
    time_dense = ...
>>>>>>> 35908f4... Base Code
=======
    time_dense = TimeDistributed(Dense(output_dim))(bidir_rnn)
>>>>>>> 6271737... Submission_01
=======

    # TODO: Add bidirectional recurrent layer
    bidir_rnn = Bidirectional(GRU(units, activation='relu', return_sequences=True, implementation=2, name='bidir_rnn'))(input_data)
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bidir_rnn)
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(time_dense)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: x
    print(model.summary())
    return model

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6271737... Submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0

def final_model(input_dim, filters, kernel_size, conv_stride,
    conv_border_mode, units, dropout, recur_layers, output_dim=29):
    """ Build a deep network for speech
<<<<<<< HEAD
<<<<<<< HEAD
=======
def final_model():
    """ Build a deep network for speech 
>>>>>>> 35908f4... Base Code
=======
>>>>>>> 6271737... Submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    # TODO: Specify the layers in your network
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6271737... Submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    conv_1d = Conv1D(filters, kernel_size,
                     strides=conv_stride,
                     padding=conv_border_mode,
                     activation='relu',
                     name='conv1d')(input_data)
    # Add batch normalization
    bn_cnn = BatchNormalization(name='bn_conv_1d')(conv_1d)
    # Add dropout to avoid overfitting
    bn_cnn_do = Dropout(dropout)(bn_cnn)

    for layer in range(recur_layers):
        bidir_rnn_name = 'bidir_rnn_%d' % layer
        bn_bidir_rnn_name = 'bn_bidir_rnn_'+bidir_rnn_name

        bidir_rnn = Bidirectional(GRU(units, return_sequences=True,
                                name=bidir_rnn_name, implementation=2))(bn_cnn_do)
        # Add batch normalization to bidirectional rnn layer
        bn_bidir_rnn = BatchNormalization(name=bn_bidir_rnn_name)(bidir_rnn)
        # Add dropout to avoid overfitting
        bn_cnn_do = Dropout(dropout)(bn_bidir_rnn)

    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_cnn_do)
<<<<<<< HEAD
<<<<<<< HEAD
    # TODO: Add softmax activation layer
    y_pred =  Activation('softmax', name='softmax')(time_dense)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    # TODO: Specify model.output_length
    model.output_length = lambda x: cnn_output_length(
        x, kernel_size, conv_border_mode, conv_stride)
    print(model.summary())
    return model
=======
    ...
=======
>>>>>>> 6271737... Submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
    # TODO: Add softmax activation layer
    y_pred =  Activation('softmax', name='softmax')(time_dense)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    # TODO: Specify model.output_length
    model.output_length = lambda x: cnn_output_length(
        x, kernel_size, conv_border_mode, conv_stride)
    print(model.summary())
    return model
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 35908f4... Base Code
=======
>>>>>>> 6271737... Submission_01
=======
>>>>>>> a7568d9f54a58f4956b458fc6a3732a6565cdda0
