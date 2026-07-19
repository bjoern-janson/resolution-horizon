import unittest
from instrument import StructuralHorizonEstimator

class TestStructuralDiscoveryFramework(unittest.TestCase):
    """
    Automated verification suite testing paired curve phase shifts,
    misresolution invariants, and directional derivative signs.
    """

    def setUp(self):
        # Nominal system parameters
        self.N = 100000
        self.sigma = 0.02
        self.estimator = StructuralHorizonEstimator(N=self.N, sigma=self.sigma)
        self.metrics = self.estimator.evaluate_horizon(max_k=6, lambda_N=1.0)

    def test_coupled_phase_transition_geometries(self):
        """Verifies the three-regime paired curve fingerprint profile."""
        k_star = self.metrics["k_star"]
        k_star_idx = k_star - 1

        # Region I (Discovery): Compression and overall efficiency must rise monotonically
        for idx in range(k_star_idx):
            if idx > 0:
                self.assertGreater(
                    self.metrics["delta_L"][idx], 
                    self.metrics["delta_L"][idx - 1],
                    "Regime I Violation: Invariant compression failed to increase monotonically."
                )
                self.assertGreater(
                    self.metrics["eta"][idx], 
                    self.metrics["eta"][idx - 1],
                    "Regime I Violation: Overall structural efficiency failed to ascend toward the horizon."
                )

        # Region III (Misresolution): Compression must fall, ambiguity must rebound
        for idx in range(k_star_idx + 1, len(self.metrics["k_axis"])):
            self.assertLess(
                self.metrics["delta_L"][idx], 
                self.metrics["delta_L"][idx - 1],
                "Regime III Violation: Compression curve failed to decay past horizon."
            )
            self.assertGreater(
                self.metrics["C_G"][idx], 
                self.metrics["C_G"][idx - 1],
                "Regime III Violation: Symmetry uncertainty failed to inflate/rebound past horizon."
            )

    def test_resource_response_surface_signs(self):
        """Validates directional horizon responses under noise perturbations (dk*/dσ <= 0)."""
        high_noise_estimator = StructuralHorizonEstimator(N=self.N, sigma=0.45)
        high_noise_metrics = high_noise_estimator.evaluate_horizon(max_k=6, lambda_N=1.0)
        
        self.assertLessEqual(
            high_noise_metrics["k_star"], 
            self.metrics["k_star"],
            "Response Surface Violation: High noise failed to contract the optimal horizon boundary."
        )

if __name__ == "__main__":
    unittest.main()
