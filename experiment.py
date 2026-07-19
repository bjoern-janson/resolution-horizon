import numpy as np
from instrument import StructuralHorizonEstimator

def run_regularization_bypass():
    """
    Executes a controlled intervention on the smoothing hyperparameter lambda_N
    to distinguish between an Observer-Limited and a Structure-Limited horizon.
    """
    print("[RUNNING CAUSAL INTERVENTION: REGULARIZATION BYPASS]")
    print("----------------------------------------------------------------------")
    print("Fixing physical constraints: N=100000, sigma=0.04, B_r=10.0")
    
    # Environmental constants
    N = 100000
    sigma = 0.04
    
    # Sweep observer regularizers
    lambda_baseline = 1.0
    lambda_perturbed = 8.0
    
    engine_base = StructuralHorizonEstimator(N=N, sigma=sigma)
    
    # Measure Baseline Horizon
    res_base = engine_base.evaluate_horizon(max_k=6, lambda_N=lambda_baseline)
    print(f"\nBaseline Observer (lambda_N = {lambda_baseline:.1f}):")
    print(f" -> Measured Horizon k*: {res_base['k_star']}")
    print(f" -> Max Efficiency eta : {res_base['eta'][res_base['k_star']-1]:.3f}")
    
    # Measure Perturbed Horizon
    res_pert = engine_base.evaluate_horizon(max_k=6, lambda_N=lambda_perturbed)
    print(f"\nPerturbed Observer (lambda_N = {lambda_perturbed:.1f}):")
    print(f" -> Measured Horizon k*: {res_pert['k_star']}")
    print(f" -> Max Efficiency eta : {res_pert['eta'][res_pert['k_star']-1]:.3f}")
    
    print("\n----------------------------------------------------------------------")
    print("[CAUSAL DIAGNOSTIC FORK EVALUATION]")
    if res_base['k_star'] != res_pert['k_star']:
        print("Outcome: Case A — OBSERVER-LIMITED HORIZON detected.")
        print("Instability envelope V(k) shifts the operational boundary.")
    else:
        print("Outcome: Case B — STRUCTURE-LIMITED HORIZON detected.")
        print("The physical system dynamics or invariant class dominates the ceiling.")
    print("----------------------------------------------------------------------")

if __name__ == "__main__":
    run_regularization_bypass()
