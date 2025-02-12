# Project A: Visualizing Air Pollution Data
Joshua Nielsen  
Prof. Mike Ryu  
CS-150 Community Action Computing  

![Screenshot of the visualizer in action](/assets/sample_screenshot.png)

## Thesis Statement
I want to create a large-scale, dynamic visual to represent recorded ozone levels across the country over the entire year of 2024. I want it to have multiple moving parts that allow the user to customize how they see the data.

## Context
I read [in an article by IQAir](https://www.iqair.com/us/usa/california/los-angeles) that LA has some of the highest Ozone levels in the country. I wanted to see for myself how it compares to other cities, in a way that others could access. This program is for anyone who is curious about the current state of national ozone levels. My visualization covers every state through use of a dropdown menu, and every day using a slider bar. When you select a state and a day, the chart displays the mean value for each county. The slider bar dynamically changes the chart, meaning it is easy to slide back and forth and observe the changes over time.

## What am I Visualizing?
I am visualizing the percentage of ozone observed in each county in each state, over the year of 2024. There are many factors at play, which is why my callback function takes two inputs. 100% is normal observed ozone, but the bars can go as high as 1600%! (sixteen times the normal amount)

## Data Visualization Strategies
I wanted to make this a complex visualization which is also not too difficult to use. Right now you can only display statistics for one state at a time, as not to overwhelm the user with data. The slider bar is a little jank; I am aware of this, but after hours of toying with it, this is the cleanest I could get, without either showing data for January 85th, April 46th, etc. I also can't format the data for display without another callback funciton, which I believe is out of the scope of this project. The counties and states are listed in alphabetical order, so users should not have a difficult time finding the ones they are looking for. The charts appear to sometimes use diagonal titles; I couldn't find a way to disable this. Overall there are many improvements I could make, and even better ways to display the data entirely (showing each county's values over the course of 2024 on a line graph as opposed to having a bar chart and a slider, for example), but I really wanted to challenge myself to make a double-input callback function. 
