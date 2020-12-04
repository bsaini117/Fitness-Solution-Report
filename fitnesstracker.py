import requests
import time
import sys
import pandas as pd
from tabulate import tabulate
from bs4 import BeautifulSoup
import random
from argparse import ArgumentParser

class FitnessSolutionReport:
    """ calls class FitnessTracker
        Attributes: 
            age (int): users age
            gender (str): the users gender
            weight (float): The user's weight in pounds
            height (float): The user's height in inches
            objective (str): Whether the user wants to gain, maintain, or lose weight
            how_often (int): How many days the user wants to work out (minimum of 3 and maximum of 6
    """
    def __init__(self, age, gender, weight, height, objective, how_often):
        """
        This class provides a comprehensive fitness report based on user's objective to lose, mantain and gain weight
        Creates attributes and stores the information from the parameters 
        Args: 
            age (int): The user's age
            gender (str): The user's gender
            weight (float): The user's weight in pounds
            height (float): The user's height in inches
            objective (str): Whether the user wants to gain, maintain, or lose weight
            how_often (int): How many days the user wants to work out (minimum of 3 and maximum of 6)
        """
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.objective = objective
        self.how_often = how_often
        
    
        
    def CalorieCalculator(self):
        """
        Calculates the number of calories a person should have daily and bmi depending on users inputs
            
        Returns:
            f-string (str): String containing infomration about the users BMI, BMR, and its prediction
            bmi (float): The BMI as a number from the user's input based on the formula
            bmr (float): The amount of calorie intake the user should have daily based on inputs and the BMR formula
            prediction (str): Statement of wheather a user is underweight, normal weight, or over weight
            depending on inputs, gender and its corresponding formula calculation.   
        """
        
        d_ret={"bmr":0, "bmi":0}
        p_bmi = (self.weight/(self.height*self.height))*int(703)

        if self.gender == "female":
            weight = 10 * float(self.weight)
            height = 6.25 * float(self.height)
            age = 5 * int(self.age)
            bmr = ((weight + height) - age) + 5 
               
        elif self.gender == "male": 
            weight = 10 * float(self.weight)
            height = 6.25 * float(self.height)
            age = 5 * int(self.age)
            bmr = ((weight + height) - age) - 161
            
        d_ret["bmr"]=bmr
        d_ret["bmi"]=p_bmi
        
        if p_bmi < 18.5:
            return "underweight"
        elif p_bmi > 18.5 and p_bmi <25:
            return "normal weight"
        elif p_bmi > 25:
            return "overweight"
        
        return d_ret
       
       
    def WorkoutRegime(self):
        """
        This function provides three types of workout regimes based on user goals.
        Args:
            filename: Path to the file
        Returns(dict): A dictionary whose keys are the workouts and values are the repitions
           
        """
        #FOR WORKING OUT THREE DAYS
        if self.how_often == 3:
            if self.objective == "maintain":
                
                res = requests.get("https://www.jefit.com/routines/72415/wedding-thicc")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))

            elif self.objective == "gain":
                
                res = requests.get("https://www.jefit.com/routines/199187/5x5-split-routine-3-day")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))
        
            elif self.objective == "lose":
                
                res = requests.get("https://www.jefit.com/routines/86376/3-day-for-running")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))        
    
     #FOR WORKING OUT FOUR DAYS
        if self.how_often == 4:
            if self.objective == "maintain":
                
                res = requests.get("https://www.jefit.com/routines/70021/masunas-baseball-off-season-program-weeks-1-4")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))
                print(tabulate(df[3], headers='keys', tablefmt='psql'))

            elif self.objective == "gain":
            
                res = requests.get("https://www.jefit.com/routines/195547/hipertrofia-de-todo-el-cuerpo")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))
                print(tabulate(df[3], headers='keys', tablefmt='psql'))     

            elif self.objective == "lose":
                
                res = requests.get("https://www.jefit.com/routines/112064/lean-and-large")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))
                print(tabulate(df[3], headers='keys', tablefmt='psql'))    
  
     #FOR WORKING OUT FIVE DAYS
        if self.how_often == 5:
            if self.objective == "maintain":
                
                res = requests.get("https://www.jefit.com/routines/101459/bikini-prep-schedule-4")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))
                print(tabulate(df[3], headers='keys', tablefmt='psql'))
                print(tabulate(df[4], headers='keys', tablefmt='psql'))

            elif self.objective == "gain":
                
                res = requests.get("https://www.jefit.com/routines/195713/scovs-routine")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))
                print(tabulate(df[3], headers='keys', tablefmt='psql'))
                print(tabulate(df[4], headers='keys', tablefmt='psql'))    

            elif self.objective == "lose":
                
                res = requests.get("https://jefit.com/routines/107113/rajata-workout")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))
                print(tabulate(df[3], headers='keys', tablefmt='psql'))
                print(tabulate(df[4], headers='keys', tablefmt='psql'))                     

     #FOR MEN WORKING OUT SIX DAYS
        if self.how_often == 6:
            if self.objective == "maintain":
                
                res = requests.get("https://www.jefit.com/routines/33778/swimming-and-strength-101")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))
                print(tabulate(df[3], headers='keys', tablefmt='psql'))
                print(tabulate(df[4], headers='keys', tablefmt='psql'))
                print(tabulate(df[5], headers='keys', tablefmt='psql'))

            elif self.objective == "gain":
                
                res = requests.get("https://www.jefit.com/routines/111830/6-day-push-pull-leg-workout-for-body-recomposition")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))
                print(tabulate(df[3], headers='keys', tablefmt='psql'))
                print(tabulate(df[4], headers='keys', tablefmt='psql'))
                print(tabulate(df[5], headers='keys', tablefmt='psql'))
        
            elif self.objective == "lose":
                
                res = requests.get("https://www.jefit.com/routines/103151/fat-loss-workout")
                soup = BeautifulSoup(res.content,'lxml')
                table = soup.find_all('table', class_='InnerTable')
                df = pd.read_html(str(table))
                print(tabulate(df[0], headers='keys', tablefmt='psql'))
                print(tabulate(df[1], headers='keys', tablefmt='psql'))
                print(tabulate(df[2], headers='keys', tablefmt='psql'))
                print(tabulate(df[3], headers='keys', tablefmt='psql'))
                print(tabulate(df[4], headers='keys', tablefmt='psql'))
                print(tabulate(df[5], headers='keys', tablefmt='psql'))

        #Three regimes depending on gain, maintain or lose
        #Different interval based on three regimes
        
    def Diet(self):
        '''
        This function scrapes website for the diet depending on the objective of
        the user.It provides with the recipees and the links to those recipees
        Args: 
            Self: self.objective finds out if the user want to gain or loose weight
        Returns:
            wl_recipees(dict): A dictionary of weight loss recipees and their links
            wg_breakfast_recipees(dict): A dictionary of weight gain breakfast recipees
            wg_lunch_recipees(dict): A dictionary of weight gain lunch recipees
            wg_dinner_recipees(dict): A dictionary of weight gain dinner recipees
        '''
    
        #If user objective is to loose weight
        if self.objective == "lose":
        
            #WEIGHT LOSS
            weight_loss_page = requests.get("https://www.skinnytaste.com/7-day-weight-loss-meal-plan-march-9-15/")
            soup_wl = BeautifulSoup(weight_loss_page.text, "html.parser")
            wl_anchors = soup_wl.findAll("a")
            wl_recipee_lst = []
            i = 139
            while i < 165:
                wl_recipee_links = wl_anchors[i]["href"]
                wl_recipee_lst.append(wl_recipee_links)
                i += 1

            #A list of Weight loss recipees
            #print(wl_recipee_lst)
            #Getting rid of duplicate links
            wl_recipee_lst = list(dict.fromkeys(wl_recipee_lst))
            #print(wl_recipee_lst)
    
            wl_recipee_name = ['Tamarind-Chipotle Steak Nachos','Salmon Stir-fried Noodles','Creamy Ahi Tuna Pasta',
                'Steak Gyros','Butternut Squash and Chicken Pad Thai','Honey Sriracha Turkey Meatballs',
                'Coconut Crusted Fish Tacos','Healthy Bolognese',
                'Lean Pulled Pork','Salmon Chowder']
            wl_recipees = dict(zip(wl_recipee_name, wl_recipee_lst))
            return(wl_recipees)
        
        #if user objective is to gain weight   
        elif self.objective == "gain":
    

        
            #WEIGHT GAIN
            #Using request to get recipees
            weight_gain_page = requests.get("https://www.trifectanutrition.com/blog/meal-prep-for-weight-gain-your-complete-muscle-building-diet-plan")
            #Creating a beautifull soup object
            soup_wg = BeautifulSoup(weight_gain_page.text, "html.parser")
            #Finding all the anchor tags
            wg_anchors = soup_wg.findAll("a")
            #print(wg_anchors[68:101]["href"])


            #GETTING RECIPEE LINKS
    
            #Breakfast
            wg_breakfast_lst = []
            #The required information is between 68 and 79 line
            i = 68
            while i < 79:
                wg_breakfast = wg_anchors[i]["href"]
                wg_breakfast_lst.append(wg_breakfast)
                i += 1
                #print (wg_breakfast)
            #List of links Breakfast weight gain recipees
            #print(wg_breakfast_lst)
            #The recipees corresponsing to the links imported
            wg_recipee_lst_bf = ['Egg White Frittata','Breakfast Burrito','Salmon Toast',
            'Salmon Eggs Benedict','High Protein French Toast','Protein Chicken and Waffles',
            'Peanut Butter Chocolate Oatmeal Bowl','Egg And Pesto Sandwich',
            'Breakfast Casserole','Protein Yogurt Parfait']
            #Breakfast recipees and their links
            wg_breakfast_recipees = dict(zip(wg_recipee_lst_bf, wg_breakfast_lst))
            return(wg_breakfast_recipees)

            #Lunch
            wg_lunch_lst = []
            i = 80
            while i < 90:
                wg_lunch = wg_anchors[i]["href"]
                wg_lunch_list = wg_lunch_lst.append(wg_lunch)
                i += 1
                #print (wg_lunch)
            #List of weight gain lunch recipees
            wg_recipee_lst_l = ['Grilled Pesto Chicken Sandwich','Turkey Stuffed Bell Peppers','Thai Shrimp Noodle Bowl',
            'Flat Iron Steak Fajita Bowl','Spicy Tuna Sushi Bowl','Asian Turkey Lettuce Wraps',
            'Teriyaki Pineapple Chicken','Steak Kabobs',
            'New England Style Shrimp Rolls','Salmon Grain Bowl']
            wg_lunch_recipees = dict(zip(wg_recipee_lst_l, wg_lunch_lst))
            return(wg_lunch_recipees)
   

            #Dinner
            wg_dinner_lst = []
            i = 91
            while i < 101:
                wg_dinner = wg_anchors[i]["href"]
                wg_dinner_lst = wg_dinner_lst.append(wg_dinner)
                i += 1
                #print (wg_dinner)
            #List of Weight gain dinner recipees
            wg_recipee_lst_d = ['Tamarind-Chipotle Steak Nachos','Salmon Stir-fried Noodles','Creamy Ahi Tuna Pasta',
            'Steak Gyros','Butternut Squash and Chicken Pad Thai','Honey Sriracha Turkey Meatballs',
            'Coconut Crusted Fish Tacos','Healthy Bolognese',
            'Lean Pulled Pork','Salmon Chowder']
            wg_dinner_recipees = dict(zip(wg_recipee_lst_d, wg_dinner_lst))
            return(wg_dinner_recipees)
        
        
        
        
    
        
        
        
        #Macro ratios based on gaining, maintaining, or losing weight, along with the calories
        #Ratio of calories you want to be protein, carbs, and fat
        #Text file of diets
        
    #def Cardio(self, filename):
        """
        This function provides the amount of cardio as required by user goals
        Args:
            filename: Path to the file
        Returns(int): The minutes of cardio based on user goals
        """
        
        #Amount of cardio based on ratio
        #One cardio workout per parameter
        
    #def Cooldown(self):
        """
        This fucntion provides the restdays that a user should take based on their goals and how often they workout
        
        Return(int): the number of rest/cooldown days
     
        """
        
def parse_args(my_args_list):
    parser = argparse.ArgumentParser(description= "A fitness report")    
    parser.add_argument('-a', 'age', type = int, help="Age of the user", required = True)
    parser.add_argument('-w', 'weight', type = float, help="Weight of the user",required = True)
    parser.add_argument('-g', 'gender', type = str, help="Gender of the user",required = True)
    parser.add_argument('-h', 'height', type = float, help="Height of the user",  required = True)
    parser.add_argument('-o', 'objective', type = str, help ="User's goal to lose, mantain and gain weight", required = True )
    parser.add_argument('-o', 'how_often', type = int, help ="User's goal to lose, mantain and gain weight", required = True, min = 3, max = 5 )
    
    
    
    args = parser.parse_args(my_args_list)
    return args    

if __name__ == '__main__':
    print(sys.argv)
    args = parse_args(sys.argv[1:])
    print(FitnessSolutionReport(args.age, args.weight, args.gender, args.height, args.objective, args.how_often))
