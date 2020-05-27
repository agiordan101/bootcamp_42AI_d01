from numbers import Real


class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if (not isinstance(coefs, list) or
           not isinstance(words, list)):
            print("Arguments need to be List")
            return -1
        if len(coefs) != len(words):
            print("Arguments length need to be same")
            return -1
        result = zip(coefs, words)
        sum = 0
        for t in result:
            if (not isinstance(t[0], Real) or
               not isinstance(t[1], str)):
                print("Arguments need to be List of Real and String")
                return -1
            sum += t[0] * len(t[1])
        return sum

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if (not isinstance(coefs, list) or
           not isinstance(words, list)):
            print("Arguments need to be List")
            return -1
        if len(coefs) != len(words):
            print("Arguments length need to be same")
            return -1
        sum = 0
        for i, coef in enumerate(coefs, 0):
            if (not isinstance(coef, Real) or
               not isinstance(words[i], str)):
                print("Arguments need to be List of Real and String")
                return -1
            sum += coef * len(words[i])
        return sum


words = ["a", "un", "six", "sept", "trois", "quatre"]
coefs = [1, 2, 3, 4, 5, 6]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))

words = ["a", "un", "six", "sept", "trois", "quatre"]
coefs = [1, 2, 3, 4, 5, 6, 7]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))

words = ["a", "un", "six", "sept", "trois", "quatre"]
coefs = [1, 2, 3, 4, 5, "six"]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))

words = [0, "un", "six", "sept", "trois", "quatre"]
coefs = [1, 2, 3, 4, 5, 6]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))
