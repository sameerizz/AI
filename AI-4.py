# Program 4: Write a program to implement Backpropagation Algorithm

import numpy as np

class NeuralNetwork():
    
    def __init__(self):
        np.random.seed(1)  # Set random seed for reproducibility
        
        # Initialize synaptic weights with random values between -1 and 1
        self.synaptic_weights = 2 * np.random.random((3,1)) - 1

    def sigmoid(self, x):
        # Activation function: sigmoid
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        # Derivative of sigmoid function for backpropagation
        return x * (1 - x)
    
    def train(self, training_inputs, training_outputs, num_iterations):
        for iteration in range(num_iterations):
            # Forward pass
            outputs = self.think(training_inputs)
            
            # Calculate error
            error = training_outputs - outputs
            
            # Backpropagation
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(outputs))
            
            # Update weights
            self.synaptic_weights += adjustments

    def think(self, inputs):
        # Convert inputs to float
        inputs = inputs.astype(float)
        
        # Calculate output using sigmoid activation
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

if __name__ == '__main__':
    neural_network = NeuralNetwork()  
    print('Random starting synaptic weights:')
    print(neural_network.synaptic_weights)
    
    # Training data
    training_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_outputs = np.array([[0, 1, 1, 0]]).T
    
    # Train the neural network
    neural_network.train(training_inputs, training_outputs, 10000)
    
    print('New synaptic weights after training:')
    print(neural_network.synaptic_weights)
    
    # Get user input for prediction
    A = float(input('Input 1: '))
    B = float(input('Input 2: '))
    C = float(input('Input 3: '))
    
    print('New situation: input data =', A, B, C)
    print('Predicted output:')
    print(neural_network.think(np.array([A, B, C])))