import numpy
import os

def CondEntropy(j, matrix):
    jEntropy = 0
    jAllOccurrences = sum([number for number in matrix])[j]
    for i in range(256):
        iAfterJOccurence = matrix[i][j]
        if iAfterJOccurence != 0:
            jEntropy += iAfterJOccurence * numpy.log2(jAllOccurrences/iAfterJOccurence)   #jEntropy += iAfterJOccurence/jAllOccurrences * numpy.log2(jAllOccurrences/iAfterJOccurence)

    return jEntropy


def entropy(filename):
    charsMatrix = numpy.zeros((256,256), dtype=int)
    # przyjmijmy że charsMatrix[i][j] to będzie prawdopodobieństwo wystąpienia i-tego znaku po j-tym

    # path = input("Podaj sciezke do pliku: ")
    with open(filename, 'rb') as f:
        prevChar = 0
        content = f.read()
        for currChar in content:
            charsMatrix[currChar][prevChar] += 1
            prevChar = currChar

    condEnt = 0
    entropy = 0
    allOccurrences = sum(sum(number for number in charsMatrix))

    for j in range(256):
        jOccurrences = sum([number for number in charsMatrix][j])

        if jOccurrences != 0 and allOccurrences !=0:
            condEnt += 1/allOccurrences * CondEntropy(j, charsMatrix)   #condEnt += jOccurrences/allOccurrences * CondEntropy(j, charsMatrix)
            entropy += jOccurrences/allOccurrences * numpy.log2(allOccurrences/jOccurrences)

    print("Entropia warunkowa: ",condEnt)
    print("Entropia: ",entropy)
    print("Entropia różni się od entropii warunkowej o: " + str(entropy-condEnt))
    print()

if __name__ == '__main__':
    for file in os.listdir('.'):
        if file.endswith('.txt') or file.endswith('.bin'):
            print(file)
            entropy(file)
