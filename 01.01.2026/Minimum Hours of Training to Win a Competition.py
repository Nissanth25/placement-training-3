class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        total_energy_needed = sum(energy) + 1
        energy_training = max(0, total_energy_needed - initialEnergy)

        extra =0 
        exp_training = 0 

        for i in experience :
            if initialExperience <= i :
                extra = i - initialExperience +1 
                exp_training += extra
                initialExperience += extra
            initialExperience += i
        return energy_training + exp_training            
                
        
