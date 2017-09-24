import tensorflow as tf
import csv

n_nodes_hl1 = 20
n_nodes_hl2 =20
n_nodes_hl3 = 20

n_classes = 2
batch_size = 10

x = tf.placeholder('float', [None, 14])
y = tf.placeholder('float', [None, 2])
#x_data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#y_data = [0,0]


def collect_data(file):
    size = sum(1 for row in open(file))
    x_return = [None] * size
    y_return = [None] * size
    reader = csv.reader(open(file), delimiter=',')
    print(reader)
    i = 0
    for row in reader:
        x_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        y_data = [0, 0]
        if ((row[0] == 'Alabama') or (row[1] == 'Alabama')):
            x_data[0] = 1
        if ((row[0] == 'Arkansas') or (row[1] == 'Arkansas')):
            x_data[1] = 1
        if ((row[0] == 'Auburn') or (row[1] == 'Auburn')):
            x_data[2] = 1
        if ((row[0] == 'Florida') or (row[1] == 'Florida')):
            x_data[3] = 1
        if ((row[0] == 'Georgia') or (row[1] == 'Georgia')):
            x_data[4] = 1
        if ((row[0] == 'Kentucky') or (row[1] == 'Kentucky')):
            x_data[5] = 1
        if ((row[0] == 'LSU') or (row[1] == 'LSU')):
            x_data[6] = 1
        if ((row[0] == 'Mississippi') or (row[1] == 'Mississippi')):
            x_data[7] = 1
        if ((row[0] == 'Mississippi St.') or (row[1] == 'Mississippi St.')):
            x_data[8] = 1
        if ((row[0] == 'Missouri') or (row[1] == 'Missouri')):
            x_data[9] = 1
        if ((row[0] == 'South Carolina') or (row[1] == 'South Carolina')):
            x_data[10] = 1
        if ((row[0] == 'Tennessee') or (row[1] == 'Tennessee')):
            x_data[11] = 1
        if ((row[0] == 'Texas A&M') or (row[1] == 'Texas A&M')):
            x_data[12] = 1
        if ((row[0] == 'Vanderbilt') or (row[1] == 'Vanderbilt')):
            x_data[13] = 1
        y_data = [int(row[2]), int(row[3])]

        x_return[i] = x_data
        y_return[i] = y_data
        i += 1

    return x_return, y_return, size


index = 0
def next_batch(x_data, y_data, size):
    global index
    x_batch = [None]*batch_size
    y_batch = [None]*batch_size
    for i in range(batch_size):
        if index < size:
            x_batch[i] = tuple(x_data[index])
            y_batch[i] = tuple(y_data[index])
        else:
            index = 0
            x_batch[i] = tuple(x_data[index])
            y_batch[i] = tuple(y_data[index])
        index += 1
    return tuple(x_batch), tuple(y_batch)


def neural_network_model(data):
    hidden_1_layer = {'weights': tf.Variable(tf.random_normal([14, n_nodes_hl1])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))}

    hidden_2_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))}

    hidden_3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                      'biases': tf.Variable(tf.random_normal([n_classes]))}

    # (input_data * weights) + biases

    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.add(tf.matmul(l3, output_layer['weights']), output_layer['biases'])

    return output

# takes input data as parameter
def train_neural_network(x):
    prediction = neural_network_model(x)
    # OLD COST FUNCTION
    # cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=prediction))
    loss = tf.reduce_mean(tf.square(prediction - y))

    # default learning rate is 0.001
    optimizer = tf.train.AdamOptimizer().minimize(loss)

    # cycles of feedforward + backprop
    hm_epochs = 200

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        x_train, y_train, train_size = collect_data('training_data.csv')
        x_test, y_test, test_size = collect_data('testing_data.csv')
        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(train_size/batch_size)):
                epoch_x, epoch_y = next_batch(x_train, y_train, train_size)
                _, c = sess.run([optimizer, loss], feed_dict={x: epoch_x, y: epoch_y})
                epoch_loss += c
            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss', epoch_loss)

        correct = tf.equal(tf.arg_max(prediction, 1), tf.arg_max(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        print('Accuracy:', accuracy.eval({x: x_test, y: y_test}))
        #print("predictions", prediction.eval(feed_dict={x: x_test, y: y_test}, session=sess))

train_neural_network(x)
