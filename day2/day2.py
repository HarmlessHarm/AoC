import os

INPUT = "day2.input"
# INPUT = "day2.test"
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)

choice_score = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

heOps = ["A", "B", "C"]
meOps = ["X", "Y", "Z"]

""" 
SCORE TABLE
 
|h\m| X | Y | Z |
| A | T | W | L |
| B | L | T | W |
| C | W | L | T |

"""

outcome_score = [
	[3, 6, 0],
	[0, 3, 6],
	[6, 0, 3]
]

""" 
CHOICE TABLE
 
|h\m| L | T | W |
| A | C | A | B |
| B | A | B | C |
| C | B | C | A |

"""

choice_table = [
	["C", "A", "B"], # A
	['A', 'B', "C"], # B
	['B', 'C', 'A']  # C
]

puz2_score = {
	"X": 0,
	"Y": 3,
	"Z": 6,
	"A": 1,
	"B": 2,
	"C": 3
}

def score1(he, me):
	heI = heOps.index(he)
	meI = meOps.index(me)
	return outcome_score[heI][meI] + choice_score[me]

def score2(he, me):
	heI = heOps.index(he)
	meI = meOps.index(me)
	choice = choice_table[heI][meI]
	return puz2_score[choice] + puz2_score[me]



def day2():
	with open(IN_PATH, 'r') as file:
		total_score_puz1 = 0
		total_score_puz2 = 0
		for line in file.readlines():
			he, me = line.split()

			total_score_puz1 += score1(he, me)

			total_score_puz2 += score2(he, me)
			
	
	print("total score puzzle 1", total_score_puz1)
	print("total score puzzle 2", total_score_puz2)

if __name__ == "__main__":
	day2()

			
