from keras.models import Model
from keras.layers import (
        Input,
        Flatten,
        Dense,
        ZeroPadding2D,
        Conv2D,
        Activation,
        MaxPooling2D,
        BatchNormalization,
        Dropout)
from keras.models import Sequential
from keras.layers.advanced_activations import PReLU
from keras.layers import initializers

def hwdb_model(img_size, num_classes):
    model = Sequential()

    # 96C3
    model.add(
        Conv2D(filters=96, kernel_size=(3, 3), padding='same',
               input_shape=(img_size, img_size, 1), strides=(1, 1),
               kernel_initializer=initializers.he_normal()))
    # BN + PReLU
    model.add(BatchNormalization(axis=-1, momentum=0.9, epsilon=1e-6))
    model.add(PReLU())

    # MP3
    model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))

    # 128C3
    model.add(
        Conv2D(filters=128, kernel_size=(3, 3), padding='same',strides=(1, 1),
               kernel_initializer=initializers.he_normal()))
    # BN + PReLU
    model.add(BatchNormalization(axis=-1, momentum=0.9, epsilon=1e-6))
    model.add(PReLU())

    # MP3
    model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))

    # 160C3
    model.add(
        Conv2D(filters=160, kernel_size=(3, 3), padding='same',strides=(1, 1),
               kernel_initializer=initializers.he_normal()))
    # BN + PReLU
    model.add(BatchNormalization(axis=-1, momentum=0.9, epsilon=1e-6))
    model.add(PReLU())

    # MP3
    model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))

    # 256C3
    model.add(
        Conv2D(filters=256, kernel_size=(3, 3), padding='same',strides=(1, 1),
               kernel_initializer=initializers.he_normal()))
    # BN + PReLU
    model.add(BatchNormalization(axis=-1, momentum=0.9, epsilon=1e-6))
    model.add(PReLU())

    # MP3
    model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))

    # 384C3
    model.add(
        Conv2D(filters=384, kernel_size=(3, 3), padding='same',strides=(1, 1),
               kernel_initializer=initializers.he_normal()))
    # BN + PReLU
    model.add(BatchNormalization(axis=-1, momentum=0.9, epsilon=1e-6))
    model.add(PReLU())

    # 384C3
    model.add(
        Conv2D(filters=384, kernel_size=(3, 3), padding='same',strides=(1, 1),
               kernel_initializer=initializers.he_normal()))
    # BN + PReLU
    model.add(BatchNormalization(axis=-1, momentum=0.9, epsilon=1e-6))
    model.add(PReLU())

    # MP3
    model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))

    model.add(Flatten())
    # 1024FC
    model.add(Dense(1024, activation='relu'))

    model.add(Dropout(0.5))
    model.add(Dense(units=num_classes, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])
    return model
