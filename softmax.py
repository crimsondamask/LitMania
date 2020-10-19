import numpy as np

def softmax(vector):
    
    # Calculate e^x for each x in your vector where e is Euler's
    # number (approximately 2.718)
    exponentVector = np.exp(vector)

    # Add up the all the exponentials
    sumOfExponents = np.sum(exponentVector)

    # Divide every exponent by the sum of all exponents
    softmax_vector = exponentVector / sumOfExponents

    return softmax_vector


if __name__ == "__main__":
    print(softmax((0,)))
