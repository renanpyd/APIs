# API_Relatorio_GA_Visualization

# DATAFRAME
body = body = {'reportRequests': [{'viewId': your_view_id, 
                            'dateRanges': [{'startDate': '2021-01-01', 'endDate': '2021-04-30'}],
                            'metrics': [{'expression': 'ga:users'}], 
                            'dimensions': [{'name': 'ga:yearMonth'}],
                            "pivots": [{"dimensions": [{"name": "ga:channelGrouping"}],
                                        "metrics": [{"expression": "ga:users"},
                                                    {"expression": "ga:bounceRate"}]
                                       }]
                          }]}
						  
# BAR PLOT
import matplotlib.pyplot as plt
import seaborn as sns

# setando estilo seaborn
sns.set_theme()
sns.set(rc={'figure.figsize':(8,6)})

plot_data = report.loc[:, (slice(None), "ga:users")].iloc[:, 1:] # Escolha colunas de usuários, solte a primeira (soma)
plot_data.columns = plot_data.columns.get_level_values(0)
plot_data.index = plot_data.index.get_level_values(0)
plot_data.plot.bar(stacked = True);						  
						  
plot_data						  
						  
# DATAFRAME
body = body = {'reportRequests': [{'viewId': your_view_id, 
                            'dateRanges': [{'startDate': '2021-01-01', 'endDate': '2021-04-30'}],
                            'metrics': [{'expression': 'ga:sessions'},
                                        {"expression": "ga:avgSessionDuration"},
                                        {"expression": "ga:users"},
                                        {"expression": "ga:newUsers"}],
                            'dimensions': [{'name': 'ga:date'},
                                           {"name": "ga:channelGrouping"}],
                          }]}

report = run_report(body, ga_keys).reset_index() # o índice é transformado em colunas para ajudar na visualização
report						  
						  
# LINE PLOT
sns.set(rc={'figure.figsize':(12,8)})
plot_data = report.loc[:, ["ga:users"]]
sns.lineplot(data = report, y = "ga:sessions", x = 'ga:date', hue = 'ga:channelGrouping');						  
						  
						  
						  
						  
						  
						  
						  
						  
						  