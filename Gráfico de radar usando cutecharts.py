```python
!pip install cutecharts
```

    Collecting cutecharts
      Downloading cutecharts-1.2.0-py3-none-any.whl (17 kB)
    Requirement already satisfied: jinja2 in c:\users\angel\anaconda3\lib\site-packages (from cutecharts) (2.11.3)
    Requirement already satisfied: MarkupSafe>=0.23 in c:\users\angel\anaconda3\lib\site-packages (from jinja2->cutecharts) (1.1.1)
    Installing collected packages: cutecharts
    Successfully installed cutecharts-1.2.0
    


```python
import pandas as pd
import cutecharts.charts as ctc
```


```python
data = {'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
       'This week': [12, 10, 9, 9, 10, 3, 3],
        'Last week': [15, 12, 8, 9, 11, 4, 3]
       }
df_coffee = pd.DataFrame(data, columns = ['Day', 'This week', 'Last week'])
```


```python
chart = ctc.Radar('Cup of coffe consumed per day')
chart.set_options(
    labels=list(df_coffee['Day']),
    is_show_legend=True,
    legend_pos='upRight'
    )
chart.add_series('This Week', list(df_coffee['This week']))
chart.add_series('Last Week', list(df_coffee['Last week']))
```




    <cutecharts.charts.radar.Radar at 0x1fcd50b69d0>




```python
chart.render_notebook()
```





<script>
    require.config({
        paths: {
            'chartXkcd':'https://cdn.jsdelivr.net/npm/chart.xkcd@1.1/dist/chart.xkcd.min'
        }
    });
</script>

<div id="891bdeeab2f14924b71695043fe242df" class="chart-container" style="width: 800px">
        <svg id="chart_891bdeeab2f14924b71695043fe242df"></svg>
    </div>
    <script>
        require(['chartXkcd'], function(chartXkcd) {
            const svg_891bdeeab2f14924b71695043fe242df = document.querySelector('#chart_891bdeeab2f14924b71695043fe242df')
            const chart_891bdeeab2f14924b71695043fe242df = new chartXkcd.Radar(svg_891bdeeab2f14924b71695043fe242df, {"title": "Cup of coffe consumed per day", "data": {"datasets": [{"label": "This Week", "data": [12, 10, 9, 9, 10, 3, 3]}, {"label": "Last Week", "data": [15, 12, 8, 9, 11, 4, 3]}], "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]}, "options": {"showLegend": true, "showLabel": true, "tickCount": 3, "legendPosition": 2}});
        })
    </script>





```python

```
