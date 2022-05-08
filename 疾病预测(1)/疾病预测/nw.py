import numpy
import scipy.special
import scipy.ndimage

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
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        pass


    def log_loss(self,y_hat, y):
        return -(y*(self.activation_function(y_hat) + (1 - y) * self.activation_function(1 - y_hat)))

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs

input_nodes = 10
hidden_nodes = 200
output_nodes = 1
learning_rate = 0.01
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)
training_data_file = open("mnist_dataset/cardio_train.csv", 'r')
training_data_list = training_data_file.read().splitlines()
training_data_file.close()
epochs = 1

for e in range(epochs):
    for record in training_data_list:
        all_values = record.split(';')
        if all_values[0] == '':
            continue
        targets = numpy.array([all_values[10]], dtype=int)
        inputs =  numpy.array(all_values[0:10], dtype=int)
        n.train(inputs, targets)
        pass
    pass
test_data_file = open("mnist_dataset/cardio_train.csv", 'r')
test_data_list = test_data_file.read().splitlines()
test_data_file.close()

scorecard = []
deviations = []
correct_labels = []
outputs_total = []
# mean squared error
mean_squared_errors = []
mean_squared_error_total = 1
# Classification rate
classification_rates = []
# Classification accuracy
classification_accuracys = []
# total psotion
total_psotion = 1
total_psotions = []
degree = 0
for record in test_data_list:
    all_values = record.split(';')
    if all_values[0] == '':
        continue
    degree += 1
    correct_label = int(all_values[10])
    correct_labels.append(correct_label)
    inputs= numpy.array(all_values[0:10], dtype=int)
    outputs = n.query(inputs)
    if outputs[0][0] > 0:
        label = 1
    else:
        label = 0    
    # mean_squared_error_total += (outputs[0][0] - correct_label) * (outputs[0][0] - correct_label)
    mean_squared_errors.append(n.log_loss(outputs[0][0],label))
    outputs_total.append(label)
    if (label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)
    if correct_label == 1:
        total_psotion+=1
    total_psotions.append(sum(scorecard) / total_psotion)
    pass

degree = 0
# tp
scorecard_total = 0
for record in scorecard:
    degree += 1
    scorecard_total += record
    classification_rates.append(scorecard_total / degree)
    classification_accuracys.append((degree - scorecard_total) / degree)