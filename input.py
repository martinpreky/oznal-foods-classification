import numpy as np

class Input:

    tokens = []


    train_string_input = []

    train_binary_input = []

    train_binary_result = []


    test_string_input = []

    test_binary_input = []

    test_binary_result = []


    test_binary_result_predicted = []

    def __init__(self,
                 tokens,
                 trainStrInput,
                 trainBinaryResult,
                 testStrInput,
                 testBinaryResult):
        print("...Input class constructor...")

        self.tokens = tokens
        print("...Tokens: %d" % (len(self.tokens)))

        self.train_string_input = trainStrInput
        print("...Train string input: %d" % (len(self.train_string_input)))

        self.train_binary_input = Input.to_binary(self.tokens, self.train_string_input)
        print("...Train binary input: %d" % (len(self.train_binary_input)))

        self.train_binary_result = trainBinaryResult
        print("...Train binary result: %d" % (len(self.train_binary_result)))


        self.test_string_input = testStrInput
        print("...Test string input: %d" % (len(self.test_string_input)))

        self.test_binary_input = Input.to_binary(self.tokens, self.test_string_input)
        print("...Test binary input: %d" % (len(self.test_binary_input)))

        self.test_binary_result = testBinaryResult
        print("...Test binary result: %d" % (len(self.test_binary_result)))

    def message_out(self):
        print("------- Message report -------")

        # print("Malo vyjst: ")
        # print(self.test_binary_result)
        # print("Vyslo: ")
        # print("[" + ', '.join(map(str, self.test_binary_result_predicted)) + "]")

        # TODO: Compute recall and precision

        right_result = self.get_number_of_right_results()
        accuracy = right_result / len(self.test_binary_result)

        print("Presnost relativne: %.2f" % (accuracy))
        print("Presnost absolutne: %d z %d" % (right_result, len(self.test_binary_result)) )

    def get_number_of_right_results(self):
        a = np.array(self.test_binary_result)
        b = np.array(self.test_binary_result_predicted)
        number_of_right_results = np.sum(a == b)

        return number_of_right_results


    @staticmethod
    def to_binary(tokens, stringInputs):
        result = []
        for input in stringInputs:
            partialBinaryInput = [0] * len(tokens)

            for token in input:
                partialBinaryInput[tokens.index(token)] = 1

            result.append(partialBinaryInput)

        return result