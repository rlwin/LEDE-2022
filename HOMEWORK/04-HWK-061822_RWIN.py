#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[95]:


import requests
url='http://api.weatherapi.com/v1/current.json?key=fcedd833a9614b4abc220520221406&q=manchester'

response=requests.get(url)
data=response.json()


# 

# In[ ]:





# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[96]:


# see above!
#print(data.keys())
print(data['location'])


# In[ ]:





# In[ ]:





# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[91]:


print(data['current'])


# In[97]:


current_weather=data['current']
current_wind=current_weather['wind_mph']
print(f"The current wind speed is {current_wind}mph")


# In[93]:


if current_weather['feelslike_c']>current_weather['temp_c']:
    temp_feel=current_weather['feelslike_c']-current_weather['temp_c']
    print("it feels", round(temp_feel, 2), "degrees C warmer than the current temp.")
else:
    temp_feel=current_weather['temp_c']-current_weather['feelslike_c']
    print("It feels", round(temp_feel, 2), "degrees C colder than the current temp." )


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[4]:


url2='http://api.weatherapi.com/v1/astronomy.json?key=fcedd833a9614b4abc220520221406&q=manchester&dt=2022-06-19'
import requests
response2=requests.get(url2)
data2=response2.json()


# In[ ]:





# In[9]:


#print(data2.keys())
#dict_keys(['location', 'astronomy'])
#print(data2['astronomy'])
visable=(data2['astronomy']['astro']['moon_illumination'])
phase=(data2['astronomy']['astro']['moon_phase'])

print(f"Tomorrow, on the 19th, the moon will be {visable}% visable at a {phase}")



# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[10]:


url3='http://api.weatherapi.com/v1/forecast.json?key=fcedd833a9614b4abc220520221406&q=11222'
import requests
response3=requests.get(url3)
data3=response3.json()

print(data3['location'])


# In[11]:


#print(data3.keys())
#print(data3['forecast'].keys())
#print(data3['forecast']['forecastday'])
forecast_bk=(data3['forecast']['forecastday'])

for forecast_current in forecast_bk:
    forecast_temp=(forecast_current['day'])
    if forecast_temp['maxtemp_c']>forecast_temp['mintemp_c']:
        temp_dif=forecast_temp['maxtemp_c']-forecast_temp['mintemp_c']
        print (f"The difference between the high and low temps for today is {round(temp_dif, 2)} degrees C")
    else:
        temp_dif=forecast_temp['mintemp_c']-forecast_temp['maxtemp_c']
        print(f"The difference between the high and low temps for today is {round(temp_dif, 2)} degrees C")
   


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[ ]:


# rename the url and response/request etc. I renamed them by order they were imported, i.e. url, url2, url3, etc


# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[12]:


import requests

url4 = 'http://api.weatherapi.com/v1/forecast.json?key=fcedd833a9614b4abc220520221406&q=11222&days=3&aqi=no&alerts=no'
response4=requests.get(url4)
data4=response4.json()

#print(data4.keys())
#print(data4['forecast'].keys())
threeday_forecast=(data4['forecast']['forecastday'])
for daycast in threeday_forecast:
    maxtemp_forecast=(daycast['day']['maxtemp_c'])
    print(f"The maximum temperature for {daycast['date']} will be {maxtemp_forecast}degrees C")
    


# In[13]:


for daycast in threeday_forecast:   
    if maxtemp_forecast<15:
        print(f"It will feel cold on {daycast['date']}")
    elif maxtemp_forecast>=15:
        print(f"It will feel warm on {daycast['date']}")
    elif maxtemp_forecast>25:
        print(f"It will feel hot on {daycast['date']}")




# In[ ]:





# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[ ]:


#API is set only to three days forecast


# In[ ]:





# In[ ]:





# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[17]:


for temp in threeday_forecast:
    temp_forecast=(temp['day'])
    high_temps=(temp_forecast['maxtemp_c'])
    print(high_temps)
    
    #can't figure out, I need to make hottest_day=(high_temps[0])
    #and then within this loop
    # if high_temps>high_temps[0]:
        #hottest_day=high_temps
    #not sure how to assign the hottest_day to the first result in high_temps


# In[ ]:





# In[ ]:





# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[18]:


import requests
url5='http://api.weatherapi.com/v1/forecast.json?key=fcedd833a9614b4abc220520221406&q=Miami&days=1'
response5=requests.get(url5)
data5=response5.json()
# dict_keys(['location', 'current', 'forecast'])
#print(data5['location'])
miami_forecast=(data5['forecast']['forecastday'])
for hourly_forecast in miami_forecast:
    for hourly in hourly_forecast['hour']:
        #print(hourly['time'])
        #print(hourly['temp_c'])
        #print(f"At {hourly['time']} it will be {hourly['temp_c']} degrees C")
        #print(hourly['cloud'])
        if hourly['cloud']>50:
            print(f"At {hourly['time']} it will be {hourly['temp_c']} degrees C and cloudy")
        else:
            print(f"At {hourly['time']} it will be {hourly['temp_c']} degrees C and clear")
    



# In[ ]:





# In[ ]:





# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[19]:


above85=0

miami_forecast=(data5['forecast']['forecastday'])
for hourly_forecast in miami_forecast:
    for hourly in hourly_forecast['hour']:
        hourly_temp=hourly['temp_f']
        if (hourly_temp)>85:
                above85=above85+1
above85=(above85/24*100)
print(f"The temperature will be above 85F {round(above85, 2)}% of the time today")


# In[ ]:





# In[ ]:





# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# In[ ]:


# $4 a month for <= 2000000 calls a month


# In[ ]:





# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# In[ ]:


# not sure?! Sign up for student accounts? 

