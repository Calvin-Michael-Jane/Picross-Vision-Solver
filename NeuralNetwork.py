#!/usr/bin/python

import math
import random
import pickle

class Layer:
    def __init__(self, prev_num, curr_num, is_input):
        self.act = [0.0] * curr_num # node activation values
        self.insum = [0.0] * curr_num # sums without sigmoid
        self.delta = [0.0] * curr_num #error
        if not is_input: # input layer does not need weights
            weight = []
            for i in range(prev_num):
                weight_row = []
                for j in range(curr_num):
                    weight_row.append(-1.0 + 2.0 * random.random())
                weight.append(weight_row)
            self.weight = weight
        self.is_input = is_input

# data is formatted as follows:
# line 1: number of samples
# line 2-N: 1 value per pixel + label value        
class DataSet:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            line = f.readline();
            line = line.strip()
            self.num_train = int(line)
            self.trainlabel = [0] * self.num_train
            trainex = []
            i = 0
            for line in f:
                ex = []
                line = line.strip()
                words = line.split(' ')
                for j in range(len(words)-1):
                    ex.append(float(words[j]))
                self.trainlabel[i] = int(words[-1])
                trainex.append(ex)
                i += 1

            self.trainex = trainex

class NeuralNetwork:

    def __init__(self, data_path, num_epochs):
        self.data = DataSet(data_path);
        self.sizes = []
        self.layers = []
        
        training_size = self.data.num_train
        
        
        num_layers = 3
        size_input = 196 # ie 14x14 = 196
        size_hidden = 10 # arbitrary
        size_output = 11 # 0-10
        learning_rate = 0.2
        self.sizes = [size_input, size_hidden, size_output]
        
        # initialize layers (weights)
        input = Layer(0, size_input, True)
        hidden = Layer(size_input, size_hidden, False)
        output = Layer(size_hidden, size_output, False)
        self.layers = [input, hidden, output]
        
        # train for num_epochs epochs
        for x in range(num_epochs):
            for i in range(training_size):
                
                # initialize desired output vector
                desired_output = [0.1] * size_output
                desired_output[self.data.trainlabel[i]] = 0.9 # ???
                
                # propagate inputs forward to compute outputs
                # input               
                for j in range(size_input):
                    self.layers[0].act[j] = self.data.trainex[i][j]
                    
                # hidden + output
                for j in range(1, 3):
                    for k in range(self.sizes[j]):
                        sum = 0.0
                        for l in range(self.sizes[j-1]):
                            sum += self.layers[j].weight[l][k] * self.layers[j-1].act[l]
                        self.layers[j].insum[k] = sum
                        self.layers[j].act[k] = sigmoid(sum)
                
                # propagate deltas backward from output to input
                # output
                for j in range(size_output):
                    self.layers[2].delta[j] = d_sigmoid(self.layers[2].insum[j]) * (desired_output[j] - self.layers[2].act[0])
                    
                for j in range(1, -1, 1):
                    for k in range(self.sizes[j]):
                        sum = 0.0
                        for l in range(self.sizes[j+1]):
                            sum += self.layers[j+1].weight[k][l] * self.layers[j+1].delta[l]
                        self.layers[j].delta[k] = d_sigmoid(self.layers[j].insum[k]) * sum
                
                # update every weight in network using deltas
                for j in range(1, 3):
                    for k in range(len(self.layers[j].weight)):
                        for l in range(len(self.layers[j].weight[k])):
                            self.layers[j].weight[k][l] += learning_rate * self.layers[j-1].act[k] * self.layers[j].delta[l]
           
        # print weights for savings
        # output = open('data/neuralnet', 'wb')
        # pickle.dump(self, output)
        
    def predict(self, training_sample):
        ## propagate inputs forward to compute outputs
        # input
        for i in range(len(training_sample)):
            self.layers[0].act[i] = training_sample[i]
        
        for i in range(1, 3):
            for j in range(self.sizes[i]):
                sum = 0.0
                for k in range(self.sizes[i-1]):
                    sum += self.layers[i].weight[k][j] * self.layers[i-1].act[k]
                self.layers[i].insum[j] = sum
                self.layers[i].act[j] = sigmoid(sum)
        
        max = -1.1
        max_val = -1
        for i in range(self.sizes[2]):
            if self.layers[2].act[i] > max:
                max = self.layers[2].act[i]
                max_val = i
        return max_val
 
def loadnet(filename):
    f = open(filename, 'rb')
    net = pickle.load(f)
    return net        
    
def sigmoid(a):
    return math.tanh(a)
    
    
def d_sigmoid(a):
    return 1 - math.pow(sigmoid(a), 2)

