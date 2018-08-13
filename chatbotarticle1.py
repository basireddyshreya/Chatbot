def evaluateRecall(y, yTest, k=1):
	numExamples = float(len(y))
	numCorrect = 0
	for predictions, label in zip(y, yTest):
		if label in predictions[:k]:
			numCorrect+=1
	return numCorrect/numExamples