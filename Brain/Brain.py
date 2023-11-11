import tensorflow as tf

class NeuralNet(tf.keras.Model):
    def __init__(self, inp_size, hid_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = tf.keras.layers.Dense(hid_size, activation='relu', input_shape=(inp_size,))
        self.l2 =  tf.keras.layers.Dense(hid_size, activation='relu')
        self.l3 = tf.keras.layers.Dense(num_classes)

    def call(self, x):
        out = self.l1(x)
        out = self.l2(out)
        out = self.l3(out)
        return out
