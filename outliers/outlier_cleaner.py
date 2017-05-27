#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    print "length pred: ", len(predictions)
    print "length ages: ", len(ages)
    print "length net: ", len(net_worths)
    print "pred: ", predictions[1]
    print "new: ", net_worths[1]
    print "diff: ", predictions[1] - net_worths[1]

    errors = []
    newArr = []
    counter = 0

    print "test: ", predictions[0][0]


    for pred in predictions:
        errors.append(abs(predictions[counter][0] - net_worths[counter][0]))
        newArr.append((ages[counter][0], net_worths[counter][0], abs(predictions[counter][0] - net_worths[counter][0])))
        counter += 1

    print newArr[57]
    newArr.sort(key=lambda x:x[2])

    for error in newArr:
        print "error: ", error[2]

    print "biggest: ", newArr[0:-10]

    arr = newArr[0:-9]


    cleaned_data = []

    ### your code goes here
    cleaned_data = arr


    return cleaned_data

