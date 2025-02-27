# MAE 4300 Machine Design Class
Code for the Machine Design Final Project: Gear box design. 
## Code Sections
Brief descriptions for all the different files
### shaft_design.py
Basic code for calculating the Goodman fatigue factor of safety. 
```python
get_user_inputs()
```
Is a function that gets the variables for use in the calcution function it returns 
```python
 return moment_lbf_in, torque_lbf_in, diameter_in, stress_case
```
The main function is 
```python 
calculate_safety_factor(moment, torque, diameter, stress_case)
```
The parameters are intended to be in the lbf and in.

The 4 stress concentration cases are:
1. Wide Radius
2. Sharp Radius
3. Keyway
4. R.R.G