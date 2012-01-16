#!/usr/bin/python

import math
import random

class Layer:
    def __init__(self, prev_num, curr_num, is_input):
        self.act = [0.0] * curr_num # node activation values
        self.in = [0.0] * curr_num # sums without sigmoid
        self.delta. = [0.0] * curr_num #error
        self.weight = [[0.0] * prev_num] * curr_num # link weights
        if is_input: #input layer does not need weights
            for i in range(prev_num):
                for j in range(curr_num):
                    weight[i][j] = -1 + 2 * random.random() # initialize weights to [-1.0, 1.0]
        self.is_input = is_input;

class NeuralNetwork:
    def __init__(self, data, learning_rate, training_set_size, num_epochs):
        self.data = data
        self.learning_rate = learning_rate;
        self.sizes = [];
        self.layers = [];

        
        
        #learning_rate = new double[lr.length];
        #for (int i = 0; i < lr.length; i++) {
        #  learning_rate[i] = lr[i] * (trainingSetSize / 40);
        #}
        
        num_layers = 3;
        size_input = 196 # ie 14x14 = 196
        size_hidden = 10 # arbitrary
        size_output = 11 # 0-10
        self.sizes = [size_input, size_hidden, size_output]
        
        # initialize layers (weights)
        input = Layer(0, size_input, true);
        hidden = Layer(size_input, size_hidden, false);
        output = Layer(size_hidden, size_output, false);
        self.layers = [input, hidden, output];
        
        # train for num_epochs epochs
        for x in range(num_epochs):
            for i in range(training_size):
                
                # initialize desired output vector
                desired_output = [-1.0] * size_output
                desired_output[data.trainlabel[i]] = 1.0 # ???
                
                # propagate inputs forward to compute outputs
                # input               
                for j in range(size_input):
                    layers[0].act[j] = data.trainex[i][j]
                    
                # hidden + output
                for j in range(1, 2):
                    for k in range(sizes[j]):
                        sum = 0
                        for l in range(sizes[j-1]):
                            sum += layers[j].weight[l][k] * layers[j-1].act[l]
                        layers[j].in[k] = sum
                        layers[j].act[k] = sigmoid(sum)
                
                # propagate deltas backward from output to input
                # output
                for j in range(size_output):
                    layers[2].delta[j] = d_sigmoid(layers[2].in[j]) * (desired_output[j] - layers[2].act[0])
                    
                for j in range(1, -1, 1):
                    for k in range(sizes[j]):
                        
                
                # update every weight in network using deltas
            
        
    def predict(sample):
    
    def sigmoid(a):
        return math.tanh(a)
        
    def d_sigmoid(a):
        return 1 - math.pow(sigmoid(a), 2)

