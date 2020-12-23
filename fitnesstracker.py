import re
import requests
import sys
import matplotlib.pyplot as plt
import pandas as pd
from argparse import ArgumentParser
from bs4 import BeautifulSoup



class FitnessSolutionReport:
    """Calls class FitnessSolutionReport"""
    
    
    
    def __init__(self, age, weight, gender, height, objective, how_often):
        """
        Creates attributes and stores the information from the parameters 
        Args: 
            age (int): The user's age
            gender (str): The user's gender
            weight (float): The user's weight in kilograms
            height (float): The user's height in centimeters
            objective (str): Whether the user wants to gain, maintain, or lose weight
            how_often (int): How many days the user wants to work out (minimum of 3 and maximum of 6)
        """
        self.age = age
        self.weight = weight
        self.gender = gender
        self.height = height
        self.objective = objective
        self.how_often = how_often
        
    
        
    def DataframeConverter(self, url, days):
        """
        Scrapes data from the given URL, converts it into a Pandas dataframe, and returns it
        Args: 
            url: The URL of the website from which the data is going to be scraped
            days (int): Amount of days user wants to workout (pulled from WorkoutRegime)
        Returns: Updated dataframe based on the input of the the user and the corresponding website with the fitness regime
        """
        
        res = requests.get(url)
        soup = BeautifulSoup(res.content,'lxml')
        table = soup.find_all('table', class_='InnerTable')
        
        l = []
        
        for i in range(days):
            innerTables = table[i].find_all('p')
            exercise = table[i].find_all('a')
            td = table[i].find_all('td')
            names, timers, reps, Sets = 2, 9, 10, 11
            
            for i in range(len(innerTables)):
                    day = {}
                    day["Muscle"] = innerTables[i].text
                    try:
                        day["Exercise Name"] = exercise[names].text
                    except:
                        day["Exercise Name"] = exercise[2].text
                    try:
                        day["Timer"] = td[timers].text.replace(' ','').replace('\n','')
                    except:
                        day["Timer"] = td[9].text.replace(' ','').replace('\n','')
                    try:
                        day["Reps"] = td[reps].text.replace(' ','').replace('\n','')
                    except:
                        day["Reps"] = td[10].text.replace(' ','').replace('\n','')
                    try:
                        day["Sets"] = td[Sets].text.replace(' ','').replace('\n','') 
                    except:
                        day["Sets"] = td[11].text.replace(' ','').replace('\n','') 
                    

                    names += 4
                    timers += 7
                    reps +=7
                    Sets += 7

                    l.append(day)
                    
        df = pd.DataFrame(l)
        return df
              
       
    
    def BioCalculator(self):
        """
        Calculates the user's BMI, BMR, and weight status based on weight, height, age, and gender
        Returns: Dataframe featuring biological data about the user, including BMR, BMI, and weight status
        Side Effects:
            Prints out a title statement defining what information the function is outputting to the user
        """

        l = []
        d_ret = {}
        p_bmi = (self.weight / (self.height * self.height)) * 703

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

        if p_bmi < 18.5:
            weightStatus = "Underweight"
        elif p_bmi > 18.5 and p_bmi < 25:
            weightStatus = "Normal weight"
        elif p_bmi > 25:
            weightStatus = "Overweight"

        d_ret["BMR"] = bmr
        d_ret["BMI"] = p_bmi
        d_ret["Weight Status"] = weightStatus

        l.append(d_ret)
        df = pd.DataFrame(l)
        
        print('\n' + '-' * 180)
        print('\033[1m'+'A Comprehensive Fitness Report')
        print('\n' + '-' * 180)
        
        print('\n' + '-' * 120)
        print("Unique biological health information about the user based on various factors.")
        print('\n' + '-' * 120)
        
        return df
    
    
       
    def WorkoutRegime(self):
        """
        Provides user with workout regime based on their objective and how often they want to workout.
        Returns: Dataframe featuring workout regime based on the URL provided
        Side Effects: 
            Prints out a title statement defining what information the function is outputting to the user
            Calls DataframeConverter() function
            Adds column to dataframe specifying days using df.index()
        """
        
        print('\n' + '-' * 120)
        print("A custom-made workout-plan based on your primary objective and preference for how often you would like to workout.")
        print('\n' + '-' * 120)
        
        #FOR WORKING OUT THREE DAYS

        if self.how_often == 3:
            
            if self.objective == "maintain":

                url = "https://www.jefit.com/routines/72415/wedding-thicc"
                df = self.DataframeConverter(url, 3)
                df.index = ['Day 1', ' ', ' ', ' ' , ' ' , ' ', 'Day 2' ,' ' , ' ', ' ', ' ' , ' ' , 'Day 3' , ' ' , ' ' , ' ' , ' ', ' ', ' ' , ' '] 
                return df

            elif self.objective == "gain":

                url = "https://www.jefit.com/routines/199187/5x5-split-routine-3-day"
                df = self.DataframeConverter(url, 3)
                df.index = ['Day 1', ' ', ' ', ' ' , 'Day 2' ,' ' , ' ', ' ',  'Day 3' , ' ' , ' ' , ' ' , ' ' ] 
                return df

            elif self.objective == "lose":

                url = "https://www.jefit.com/routines/86376/3-day-for-running"
                df = self.DataframeConverter(url, 3)
                df.index = ['Day 1', ' ', ' ', ' ' , ' ', ' ', ' ' ,' ', ' ','Day 2' ,' ' , ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' ' ,  'Day 3' , ' ' , ' ' , ' ' , ' ' , ' ', ' ', ' ' ,' ', ' ', ' ' ] 
                return df

        #FOR WORKING OUT FOUR DAYS

        if self.how_often == 4:
            
            if self.objective == "maintain":

                url = "https://www.jefit.com/routines/70021/masunas-baseball-off-season-program-weeks-1-4"
                df = self.DataframeConverter(url, 4)
                df.index = ['Monday', ' ', ' ', ' ' , ' ' , ' ', 'Tuesday' ,' ' , ' ', ' ', ' ' , ' ' , ' ' , ' ' ,' ' , ' ' , 'Thursday' , ' ' , ' ' , ' ', ' ', ' ' ,'Friday' , ' ' , ' ' , ' ' , ' ', ' ', ' ' , ' ' , ' ' ,' '] 
                return df

            elif self.objective == "gain":
                url = "https://www.jefit.com/routines/195547/hipertrofia-de-todo-el-cuerpo"
                df = self.DataframeConverter(url, 4)
                df.index = ['Monday', ' ', ' ', ' ' , ' ' , ' ', 'Tuesday' ,' ' , ' ', ' ', ' ' , ' ' ,  'Thursday' , ' ' , ' ' , ' ', ' ', ' ' ,'Friday' , ' ' , ' ' , ' ' , ' ', ' '] 
                return df

            elif self.objective == "lose":
                url = "https://www.jefit.com/routines/112064/lean-and-large"
                df = self.DataframeConverter(url, 4)
                df.index = ['Day 1', ' ', ' ', ' ' , ' ' , ' ', 'Day 2' ,' ' , ' ', ' ', ' ' , ' ' , ' ',  'Day 3' , ' ' , ' ' , ' ', ' ', ' ' ,'Day 4' , ' ' , ' ' , ' ' , ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' '] 
                return df

        #FOR WORKING OUT FIVE DAYS

        if self.how_often == 5:
            
            if self.objective == "maintain":

                url = "https://www.jefit.com/routines/101459/bikini-prep-schedule-4"
                df = self.DataframeConverter(url, 5)
                df.index = ['Monday', ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , 'Tuesday' ,' ' , ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , ' ' ,' ','Wednesday' , ' ' , ' ' , ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , ' ', 'Thursday' , ' ' , ' ' , ' ' , ' ', ' ', ' ' , ' ' , ' ' , 'Friday ' , ' ' , ' ' , ' ' , ' ' ,' ', ' ', ' '] 
                return df

            elif self.objective == "gain":

                url = "https://www.jefit.com/routines/195713/scovs-routine"
                df = self.DataframeConverter(url, 5)
                df.index = ['Monday', ' ', ' ', ' ' , ' ' , ' ' , ' ' , 'Tuesday' ,' ' , ' ', ' ','Wednesday' , ' ' , ' ' , ' ', 'Thursday' , ' ' , ' ' , ' ' , ' ' , 'Friday ' , ' ' , ' ' , ' ']
                return df

            elif self.objective == "lose":

                url = "https://jefit.com/routines/107113/rajata-workout"
                df = self.DataframeConverter(url, 5)
                df.index = ['Monday', ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , ' ' ,' ', ' ',' ',' ',' ', 'Tuesday' ,' ' , ' ', ' ', ' ' , ' ' , ' ' , ' ' ,'Wednesday' , ' ' , ' ' , ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , ' ', ' ', 'Thursday' , ' ' , ' ' , ' ' , ' ', ' ', ' ' , ' ' , ' ' ,' ', ' ', ' ', ' ', 'Friday ']
                return df            

        #FOR WORKING OUT SIX DAYS

        if self.how_often == 6:

            if self.objective == "maintain":

                url = "https://www.jefit.com/routines/33778/swimming-and-strength-101"
                df = self.DataframeConverter(url, 6)
                df.index = ['Day 1', 'Day 2', ' ', ' ' , ' ' , ' ' , 'Day 3' , 'Day 4' , 'Day 5' , ' ' , ' ' , ' ' , ' ' ,''] 
                return df

            elif self.objective == "gain":

                url = "https://www.jefit.com/routines/111830/6-day-push-pull-leg-workout-for-body-recomposition"
                df = self.DataframeConverter(url, 6)
                df.index = ['Monday', ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , 'Tuesday' ,' ' , ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , 'Wednesday' , ' ' , ' ' , ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , 'Thursday' , ' ' , ' ' , ' ' , ' ', ' ', ' ' , ' ' , ' ' , 'Friday ' , ' ' , ' ' , ' ' , ' ' ,' ', ' ', ' ' , ' ' , ' ' , ' ' , 'Saturday' , ' ' , ' ' , ' ' , ' ' , ' ', ' ',' ', ' ', ' '] 
                return df

            elif self.objective == "lose":

                url = "https://www.jefit.com/routines/103151/fat-loss-workout"
                df = self.DataframeConverter(url, 6)
                df.index = ['Monday', ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ', 'Tuesday' ,' ' , ' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , 'Wednesday' , ' ' , ' ' , ' ', ' ', ' ' , ' ' , ' ' , 'Thursday' , ' ' , ' ' , ' ' , ' ', ' ', ' ' , 'Friday ' , ' ' , ' ' , ' ' , ' ' ,' ', ' ', ' ' , ' ' , ' ' , ' ' , ' ' , 'Saturday' , ' ' , ' ' , ' ' , ' ' , ' ', ' ',' ', ' ', ' ' , ' ' , ' '] 
                return df
    
    
    
    def DietPlan(self):
        """
            Scrapes diet tables from provided URLS and returns them as Pandas dataframes
            Returns: Output statement regarding diet maintenance
            Side Effects:
                Prints out a title statement defining what information the function is outputting to the user
                Prints dashes that help separate information
                Prints text as header titles for the dataframes
                Prints actual dataframes
                Prints newline character
        """
        
        print('\n' + '-' * 120)
        print("A custom-made diet plan based on your goals (only applicale to users who want to gain/lose weight).")
        print('\n' + '-' * 120)
        
        if self.objective == "lose":
            url = 'http://www.myfooddata.com/articles/gourmet-low-carb-high-protein-weight-loss-meal-plans.php'
            num_of_tables = 7
        elif self.objective == "gain":
            url = 'http://myfooddata.com/articles/budget-weight-gain-meal-plans.php'
            num_of_tables = 7
        else:
            output = 'To maintain your caloric intake, calculate your maintenance calories using this website: https://mayocl.in/3hfMMfJ'
            return output
        
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')
        table = soup.find_all('div', class_='dayplan')
        head = soup.find_all('h2')
        dfs = pd.read_html(url)
        
        #Headings
        
        tableCounter = 0
        for i in range(num_of_tables):
            print('-' * 60)
            print(head[i].text[: 5] + ' ' + head[i].text[5:])
            print('-' * 60)
            
            # Inner Headings
            
            innerTable = table[i].find_all('strong')
            for j in range(len(innerTable)):
                print(innerTable[j].text)
                print(dfs[tableCounter])
                tableCounter += 1
                print('\n')



    def FitnessResources(self):
        """
        To obtain author and URL information of fitness resources from a file and organize them into a dataframe
        Returns: Dataframe featuring magazines and URLS that provide the user with fitness information
        Side Effects: 
            Prints out a title statement defining what information the function is outputting to the user
        """
        
        print('\n' + '-' * 120)
        print("A list of hand-selected fitness resources that will help to answer any questions you might have regarding the above information.")
        print('\n' + '-' * 120)
        
        a = []
        u = []
        d = []
        with open("fitness_resources.txt", 'r', encoding = "utf-8") as f:
        
            for line in f:
                url = (re.findall('(https?:\/\/www\.[^|]*$)', line))
                author = (re.findall('([A-Za-z]+,\s+[A-Za-z]+\s[A-Za-z].)', line))
                date = (re.findall ('(\d{4})', line))

                a.append(str(author)[1:-1].replace("'", ""))
                u.append(str(url)[1:-1].replace(r"\n" "'", ""))
                d.append(str(date)[1:-1].replace("'", ""))
            
        d = {'Author of Magazine': a, 'Website link': u, 'Date': d}
        magazines = pd.DataFrame(data = d)
        magazines.reset_index(drop=True, inplace=True) 
        magazines.sort_values(by=['Date'], inplace=True, ascending=False)
        return(magazines)
    
    
    
    def Tips(self):
        """
        To obtain fitness tips from a file and organize them into a dataframe by week
        Returns: Dataframe featuring tips thatare organized by week
        Side Effects: 
            Prints out a title statement defining what information the function is outputting to the user
        """
    
        print('\n' + '-' * 120)
        print("A list of fitness tips that you can read on your daily journey.")
        print('\n' + '-' * 120)
        
        df = pd.read_csv("tips.csv")
        return(df)
    
    

    def WeightManage(self):
            """
                Plots a graph expressing how much weight the user would gain/lose/maintain over 4 weeks
                Args:
                    objective (str): Whether the user wants to gain, maintain, or lose weight
                Side Effects:
                    Prints out a title statement defining what information the function is outputting to the user
                    Shows graph output
            """
            
            print('\n' + '-' * 120)
            print("A graph visualizing the way your weight will change if you follow the diet plan above (will output in separate window).")
            print('\n' + '-' * 120)
            
            if self.objective == 'lose':
                lbl = 'Weight Lost from Cardio'
                weight = [self.weight, self.weight-2, self.weight-4, self.weight-6]
            elif self.objective == 'gain':
                lbl = 'Weight Gained from Calories'
                weight = [self.weight, self.weight+2, self.weight+4, self.weight+6]
            elif self.objective == 'maintain':
                lbl = 'Weight Maintained from Calories'
                weight = [self.weight, self.weight, self.weight, self.weight]
            
            weeks = [1, 2, 3, 4]
            
            plt.xlabel('Weeks')
            plt.ylabel('Weight (kg)')

            plt.plot(weeks, weight, label=lbl)
            plt.grid()
            plt.legend()
            plt.show()


    
def parse_args(my_args_list):
    parser = ArgumentParser(description= "A comprehensive fitness report")   
    parser.add_argument('age', type = int, help="Age of the user")
    parser.add_argument('weight', type = float, help="Weight of the user (kg)")
    parser.add_argument('gender', type = str, help="Gender of the user (male/female)")
    parser.add_argument('height', type = float, help="Height of the user (cm)")
    parser.add_argument('objective', type = str, help ="User's goal to lose, mantain or gain weight")
    parser.add_argument('how_often', type = int, help ="How many days the user wants to spend attaining their goal (3-6)", choices=range(3,7))
    
    args = parser.parse_args()
    return args    

if __name__ == '__main__':
    print(sys.argv)
    args = parse_args(sys.argv[1:])
    fitness = FitnessSolutionReport(args.age, args.weight, args.gender, args.height, args.objective, args.how_often)
    print(fitness.BioCalculator())
    print(fitness.WorkoutRegime())
    print(fitness.DietPlan())
    print(fitness.FitnessResources())
    print(fitness.Tips())
    print(fitness.WeightManage())
