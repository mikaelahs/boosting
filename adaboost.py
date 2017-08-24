import numpy as np
import argparse
from sklearn.tree import DecisionTreeClassifier

def parse_argument():
    """
    Code for parsing arguments
    """
    parser = argparse.ArgumentParser(description='Parsing a file.')
    parser.add_argument('--train', nargs=1, required=True)
    parser.add_argument('--test', nargs=1, required=True)
    parser.add_argument('--numTrees', nargs=1, required=True)
    args = vars(parser.parse_args())
    return args


def adaboost(X, y, num_iter):
    """Given an numpy matrix X, a array y and num_iter return trees and weights 
   
    Input: X, y, num_iter
    Outputs: array of trees from DecisionTreeClassifier
             trees_weights array of floats
    Assumes y is in {-1, 1}^n
    """
    trees = []
    trees_weights = []
    # your code here
    return trees, trees_weights


def adaboost_predict(X, trees, trees_weights):
    """Given X, trees and weights predict Y

    assume Y in {-1, 1}^n
    """
    # your code here
    return Yhat


def parse_spambase_data(filename):
    """ Given a filename return X and Y numpy arrays

    X is of size number of rows x num_features
    Y is an array of size the number of rows
    Y is the last element of each row.
    """
    # your code here
    return X, Y

def new_label(Y):
    """ Transforms a vector od 0s and 1s in -1s and 1s.
    """
    return [-1. if y == 0. else 1. for y in Y]

def old_label(Y):
    return [0. if y == -1. else 1. for y in Y]

def accuracy(y, pred):
    return np.sum(y == pred) / float(len(y)) 

def main():
    """
    This code is called from the command line via
    
    python adaboost.py --train [path to filename] --test [path to filename] --numTrees 
    """
    args = parse_argument()
    train_file = args['train'][0]
    test_file = args['test'][0]
    num_trees = int(args['numTrees'][0])
    print train_file, test_file, num_trees

    # your code here

    ## here print accuracy and write predictions to a file
    acc_test = accuracy(Y_test, Yhat_test)
    acc = accuracy(Y, Yhat)
    print("Train Accuracy %.4f" % acc)
    print("Test Accuracy %.4f" % acc_test)

if __name__ == '__main__':
    main()

