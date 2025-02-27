from math import sqrt, pi

def get_user_inputs():
    """Prompts the user for moment, torque, and diameter values, then selects a stress concentration case."""
    moment_lbf_in = float(input("Input moment (lbf*in): ")) / 1000
    torque_lbf_in = float(input("Input torque (lbf*in): ")) / 1000
    diameter_in = float(input("Input diameter (in): "))

    def select_stress_case():
        """Displays stress concentration cases and gets user selection."""
        print("""Stress Concentrations:
        1. Wide Radius
        2. Sharp Radius
        3. Keyway
        4. R.R.G""")

        case_selection = int(input("Select Case: "))
        if case_selection in {1, 2, 3, 4}:
            return case_selection
        else:
            print("Invalid Case")
            return select_stress_case()

    stress_case = select_stress_case()
    return moment_lbf_in, torque_lbf_in, diameter_in, stress_case


def calculate_safety_factor(moment, torque, diameter, stress_case):
    """Calculates the safety factor for a shaft based on stress concentration factors."""
    notch_sensitivity_coefficient_a_s = 0.00538003
    notch_sensitivity_coefficient_a = 0.009601465
    ultimate_tensile_strength = 68

    # Stress concentration factors and notch radii for each case
    stress_concentration_factors = {
        1: (1.7, 1.5, 0.1 * diameter),
        2: (2.7, 2.2, 0.02 * diameter),
        3: (2.14, 3, 0.02 * diameter),
        4: (5, 3, 0.01)
    }

    if stress_case not in stress_concentration_factors:
        raise ValueError("Invalid stress concentration case")

    stress_concentration_factor, shear_stress_concentration_factor, notch_radius = stress_concentration_factors[
        stress_case]

    fatigue_stress_concentration_factor = 1 + (stress_concentration_factor - 1) / (
        1 + sqrt(notch_sensitivity_coefficient_a) / sqrt(notch_radius))
    fatigue_shear_stress_concentration_factor = 1 + (shear_stress_concentration_factor - 1) / (
        1 + sqrt(notch_sensitivity_coefficient_a_s) / sqrt(notch_radius))

    bending_stress_component = 2 * fatigue_stress_concentration_factor * moment
    torsional_stress_component = sqrt(3) * fatigue_shear_stress_concentration_factor * torque

    endurance_limit_prime = ultimate_tensile_strength / 2
    endurance_limit = 2 * ultimate_tensile_strength ** (-0.217) * 0.879 * diameter ** (-0.107) * endurance_limit_prime

    safety_factor = (pi * (diameter ** 3) / 16 *
        ((bending_stress_component / endurance_limit + torsional_stress_component / ultimate_tensile_strength) ** -1))

    print(f"Safety factor: {safety_factor:.3f}")


if __name__ == '__main__':
    while True:
        moment, torque, diameter, stress_case = get_user_inputs()
        calculate_safety_factor(moment, torque, diameter, stress_case)
