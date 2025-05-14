import numpy as np

def solution(A, B):
    A_np = np.array(A)
    
    B_np = np.array(B)
    
    return (A_np + B_np).tolist()