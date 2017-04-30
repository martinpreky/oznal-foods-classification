from sklearn.neural_network import MLPClassifier
import sampleData
import csvData
import dbData
from sklearn.metrics import precision_recall_curve
import sys

#hovno = sampleData.get_input_instance()
#hovno = csvData.get_input_instance()

for k in range(1,5):
    for b in [True, False]:
        print("")
        print("")
        print("========= new iteration ===========")
        print("kfold: " + str(k))
        print("include recipes: " + str(b))
        sys.stdout.flush()
        hovno = dbData.get_input_instance('items_kfold_'+str(k), b)

        X = hovno.train_binary_input
        y = hovno.train_binary_result

        print("...Neural network init...")
        clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(10, 2), random_state=1, max_iter=500, verbose=True)

        print("...Neural network train...")
        clf.fit(X, y)

        print("...Neural network predict...")
        hovno.test_binary_result_predicted = clf.predict(hovno.test_binary_input)

        precision, recall, thresholds = precision_recall_curve(hovno.test_binary_result, hovno.test_binary_result_predicted)

        print(precision)
        print(recall)
        print(thresholds)

        hovno.message_out()
