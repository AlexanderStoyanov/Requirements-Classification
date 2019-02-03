# Requirements Classification

## Topics
Machine Learning, Natural Language Processing, Text Classification

## Background
In order to develop quality software, software engineers derive requirements for that software from various resources like charts, graphs, or written natural language. It quickly becomes time-consuming the bigger the software is because requirements need to be split into functional and non-functional, and non-functional to be split further in many subcategories.

This project is created to help automate classification of natural-language-written requirements into right categories in order to save resources needed to do this redundant and boring task.

## Overview
Members:
- Alexander Stoyanov
- Sundeep Singh
- Anthony Baichulall
- Jorge Brito
- Jacob Lee

Technology used:
- Docker
- Tensorflow (Python 2)

Dependencies:
- Keras
- Scikit
- Numpy
- NLTK
- matplotlib
- json

## Implementation
There are two part to this project:
1. Classification of requirements into two (2) categories, functional and non-functional
2. Classification of non-functional requirements into four (4) different categories

## Notes
Part 2 implemented in two ways:
1. Using binary classifier on all four classes separately
2. Using multiclass classifier

In some cases binary classifiers noted to perform better than their multiclass alternatives

## References
- https://github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_text_classification.ipynb
- https://developers.google.com/machine-learning/guides/text-classification/
