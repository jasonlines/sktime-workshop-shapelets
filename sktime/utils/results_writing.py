import os
from sklearn.metrics import accuracy_score as acc


def write_results_to_uea_format(output_path, classifier_name, dataset_name, actual_class_vals,
                                predicted_class_vals, split='TEST', resample_seed=0, actual_probas=None, second_line="N/A"):

    if len(actual_class_vals) != len(predicted_class_vals):
        raise IndexError("The number of predicted class values is not the same as the number of actual class values")

    try:
        os.makedirs(str(output_path)+"/"+str(classifier_name)+"/Predictions/" + str(dataset_name) + "/")
    except os.error:
        pass  # raises os.error if path already exists

    if split == 'TRAIN' or split == 'train':
        train_or_test = "train"
    elif split == 'TEST' or split == 'test':
        train_or_test = "test"
    else:
        raise ValueError("Unknown 'split' value - should be TRAIN/train or TEST/test")

    file = open(str(output_path)+"/"+str(classifier_name)+"/Predictions/" + str(dataset_name) +
                "/"+str(train_or_test)+"Fold"+str(resample_seed)+".csv", "w")

    correct = acc(actual_class_vals, predicted_class_vals)

    # the first line of the output file is in the form of:
    # <classifierName>,<datasetName>,<train/test>
    file.write(str(classifier_name)+"," + str(dataset_name) + ","+str(train_or_test)+"\n")

    # the second line of the output is free form and classifier-specific; usually this will record info
    # such as build time, paramater options used, any constituent model names for ensembles, etc.
    file.write(str(second_line)+"\n")

    # the third line of the file is the accuracy (should be between 0 and 1 inclusive). If this is a train
    # output file then it will be a training estimate of the classifier on the training data only (e.g.
    # 10-fold cv, leave-one-out cv, etc.). If this is a test output file, it should be the output
    # of the estimator on the test data (likely trained on the training data for a-priori parameter optimisation)

    file.write(str(correct)+ "\n")

    # from line 4 onwards each line should include the actual and predicted class labels (comma-separated). If
    # present, for each case, the probabilities of predicting every class value for this case should also be
    # appended to the line (a space is also included between the predicted value and the predict_proba). E.g.:
    #
    # if predict_proba data IS provided for case i:
    #   actual_class_val[i], predicted_class_val[i],,prob_class_0[i],prob_class_1[i],...,prob_class_c[i]
    #
    # if predict_proba data IS NOT provided for case i:
    #   actual_class_val[i], predicted_class_val[i]
    for i in range(0, len(predicted_class_vals)):
        file.write(str(actual_class_vals[i]) + "," + str(predicted_class_vals[i]))
        if actual_probas is not None:
            file.write(",")
            for j in actual_probas[i]:
                file.write("," + str(j))
            file.write("\n") #TODO BUG new line is written only if the probas are provided!!!!

    file.close()


if __name__ == "__main__":
    actual = [1,1,2,2,1,1,2,2]
    preds = [1,1,2,2,1,2,1,2]
    probas = [
        [1.0, 0.0],
        [0.9, 0.1],
        [0.4, 0.6],
        [0.1, 0.9],
        [0.9, 0.1],
        [0.4, 0.6],
        [0.7, 0.3],
        [0.2, 0.8],
    ]

    write_results_to_uea_format(
        output_path="../exampleResults",
        classifier_name="dummy_classifier",
        dataset_name="banana_point",
        actual_class_vals=actual,
        predicted_class_vals=preds,
        split='TEST',
        resample_seed=0,
        actual_probas=probas,
        second_line="buildTime=100000,num_dummy_things=2"
    )
