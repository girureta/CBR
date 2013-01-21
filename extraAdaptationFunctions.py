""" Extra adaptation functions can be defined in this library by the user.
    For doing so, just use the template provided in the adaptationFunction4.
    More adaptation formulas can be defined by copy-paste the first template.
    In addition, the code refering to those functions should be uncommented
    in the first function. The formulas can be called from the main interface
    by introducing their identification number as "method" 
"""

import chess


def adapt(problemPlay, retrievedCases, method, consist=True):
    if method == 4:
        sol = adaptationFunction4(problemPlay, retrievedCases, method)
    # elif method == 5:
    #     sol = adaptationFunction5(problemPlay, retrievedCases, method)
    # elif method == 6:
    #     sol = adaptationFunction6(problemPlay, retrievedCases, method)
    # elif method == 7:
    #     sol = adaptationFunction7(problemPlay, retrievedCases, method)
    # elif method == 8:
    #     sol = adaptationFunction8(problemPlay, retrievedCases, method)
    # elif method == 9:
    #     sol = adaptationFunction9(problemPlay, retrievedCases, method)
    else:
        sol = None

    if consist and sol != None:
        return chess.findClosestConsistentSolution(problemPlay, sol)



def adaptationFunction4(problemPlay, retrievedCases, method, consist):
    problem = {'WKingX': problemPlay.data[0],
               'WKingY': problemPlay.data[1],
               'WRookX': problemPlay.data[2],
               'WRookY': problemPlay.data[3],
               'BKingX': problemPlay.data[4],
               'BKingX': problemPlay.data[5],
               }

    cSol = [{'WKingX': c[0], 'WKingY': c[1], 'WRookX': c[2], 'WRookY': c[3], 
            'BKingX': c[4], 'BKingX': c[5]} for c in retrievedCases.solution]

    cP = [{'WKingX': c[0], 'WKingY': c[1], 'WRookX': c[2], 'WRookY': c[3], 
          'BKingX': c[4], 'BKingX': c[5]} for c in retrievedCases.currentPlay]          

    sol = {'WKingX': 0, 'WKingY': 0, 'WRookX': 0,
           'WRookY': 0, 'BKingX': 0, 'BKingX': 0}

    # Formulas can be easily defined using the folowing notation:
    #  problem['WKingX'] is the X coordinate of white king
    #  cP[i]['BKingY'] is the Y coordinate of black king of the ith 
    #                     retrieved case problem
    #  cSol[i]['WRookX'] is the X coordinate of white rook of the ith
    #                     retrieved case solution
    #  sol['BKingY'] is the Y coordinate of black king in the adapted solution

    # An example: 
    # sol['WkingY'] = round(0.8 * cSol[0]['WkingX'] + 0.2 * cSol[1]['WKingX'])

    solution = [sol['WKingX'], sol['WKingY'], sol['WRookX'], sol['WRookY'],
                                                sol['BKingX'], sol['BKingY'],]

    # return solution
    return None


def adaptationFunction5(problemPlay, retrievedCases, method, consist):
    return None


def adaptationFunction6(problemPlay, retrievedCases, method, consist):
    return None


def adaptationFunction7(problemPlay, retrievedCases, method, consist):
    return None


def adaptationFunction8(problemPlay, retrievedCases, method, consist):
    return None

def adaptationFunction9(problemPlay, retrievedCases, method, consist):
    return None