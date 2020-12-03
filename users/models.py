from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from blog.models import Post
from datetime import date

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    user_age = models.IntegerField(default=0)
    user_height_in_inches = models.IntegerField(default=0)
    user_weight_in_lbs = models.IntegerField(default=0)
    sexes = (('Male','Male'),('Female','Female'))
    user_sex = models.CharField(max_length=10, choices = sexes)
    goals = (('Lose Weight','Lose Weight'),('Maintain Weight','Maintain Weight'),('Gain Weight','Gain Weight'))
    focus_areas = (('Eat enough grains','Eat enough grains'),('Eat enough protein','Eat enough protein'),('Eat enough dairy','Eat enough dairy'),('Eat enough vegetables','Eat enough vegetables'),('Limit grains intake','Limit grains intake'),('Limit protein intake','Limit protein intake'),('Limit dairy intake','Limit dairy intake'),('Limit vegetables intake','Limit vegetables intake'),('Limit fruit intake','Limit fruit intake'),('Reach aerobic exercise targets','Reach aerobic exercise targets'),('Reach muscle strengthening targets','Reach muscle strengthening targets'))
    focus_area_1 = models.CharField(default=0, max_length=40, choices = focus_areas)
    focus_area_2 = models.CharField(default=0, max_length=40, choices = focus_areas)
    focus_area_3 = models.CharField(default=0, max_length=40, choices = focus_areas)
    user_goals = models.CharField(default=0, max_length=20, choices = goals)
    favorite_food = models.TextField(default=0, max_length=50)
    favorite_hobby = models.TextField(default=0, max_length=50)
    bio = models.TextField(default=0, max_length=50)
    custom_grains_target = models.IntegerField(default = 0)
    custom_protein_target = models.IntegerField(default = 0)
    custom_dairy_target = models.IntegerField(default = 0)
    custom_vegetables_target = models.IntegerField(default = 0)
    custom_fruit_target = models.IntegerField(default = 0)
    custom_aerobic_target = models.IntegerField(default = 0)
    custom_muscle_strengthening_target = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()
    
    
    def habit_tracker_1(self):
        if self.focus_area_1 == 'Eat enough grains':
            output = self.days_in_a_row_eat_grains()
        elif self.focus_area_1 == 'Eat enough protein':
            output = self.days_in_a_row_eat_protein()
        elif self.focus_area_1 == 'Eat enough dairy':
            output = self.days_in_a_row_eat_dairy()
        elif self.focus_area_1 == 'Eat enough vegetables':
            output = self.days_in_a_row_eat_vegetables()
        elif self.focus_area_1 == 'Eat enough fruit':
            output = self.days_in_a_row_eat_fruit()
        elif self.focus_area_1 == 'Limit grains intake':
            output = self.days_in_a_row_limit_grains()
        elif self.focus_area_1 == 'Limit protein intake':
            output = self.days_in_a_row_limit_protein()
        elif self.focus_area_1 == 'Limit dairy intake':
            output = self.days_in_a_row_limit_dairy()
        elif self.focus_area_1 == 'Limit vegetables intake':
            output = self.days_in_a_row_limit_vegetables()
        elif self.focus_area_1 == 'Limit fruit intake':
            output = self.days_in_a_row_limit_fruit()
        elif self.focus_area_1 == 'Reach aerobic exercise targets':
            output = self.days_in_a_row_aerobic()
        elif self.focus_area_1 == 'Reach muscle strengthening targets':
            output = self.days_in_a_row_muscle_strengthening()
        else:
            output = 0
        return output
            
    def habit_tracker_2(self):
        if self.focus_area_2 == 'Eat enough grains':
            output = self.days_in_a_row_eat_grains()
        elif self.focus_area_2 == 'Eat enough protein':
            output = self.days_in_a_row_eat_protein()
        elif self.focus_area_2 == 'Eat enough dairy':
            output = self.days_in_a_row_eat_dairy()
        elif self.focus_area_2 == 'Eat enough vegetables':
            output = self.days_in_a_row_eat_vegetables()
        elif self.focus_area_2 == 'Eat enough fruit':
            output = self.days_in_a_row_eat_fruit()
        elif self.focus_area_2 == 'Limit grains intake':
            output = self.days_in_a_row_limit_grains()
        elif self.focus_area_2 == 'Limit protein intake':
            output = self.days_in_a_row_limit_protein()
        elif self.focus_area_2 == 'Limit dairy intake':
            output = self.days_in_a_row_limit_dairy()
        elif self.focus_area_2 == 'Limit vegetables intake':
            output = self.days_in_a_row_limit_vegetables()
        elif self.focus_area_2 == 'Limit fruit intake':
            output = self.days_in_a_row_limit_fruit()
        elif self.focus_area_2 == 'Reach aerobic exercise targets':
            output = self.days_in_a_row_aerobic()
        elif self.focus_area_2 == 'Reach muscle strengthening targets':
            output = self.days_in_a_row_muscle_strengthening()
        else:
            output = 0
        return output   
    
    def habit_tracker_3(self):
        if self.focus_area_3 == 'Eat enough grains':
            output = self.days_in_a_row_eat_grains()
        elif self.focus_area_3 == 'Eat enough protein':
            output = self.days_in_a_row_eat_protein()
        elif self.focus_area_3 == 'Eat enough dairy':
            output = self.days_in_a_row_eat_dairy()
        elif self.focus_area_3 == 'Eat enough vegetables':
            output = self.days_in_a_row_eat_vegetables()
        elif self.focus_area_3 == 'Eat enough fruit':
            output = self.days_in_a_row_eat_fruit()
        elif self.focus_area_3 == 'Limit grains intake':
            output = self.days_in_a_row_limit_grains()
        elif self.focus_area_3 == 'Limit protein intake':
            output = self.days_in_a_row_limit_protein()
        elif self.focus_area_3 == 'Limit dairy intake':
            output = self.days_in_a_row_limit_dairy()
        elif self.focus_area_3 == 'Limit vegetables intake':
            output = self.days_in_a_row_limit_vegetables()
        elif self.focus_area_3 == 'Limit fruit intake':
            output = self.days_in_a_row_limit_fruit()
        elif self.focus_area_3 == 'Reach aerobic exercise targets':
            output = self.days_in_a_row_aerobic()
        elif self.focus_area_3 == 'Reach muscle strengthening targets':
            output = self.days_in_a_row_muscle_strengthening()
        else:
            output = 0
        return output
    
    
    def days_in_a_row_aerobic(self):
        i=0
        days_in_a_row = 0
        while self.minutes_aerobic_activity_day(i) > 0:
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_muscle_strengthening(self):
        i=0
        days_in_a_row = 0
        while self.minutes_weightlifting_activity_day(i) > 0:
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_eat_protein(self):
        i=0
        days_in_a_row = 0
        while self.servings_protein_day(i) >= self.servings_recommended_protein():
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_eat_dairy(self):
        i=0
        days_in_a_row = 0
        while self.servings_dairy_day(i) >= self.servings_recommended_dairy():
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_eat_grains(self):
        i=0
        days_in_a_row = 0
        while self.servings_grains_day(i) >= self.servings_recommended_grains():
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_eat_vegetables(self):
        i=0
        days_in_a_row = 0
        while self.servings_vegetables_day(i) >= self.servings_recommended_vegetables():
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_eat_fruit(self):
        i=0
        days_in_a_row = 0
        while self.servings_fruit_day(i) >= self.servings_recommended_fruit():
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_limit_protein(self):
        i=0
        days_in_a_row = 0
        while self.servings_protein_day(i) <= self.servings_recommended_protein() & self.posts_on_day(i) > 0:
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_limit_dairy(self):
        i=0
        days_in_a_row = 0
        while self.servings_dairy_day(i) <= self.servings_recommended_dairy() & self.posts_on_day(i) > 0:
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_limit_grains(self):
        i=0
        days_in_a_row = 0
        while self.servings_grains_day(i) <= self.servings_recommended_grains() & self.posts_on_day(i) > 0:
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_limit_vegetables(self):
        i=0
        days_in_a_row = 0
        while (self.servings_vegetables_day(i) <= self.servings_recommended_vegetables()) & self.posts_on_day(i) > 0:
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
    
    def days_in_a_row_limit_fruit(self):
        i=0
        days_in_a_row = 0
        while self.servings_fruit_day(i) <= self.servings_recommended_fruit() & self.posts_on_day(i) > 0:
            days_in_a_row = days_in_a_row + 1
            i = i+1
        return days_in_a_row
                
    def servings_recommended_protein(self):
        if self.custom_protein_target == 0:  
            calories = self.calories_recommended()
            servings = 1.3265172+0.0021766*calories-0.0000010958*(calories-2100)**2
            servings = round(servings)
        else:
            servings = self.custom_protein_target
        return servings
    
    def servings_recommended_dairy(self):
        if self.custom_dairy_target == 0:
            calories = self.calories_recommended()
            servings = 2.9336507 + 0.000043221*calories - 0.00000034282*(calories-2100)**2 + 0.0000000003399*(calories-2100)**3 - 0.00000000000006829*(calories-2100)**4
            servings = round(servings)
        else:
            servings = self.custom_dairy_target
        return servings
    
    def servings_recommended_vegetables(self):
        if self.custom_vegetables_target == 0:    
            calories = self.calories_recommended()
            servings = -0.15035 + (0.0013811*calories) - 0.00000017483*(calories-2100)**2
            servings = round(servings)
        else:
            servings = self.custom_vegetables_target
        return servings
    
    def servings_recommended_grains(self):
        if self.custom_grains_target == 0:
            calories = self.calories_recommended()
            servings= -1.181555 + 0.0038832*calories - 0.00000011863*(calories-2100)**2 - 0.0000000005989*(calories-2100)**3
            servings = round(servings)
        else:
            servings = self.custom_grains_target
        return servings
    
    def servings_recommended_fruit(self):
        if self.custom_fruit_target == 0:           
            calories = self.calories_recommended()
            servings = 0.3786838 + (0.0007168*calories) - 0.00000010614*(calories-2100)**2
            servings = round(servings)
        else:
            servings = self.custom_fruit_target
        return servings
    
    def minutes_recommended_aerobic(self):
        if self.custom_aerobic_target == 0:
            minutes = 150
        else:
            minutes = self.custom_aerobic_target
        return minutes
    
    def aerobic_progress_one(self):
        total = self.minutes_recommended_aerobic()
        answer = total/6
        return answer
    
    def aerobic_progress_two(self):
        total = self.minutes_recommended_aerobic()
        answer = 2*total/6
        return answer
    
    def aerobic_progress_three(self):
        total = self.minutes_recommended_aerobic()
        answer = 3*total/6
        return answer
    
    def aerobic_progress_four(self):
        total = self.minutes_recommended_aerobic()
        answer = 4*total/6
        return answer
    
    def aerobic_progress_five(self):
        total = self.minutes_recommended_aerobic()
        answer = 5*total/6
        return answer
            
    def minutes_recommended_muscle_strengthening(self):
        if self.custom_muscle_strengthening_target == 0:
            minutes = 60
        else:
            minutes = self.custom_muscle_strengthening_target
        return minutes
    
    def muscle_strengthening_progress_one(self):
        total = self.minutes_recommended_muscle_strengthening()
        answer = total/6
        return answer
    
    def muscle_strengthening_progress_two(self):
        total = self.minutes_recommended_muscle_strengthening()
        answer = 2*total/6
        return answer
    
    def muscle_strengthening_progress_three(self):
        total = self.minutes_recommended_muscle_strengthening()
        answer = 3*total/6
        return answer
    
    def muscle_strengthening_progress_four(self):
        total = self.minutes_recommended_muscle_strengthening()
        answer = 4*total/6
        return answer
    
    def muscle_strengthening_progress_five(self):
        total = self.minutes_recommended_muscle_strengthening()
        answer = 5*total/6
        return answer
    
    def protein_servings_remaining(self):
        servings_recommended = self.servings_recommended_protein()
        servings_consumed = self.meat_servings_today()
        difference = servings_recommended - servings_consumed
        return difference
    
    def negative_protein_servings_remaining(self):
        servings_recommended = self.servings_recommended_protein()
        servings_consumed = self.meat_servings_today()
        difference = servings_consumed - servings_recommended
        return difference
    
    def grains_servings_remaining(self):
        servings_recommended = self.servings_recommended_grains()
        servings_consumed = self.grains_servings_today()
        difference = servings_recommended - servings_consumed
        return difference
    
    def negative_grains_servings_remaining(self):
        servings_recommended = self.servings_recommended_grains()
        servings_consumed = self.grains_servings_today()
        difference = servings_consumed - servings_recommended
        return difference
    
    def dairy_servings_remaining(self):
        servings_recommended = self.servings_recommended_dairy()
        servings_consumed = self.dairy_servings_today()
        difference = servings_recommended - servings_consumed
        return difference
    
    def negative_dairy_servings_remaining(self):
        servings_recommended = self.servings_recommended_dairy()
        servings_consumed = self.dairy_servings_today()
        difference = servings_consumed - servings_recommended
        return difference
    
    def vegetables_servings_remaining(self):
        servings_recommended = self.servings_recommended_vegetables()
        servings_consumed = self.vegetables_servings_today()
        difference = servings_recommended - servings_consumed
        return difference
    
    def negative_vegetables_servings_remaining(self):
        servings_recommended = self.servings_recommended_vegetables()
        servings_consumed = self.vegetables_servings_today()
        difference = servings_consumed - servings_recommended
        return difference
    
    def fruit_servings_remaining(self):
        servings_recommended = self.servings_recommended_fruit()
        servings_consumed = self.fruit_servings_today()
        difference = servings_recommended - servings_consumed
        return difference
    
    def negative_fruit_servings_remaining(self):
        servings_recommended = self.servings_recommended_fruit()
        servings_consumed = self.fruit_servings_today()
        difference = servings_consumed - servings_recommended
        return difference
    
    
    def baseline_metabolic_rate(self):
        age = self.user_age
        height = self.user_height_in_inches
        weight = self.user_weight_in_lbs
        if self.user_sex == 'male':
            bmr = 66 + (6.3*weight) + (12.9*height) - (6.8*age)
        else:
            bmr = 655 + 4.3*weight + 4.7*height - 4.7*age
        return bmr
        
    def calories_recommended(self):
        calories = self.calories_expected()
        if self.user_goals == "Lose Weight":
            calories = calories - 500
        elif self.user_goals == "Gain Weight":
            calories = calories + 500   
        return calories
    
    def expected_aerobic_activity_day(self):
        one_day_before = 1
        two_days_before = 2
        three_days_before = 3
        four_days_before = 4
        five_days_before = 5
        six_days_before = 6
        seven_days_before = 7
        eight_days_before = 8
        nine_days_before = 9
        ten_days_before = 10
        one = float(self.minutes_aerobic_activity_day(one_day_before))
        two = float(self.minutes_aerobic_activity_day(two_days_before))
        three = float(self.minutes_aerobic_activity_day(three_days_before))
        four = float(self.minutes_aerobic_activity_day(four_days_before))
        five = float(self.minutes_aerobic_activity_day(five_days_before))
        six = float(self.minutes_aerobic_activity_day(six_days_before))
        seven = float(self.minutes_aerobic_activity_day(seven_days_before))
        eight = float(self.minutes_aerobic_activity_day(eight_days_before))
        nine = float(self.minutes_aerobic_activity_day(nine_days_before))
        ten = float(self.minutes_aerobic_activity_day(ten_days_before))
        total = one + two + three + four + five + six + seven + eight + nine + ten
        if total > 0:
            average = total/15
        else:
            average = 0
        return average
    
    def expected_weightlifting_activity_day(self):
        one_day_before = 1
        two_days_before = 2
        three_days_before = 3
        four_days_before = 4
        five_days_before = 5
        six_days_before = 6
        seven_days_before = 7
        eight_days_before = 8
        nine_days_before = 9
        ten_days_before = 10
        one = float(self.minutes_weightlifting_activity_day(one_day_before))
        two = float(self.minutes_weightlifting_activity_day(two_days_before))
        three = float(self.minutes_weightlifting_activity_day(three_days_before))
        four = float(self.minutes_weightlifting_activity_day(four_days_before))
        five = float(self.minutes_weightlifting_activity_day(five_days_before))
        six = float(self.minutes_weightlifting_activity_day(six_days_before))
        seven = float(self.minutes_weightlifting_activity_day(seven_days_before))
        eight = float(self.minutes_weightlifting_activity_day(eight_days_before))
        nine = float(self.minutes_weightlifting_activity_day(nine_days_before))
        ten = float(self.minutes_weightlifting_activity_day(ten_days_before))
        total = one + two + three + four + five + six + seven + eight + nine + ten
        if total > 0:
            average = total/15
        else:
            average = 0
        return average
    
    def calories_expended_aerobic(self):
        expected_minutes = self.expected_aerobic_activity_day()
        weight = self.user_weight_in_lbs
        weight = weight / 2.20462
        calories = (weight*expected_minutes*3.5*6)/200
        return calories
    
    def calories_expended_weightlifting(self):
        expected_minutes = self.expected_weightlifting_activity_day()
        weight = self.user_weight_in_lbs
        weight = weight / 2.20462
        calories = (weight*expected_minutes*3.5*4.5)/200
        return calories
    
    def calories_expected(self):
        aerobic_calories = self.calories_expended_aerobic()
        weightlifting_calories = self.calories_expended_weightlifting()
        bmr = self.baseline_metabolic_rate()
        total_calories = aerobic_calories + weightlifting_calories + bmr
        return total_calories
    
    def minutes_aerobic_activity_week(self):
        today = date.today()
        if today.weekday() == 0:
            today = 0
            return self.minutes_aerobic_activity_day(today)
        elif today.weekday() == 1:
            today = 0
            days_before = 1
            monday = int(self.minutes_aerobic_activity_day(days_before))
            tuesday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday
        elif today.weekday() == 2:
            today = 0
            days_before = 1
            two_days_before = 2
            monday = int(self.minutes_aerobic_activity_day(two_days_before))
            tuesday = int(self.minutes_aerobic_activity_day(days_before))
            wednesday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday + wednesday
        elif today.weekday() == 3:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            monday = int(self.minutes_aerobic_activity_day(three_days_before))
            tuesday = int(self.minutes_aerobic_activity_day(two_days_before))
            wednesday = int(self.minutes_aerobic_activity_day(days_before))
            thursday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday + wednesday + thursday
        elif today.weekday() == 4:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            monday = int(self.minutes_aerobic_activity_day(four_days_before))
            tuesday = int(self.minutes_aerobic_activity_day(three_days_before))
            wednesday = int(self.minutes_aerobic_activity_day(two_days_before))
            thursday = int(self.minutes_aerobic_activity_day(days_before))
            friday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday
        elif today.weekday() == 5:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            five_days_before = 5
            monday = int(self.minutes_aerobic_activity_day(five_days_before))
            tuesday = int(self.minutes_aerobic_activity_day(four_days_before))
            wednesday = int(self.minutes_aerobic_activity_day(three_days_before))
            thursday = int(self.minutes_aerobic_activity_day(two_days_before))
            friday = int(self.minutes_aerobic_activity_day(days_before))
            saturday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday + saturday
        elif today.weekday() == 6:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            five_days_before = 5
            six_days_before = 6
            monday = int(self.minutes_aerobic_activity_day(six_days_before))
            tuesday = int(self.minutes_aerobic_activity_day(five_days_before))
            wednesday = int(self.minutes_aerobic_activity_day(four_days_before))
            thursday = int(self.minutes_aerobic_activity_day(three_days_before))
            friday = int(self.minutes_aerobic_activity_day(two_days_before))
            saturday = int(self.minutes_aerobic_activity_day(days_before))
            sunday = int(self.minutes_aerobic_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday + saturday + sunday
        
    def minutes_weightlifting_activity_week(self):
        today = date.today()
        if today.weekday() == 0:
            today = 0
            return self.minutes_weightlifting_activity_day(today)
        elif today.weekday() == 1:
            today = 0
            days_before = 1
            monday = int(self.minutes_weightlifting_activity_day(days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday
        elif today.weekday() == 2:
            today = 0
            days_before = 1
            two_days_before = 2
            monday = int(self.minutes_weightlifting_activity_day(two_days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(days_before))
            wednesday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday + wednesday
        elif today.weekday() == 3:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            monday = int(self.minutes_weightlifting_activity_day(three_days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(two_days_before))
            wednesday = int(self.minutes_weightlifting_activity_day(days_before))
            thursday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday + wednesday + thursday
        elif today.weekday() == 4:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            monday = int(self.minutes_weightlifting_activity_day(four_days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(three_days_before))
            wednesday = int(self.minutes_weightlifting_activity_day(two_days_before))
            thursday = int(self.minutes_weightlifting_activity_day(days_before))
            friday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday
        elif today.weekday() == 5:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            five_days_before = 5
            monday = int(self.minutes_weightlifting_activity_day(five_days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(four_days_before))
            wednesday = int(self.minutes_weightlifting_activity_day(three_days_before))
            thursday = int(self.minutes_weightlifting_activity_day(two_days_before))
            friday = int(self.minutes_weightlifting_activity_day(days_before))
            saturday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday + saturday
        elif today.weekday() == 6:
            today = 0
            days_before = 1
            two_days_before = 2
            three_days_before = 3
            four_days_before = 4
            five_days_before = 5
            six_days_before = 6
            monday = int(self.minutes_weightlifting_activity_day(six_days_before))
            tuesday = int(self.minutes_weightlifting_activity_day(five_days_before))
            wednesday = int(self.minutes_weightlifting_activity_day(four_days_before))
            thursday = int(self.minutes_weightlifting_activity_day(three_days_before))
            friday = int(self.minutes_weightlifting_activity_day(two_days_before))
            saturday = int(self.minutes_weightlifting_activity_day(days_before))
            sunday = int(self.minutes_weightlifting_activity_day(today))
            return monday + tuesday + wednesday + thursday + friday + saturday + sunday
    
    def minutes_aerobic_activity_day(self,days_before):
        today = date.today()
        posts_on_day = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day-days_before, author=self.user)
        total_servings = 0
        for post in posts_on_day:
            total_servings = total_servings + post.minutes_aerobic_exercise
        return total_servings
        

    def posts_on_day(self,days_before):
        today = date.today()
        posts_on_day = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day-days_before, author=self.user)
        total = posts_on_day.count()
        return total
    
    def servings_protein_day(self,days_before):
        today = date.today()
        posts_on_day = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day-days_before, author=self.user)
        total_servings = 0
        for post in posts_on_day:
            total_servings = total_servings + post.servings_meat
        return total_servings
    
    def servings_dairy_day(self,days_before):
        today = date.today()
        posts_on_day = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day-days_before, author=self.user)
        total_servings = 0
        for post in posts_on_day:
            total_servings = total_servings + post.servings_dairy
        return total_servings
    
    def servings_grains_day(self,days_before):
        today = date.today()
        posts_on_day = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day-days_before, author=self.user)
        total_servings = 0
        for post in posts_on_day:
            total_servings = total_servings + post.servings_grains
        return total_servings
    
    def servings_vegetables_day(self,days_before):
        today = date.today()
        posts_on_day = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day-days_before, author=self.user)
        total_servings = 0
        for post in posts_on_day:
            total_servings = total_servings + post.servings_vegetables
        return total_servings
    
    def servings_fruit_day(self,days_before):
        today = date.today()
        posts_on_day = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day-days_before, author=self.user)
        total_servings = 0
        for post in posts_on_day:
            total_servings = total_servings + post.servings_fruit
        return total_servings
    
    def minutes_weightlifting_activity_day(self,days_before):
        today = date.today()
        posts_on_day = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day-days_before, author=self.user)
        total_servings = 0
        for post in posts_on_day:
            total_servings = total_servings + post.minutes_weightlifting_exercise
        return total_servings

    
    def minutes_aerobic_activity_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.minutes_aerobic_exercise
        return total_servings
    
    def minutes_weightlifting_activity_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.minutes_weightlifting_exercise
        return total_servings
    
    def meat_servings_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.servings_meat
        return total_servings
    
    def grains_servings_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.servings_grains
        return total_servings

    def dairy_servings_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.servings_dairy
        return total_servings

    def vegetables_servings_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.servings_vegetables
        return total_servings

    def fruit_servings_today(self):
        today = date.today()
        posts_today = Post.objects.filter(date_posted__year=today.year, date_posted__month=today.month, date_posted__day=today.day, author=self.user)
        total_servings = 0
        for post in posts_today:
            total_servings = total_servings + post.servings_fruit
        return total_servings

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
     
   
        
    
    
