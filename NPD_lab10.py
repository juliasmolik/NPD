import numpy as np


def double_size(path_to_file):
    """
    Function that checks which object has increased in
    size at least twice in time observation
    :param path_to_file: path to the file containing the data
    """

    data = np.load(path_to_file)
    outputs = data["outputs"]
    result = []
    for i in range(len(outputs)):
        if float(outputs[i][0])*2 <= float(outputs[i][-1]):
            result.append(i)
            print("The last observation of the object {} is at least twice the size of the first observation of the same object".format(i))
    print("A total of {} objects have at least doubled their size over time".format(len(result)))


double_size('./lab10/sample_treated.npz')