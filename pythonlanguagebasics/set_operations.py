
# Set Operations


# Set declaration
deep_learning_neuron_set = set(['neuron_solo', 'multi_perceptron', 'multi_perceptron', 'RNN'])
deep_learning_neuron_set_aliter = {'neuron_solo', 'multi_perceptron', 'multi_perceptron', 'RNN'}




deep_learning_neuron_subset = set(['neuron_solo', 'multi_perceptron', 'multi_perceptron'])

deep_learning_neuron_superset = set(['neuron_solo', 'multi_perceptron', 'multi_perceptron', 'RNN', 'neural_network_algorithms'])




print(deep_learning_neuron_subset.issubset(deep_learning_neuron_set))

print(deep_learning_neuron_superset.issuperset(deep_learning_neuron_set))

print(deep_learning_neuron_set)


