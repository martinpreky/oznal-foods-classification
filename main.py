from sklearn.neural_network import MLPClassifier
import sampleData
import csvData
import dbData

#hovno = sampleData.get_input_instance()
#hovno = csvData.get_input_instance()
hovno = dbData.get_input_instance('items_kfold_1')

# X = hovno.train_binary_input
# y = hovno.train_binary_result
#
# print("...Neural network init...")
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1, max_iter=5000)
#
# print("...Neural network train...")
# clf.fit(X, y)
#
# print("...Neural network predict...")
# hovno.test_binary_result_predicted = clf.predict(hovno.test_binary_input)
#
# hovno.message_out()
