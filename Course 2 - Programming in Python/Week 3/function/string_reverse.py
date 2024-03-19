# str[start:stop:step]
# The syntax is [start:stop:step]. The start is the index of the first character 
# you want to include in the slice. 
# The stop is the index of the first character you don't want to include in the slice. 
# The step is the amount by which the index increases, and it can be negative.

trial = "reversal"
new_trial = trial[::-1] # This will reverse the string "reversal" to "lasrever"
print(new_trial) # lasrever