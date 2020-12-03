class FitnessTracker:
    """ calls class FitnessTracker"""
    def __init__():
        """Creates attributes and stores the information from the parameters 
            Args: 
                age(int): the number of the person's age
                gender (str): the name of the gender
                weight(int): the weight of. user 
        """
        self.age
        self.gender
        self.weight
        
    def HowOften(self):
        """
        This function calculates how often the user should exercise based on age, gender and weight
        
        Returns(int): Returns the days to workout in a week
        """
        #Gain, maintain, or lose weight (goal)
        
    def CalorieCalculator(self):
        """
        Calculates the number of calories depending on the amount entered based on the calorie calculation.
        Args:
        Raises: ValueError: Raises a value error if user inputs a negative number.
        Returns(int): the number of calories based on bmi  
        """
        w = input("Weight: ")
        h = input("Height: ")
        a = input("Age: ")
        gender = input("Gender: ")

        if gender == "female":
            weight = 10 * self.weight
            height = 6.25 * self.height
            age = 5 * self.age
            bmr = ((weight + height) - age) + 5        
        elif gender == "male": 
            weight = 10 * self.weight
            height = 6.25 * self.height
            age = 5 * self.age
            bmr = ((weight + height) - age) - 161
    #bmi = (weight / (height * height) * 703))
    #  return bmi
        if bmr < 18.5:
            return "underweight"
        elif bmr == 24:
            return "normal weight"
        elif bmr > 25:
            return "overweight"
    
    def WorkoutRegime(self, filename):
        """
        This function provides three types of workout regimes based on user goals.
        Args:
            filename: Path to the file
        Returns(dict): A dictionary whose keys are the workouts and values are the repitions
           
        """
        #Three regimes depending on gain, maintain or lose
        #Different interval based on three regimes
        
    def Diet(self, filename):
        """
        This function provides the type of diet based on user goals
        Args:
            filename: Path to the file
        Returns(dict): Returns a dictionary with weekdays as keys and diet information as a list of values
        """
        
        #Macro ratios based on gaining, maintaining, or losing weight, along with the calories
        #Ratio of calories you want to be protein, carbs, and fat
        #Text file of diets
        
    def Cardio(self, filename):
        """
        This function provides the amount of cardio as required by user goals
        Args:
            filename: Path to the file
        Returns(int): The minutes of cardio based on user goals
        """
        
        #Amount of cardio based on ratio
        #One cardio workout per parameter
        
    def Cooldown(self):
        """
        This fucntion provides the restdays that a user should take based on their goals and how often they workout
        
        Return(int): the number of rest/cooldown days
     
        """
        
    
    def Tips(self, filename):
        """
        This function provides user with motivational/usefull fitness tips
        
        Args:   
            Filename: the path to the file
        Returns:
            a quote from the opened file based on the three workout regime
        """
    
        
