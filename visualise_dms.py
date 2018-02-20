from matplotlib import pyplot
from math import cos, sin, atan
import numpy as np


class Neuron():
    def __init__(self, x, y, text = '', c=[None]):
        if c is [None]:
            c = np.ones(len(self.neurons))
        self.x = y
        self.y = x
        self.text = text
        self.c = c

    def draw(self):
        circle = pyplot.Circle((self.x, self.y), radius=neuron_radius, edgecolor=(0,0,0), alpha=0.5, facecolor=(self.c,self.c,self.c))
        text_string = pyplot.Text(self.x, self.y, self.text, color='r')
        pyplot.gca().add_patch(circle)
        pyplot.gca().add_artist(text_string)
        
        


class Layer():
    def __init__(self, network, number_of_neurons, test, c=[None]):
        self.previous_layer = self.__get_previous_layer(network)
        self.y = self.__calculate_layer_y_position()
        self.neurons = self.intialise_neurons(number_of_neurons, test, c)

    def intialise_neurons(self, number_of_neurons, text, c=[None]):
        neurons = []
        x = self.__calculate_left_margin_so_layer_is_centered(number_of_neurons)
        for iteration in xrange(number_of_neurons):
            self.text = text[number_of_neurons-iteration-1]
            self.c = c[number_of_neurons-iteration-1]
            neuron = Neuron(x, self.y, self.text, self.c)
            neurons.append(neuron)
            x += horizontal_distance_between_neurons
        return neurons

    def __calculate_left_margin_so_layer_is_centered(self, number_of_neurons):
        return horizontal_distance_between_neurons * (number_of_neurons_in_widest_layer - number_of_neurons) / 2

    def __calculate_layer_y_position(self):
        if self.previous_layer:
            return self.previous_layer.y + vertical_distance_between_layers
        else:
            return 0

    def __get_previous_layer(self, network):
        if len(network.layers) > 0:
            return network.layers[-1]
        else:
            return None

    def line_between_two_neurons(self, neuron1, neuron2):
        angle = atan((neuron2.x - neuron1.x) / float(neuron2.y - neuron1.y))
        x_adjustment = neuron_radius * sin(angle)
        y_adjustment = neuron_radius * cos(angle)
        line = pyplot.Line2D((neuron1.x - x_adjustment, neuron2.x + x_adjustment), (neuron1.y - y_adjustment, neuron2.y + y_adjustment))
        pyplot.gca().add_line(line)

    def draw(self):
        for neuron in self.neurons:
            neuron.draw()
            #if self.previous_layer:
            #    for previous_layer_neuron in self.previous_layer.neurons:
            #        self.__line_between_two_neurons(neuron, previous_layer_neuron)


class NeuralNetwork():
    def __init__(self):
        self.layers = []

    def add_layer(self, number_of_neurons, text, c=[None]):
        self.layer = Layer(self, number_of_neurons, text, c)
        self.layers.append(self.layer)

    def draw(self):
        for layer in self.layers:
            layer.draw()
            

#if __name__ == "__main__":
            
            

#network.__line_between_two_neurons(1,2)
#connections = [[1, 1]]

def draw_dms(i): 
    
    network.draw()        
    l0 = network.layers[0]
    l1 = network.layers[1]
    l2 = network.layers[2]
    l3 = network.layers[3]
    l4 = network.layers[4]
    
    for neuron in range(len(l1.neurons)/2):
        network.layer.line_between_two_neurons(l0.neurons[0], l1.neurons[neuron])
    for neuron in range(len(l1.neurons)/2):
        network.layer.line_between_two_neurons(l1.neurons[-neuron-1], l0.neurons[0])
    
    for neuron in range(len(l2.neurons)):
        network.layer.line_between_two_neurons(l2.neurons[neuron], l1.neurons[neuron])
    
    for neuron in range(1, len(l2.neurons)):
        network.layer.line_between_two_neurons(l2.neurons[neuron], l1.neurons[neuron-1])
    
    for neuron in range(1, len(l2.neurons)):
        network.layer.line_between_two_neurons(l1.neurons[-neuron], l2.neurons[-neuron])
        
    for neuron in range(1, len(l2.neurons)):
        network.layer.line_between_two_neurons(l1.neurons[-neuron], l2.neurons[-neuron-1])
        
    
    network.layer.line_between_two_neurons(l3.neurons[-1], l2.neurons[-1])
    network.layer.line_between_two_neurons(l3.neurons[-2], l2.neurons[-2])
    network.layer.line_between_two_neurons(l3.neurons[-3], l2.neurons[-3])
    network.layer.line_between_two_neurons(l3.neurons[-4], l2.neurons[-4])
    network.layer.line_between_two_neurons(l3.neurons[-5], l2.neurons[-5])
    network.layer.line_between_two_neurons(l3.neurons[-6], l2.neurons[-6])
    network.layer.line_between_two_neurons(l2.neurons[-6], l3.neurons[-7])
    
    network.layer.line_between_two_neurons(l4.neurons[-1], l3.neurons[-5])
    network.layer.line_between_two_neurons(l4.neurons[-2], l3.neurons[-5])
    network.layer.line_between_two_neurons(l4.neurons[-1], l3.neurons[-6])
    network.layer.line_between_two_neurons(l4.neurons[-1], l3.neurons[-7])
    network.layer.line_between_two_neurons(l4.neurons[-2], l3.neurons[-6])
    network.layer.line_between_two_neurons(l4.neurons[-2], l3.neurons[-7])
    
    
    pyplot.axis('scaled')
    pyplot.axis('off')
    pyplot.xlim(-5, 30)
    network.draw()
    pyplot.savefig('dms_time%d.png' % i)
    pyplot.show()
        
# set params
vertical_distance_between_layers = 6
horizontal_distance_between_neurons = 2.5
neuron_radius = 1.1#0.5
number_of_neurons_in_widest_layer = 8

# time 1
network = NeuralNetwork()
network.add_layer(1,['DMS'],[0])
network.add_layer(8,['t1','t2','t3','t4','t5','t6','t7','t8'],[1]*8)
network.add_layer(6,['T1','T2','T3','T4','T5','T6'],[1]*6)
network.add_layer(7,['ATT','Gate','ATT','Gate','Diff','Up','Down'],[1]*7)
network.add_layer(2,['Same','Different'],[1]*2)
draw_dms(1)

# time 2
network = NeuralNetwork()
network.add_layer(1,['DMS'],[1])
network.add_layer(8,['t1','t2','t3','t4','t5','t6','t7','t8'],np.arange(0.,0.16,0.02))
network.add_layer(6,['T1','T2','T3','T4','T5','T6'],[0,1,1,1,1,1])
network.add_layer(7,['ATT','Gate','ATT','Gate','Diff','Up','Down'],[0,1,1,1,1,1,1])
network.add_layer(2,['Same','Different'],[1]*2)
draw_dms(2)

# time 3
network = NeuralNetwork()
network.add_layer(1,['DMS'],[1])
network.add_layer(8,['t1','t2','t3','t4','t5','t6','t7','t8'],np.arange(0.16,0.24,0.01))
network.add_layer(6,['T1','T2','T3','T4','T5','T6'],[1,0,1,1,1,1])
network.add_layer(7,['ATT','Gate','ATT','Gate','Diff','Up','Down'],[1,0,1,1,1,1,1])
network.add_layer(2,['Same','Different'],[1]*2)
draw_dms(3)

# time 4
network = NeuralNetwork()
network.add_layer(1,['DMS'],[1])
network.add_layer(8,['t1','t2','t3','t4','t5','t6','t7','t8'],np.arange(0.24,0.32,0.01))
network.add_layer(6,['T1','T2','T3','T4','T5','T6'],[1,1,0,1,1,1])
network.add_layer(7,['ATT','Gate','ATT','Gate','Diff','Up','Down'],[1,1,0,1,1,1,1])
network.add_layer(2,['Same','Different'],[1]*2)
draw_dms(4)

# time 5
network = NeuralNetwork()
network.add_layer(1,['DMS'],[1])
network.add_layer(8,['t1','t2','t3','t4','t5','t6','t7','t8'],np.arange(0.32,0.4,0.01))
network.add_layer(6,['T1','T2','T3','T4','T5','T6'],[1,1,1,0,1,1])
network.add_layer(7,['ATT','Gate','ATT','Gate','Diff','Up','Down'],[1,1,1,0,1,1,1])
network.add_layer(2,['Same','Different'],[1]*2)
draw_dms(5)

# time 6
network = NeuralNetwork()
network.add_layer(1,['DMS'],[1])
network.add_layer(8,['t1','t2','t3','t4','t5','t6','t7','t8'],np.arange(0.4,0.48,0.01))
network.add_layer(6,['T1','T2','T3','T4','T5','T6'],[1,1,1,1,0,1])
network.add_layer(7,['ATT','Gate','ATT','Gate','Diff','Up','Down'],[1,1,1,1,0,1,1])
network.add_layer(2,['Same','Different'],[1]*2)
draw_dms(6)

# time 7
network = NeuralNetwork()
network.add_layer(1,['DMS'],[1])
network.add_layer(8,['t1','t2','t3','t4','t5','t6','t7','t8'],np.arange(0.48,0.64,0.02))
network.add_layer(6,['T1','T2','T3','T4','T5','T6'],[1,1,1,1,0,1])
network.add_layer(7,['ATT','Gate','ATT','Gate','Diff','Up','Down'],[1,1,1,1,0,1,1])
network.add_layer(2,['Same','Different'],[1]*2)
draw_dms(7)

# time 8
network = NeuralNetwork()
network.add_layer(1,['DMS'],[1])
network.add_layer(8,['t1','t2','t3','t4','t5','t6','t7','t8'],np.arange(0.64,0.96,0.02))
network.add_layer(6,['T1','T2','T3','T4','T5','T6'],[1,1,1,1,1,0])
network.add_layer(7,['ATT','Gate','ATT','Gate','Diff','Up','Down'],[1,1,1,1,0,1,0])
network.add_layer(2,['Same','Different'],[1, 0])
draw_dms(8)
