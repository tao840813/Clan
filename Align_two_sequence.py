from Bio.pairwise2 import format_alignment
from Bio import pairwise2


def ScoreCalcation(alignmentsAction):
    matches = alignmentsAction[0][2]
    seq_length = min(len(alignmentsAction[0][0]), len(alignmentsAction[0][1]))
    return (matches / seq_length) * 100


def Align2Seq(Seq1: str, Seq2: str):
    alignmentsAction = pairwise2.align.globalxx(Seq1, Seq2)
    alignmentScore = ScoreCalcation(alignmentsAction)
    return alignmentScore

