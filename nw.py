import numpy
import scipy.special
import scipy.ndimage
import pickle
import matplotlib.pylab as plt
import pickle

save_file = "./mnist.pkl"


class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        self.lr = learningrate
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))
        pass

    def log_loss(self, y_hat, y):
        return -(y * (self.activation_function(y_hat) + (1 - y) * self.activation_function(1 - y_hat)))

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs


def train_modal(epochs=1):
    input_nodes = 12
    hidden_nodes = 200
    output_nodes = 1
    learning_rate = 0.01
    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    training_data_file = open("mnist_dataset/cardio_train.csv", 'r')
    training_data_list = training_data_file.read().splitlines()
    training_data_file.close()

    for e in range(epochs):
        key = -1
        for record in training_data_list:
            key += 1
            all_values = record.split(';')
            if all_values[0] == '':
                continue
            if key == 0:
                continue
            targets = numpy.array([all_values[12]], dtype=float)
            inputs = numpy.array(all_values[0:12], dtype=float)
            n.train(inputs, targets)
    pickle.dump(n.wih, open(f'./wih_value.pkl', 'wb'))
    pickle.dump(n.who, open(f'./who_value.pkl', 'wb'))


def loadNwValue(nn):
    # print(nn.wih)
    val1 = pickle.load(open(f'./wih_value.pkl', 'rb'))
    val2 = pickle.load(open(f'./who_value.pkl', 'rb'))
    nn.wih = val1
    nn.who = val2
    # print(nn.wih)
    return nn


def predict(list):
    input_nodes = 12
    hidden_nodes = 200
    output_nodes = 1
    learning_rate = 0.01
    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    nn = loadNwValue(n)
    result = nn.query(list)
    if result[0][0] < 0.5:
        return True
    else:
        return False


if __name__ == '__main__':
    input_nodes = 12
    hidden_nodes = 200
    output_nodes = 1
    learning_rate = 0.01
    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    loadNwValue(n)
