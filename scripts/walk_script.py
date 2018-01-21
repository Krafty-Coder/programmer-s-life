if person.bored():
  x = [0]

  for j in range(100):
      step_x = random.randint(0,1)
      if step_x == 1:
          x.append(x[j] + 1 + 0.05*np.random.normal())
      else:
          x.append(x[j] - 1 + 0.05*np.random.normal())

  y = [0.05*np.random.normal() for j in range(len(x))]

  trace1 = go.Scatter(
      x=x,
      y=y,
      mode='markers',
      name='Random Walk in 1D',
      marker=dict(
          color=[i for i in range(len(x))],
          size=7,
          colorscale=[[0, 'rgb(178,10,28)'], [0.50, 'rgb(245,160,105)'],
                      [0.66, 'rgb(245,195,157)'], [1, 'rgb(220,220,220)']],
          showscale=True,
      )
  )

  layout = go.Layout(
      yaxis=dict(
          range=[-1, 1]
      )
  )

  data = [trace1]
  fig= go.Figure(data=data, layout=layout)
  py.iplot(fig, filename='random-walk-1d')
elif person.motivated():
#code function to be added
  person.code
else:
#sleep function yet to come: Been a bit lazy *.*
#code and sleep to be available in activities.py 
  person.sleep
  
  
  
  
