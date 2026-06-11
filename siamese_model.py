from tensorflow.keras import layers
from tensorflow.keras import models

def create_siamese_network(input_shape):

    inputs = layers.Input(shape=input_shape)

    x = layers.Conv2D(32, (3,3), activation='relu')(inputs)
    x = layers.MaxPooling2D((2,2))(x)

    x = layers.Conv2D(64, (3,3), activation='relu')(x)
    x = layers.MaxPooling2D((2,2))(x)

    x = layers.Flatten()(x)

    x = layers.Dense(128, activation='relu')(x)

    outputs = layers.Dense(64)(x)

    return models.Model(inputs, outputs)
