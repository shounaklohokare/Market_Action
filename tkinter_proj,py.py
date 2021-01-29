from tkinter import *
from bs4 import BeautifulSoup
import requests

 

class market_action:



	def market_act(self):

		url = requests.get('https://www.moneycontrol.com/')
		soup = BeautifulSoup(url.text, 'lxml')

		tables = soup.find_all('table',class_='rhsglTbl')

		try :
			self.root.destroy()

		except:
			pass

		self.root = Tk()

		indices = tables[1]
		index_values = []
		for tr in indices.find_all('tr'):
			index_values.append(tr.b.text)

		most_active = tables[3]
		most_active_values = []

		for tr in most_active.find_all('tr')[1:]:
			x=[tr.find_all('td')[2].text]
			x.insert(0,tr.find_all('td')[1].b.text)
			x.insert(0, tr.td.a.text)
			most_active_values.append(x)


		top_gainers = tables[5]
		top_gainers_values = []
		for tr in top_gainers.find_all('tr')[1:]:
			x=[i.text for i in tr.find_all('td')[2:]]
			x.insert(0,tr.find_all('td')[1].b.text)
			x.insert(0, tr.td.a.text)
			top_gainers_values.append(x)


		top_losers = tables[7]
		top_losers_values = []
		for tr in top_losers.find_all('tr')[1:]:
			x=[i.text for i in tr.find_all('td')[2:]]
			x.insert(0,tr.find_all('td')[1].b.text)
			x.insert(0, tr.td.a.text)
			top_losers_values.append(x)

		# print(top_losers_values)
		color = 'light yellow'
		text_color = 'gray30'
		font_ = ('Helvetica', '9')
		self.root.title('MARKET ACTION')
		self.root.geometry('585x670')
		self.root.configure(bg=color)

		indices = LabelFrame(self.root, text='Indices')
		indices.grid(row=0, column=0)

		indices.configure(bg=color)

		nifty = Label(indices, text=f'Nifty\n{index_values[0]}', bd=5, bg=color, fg=text_color, font=font_, padx=10, pady=10)
		nifty.grid(row=0, column=0)

		bse_sensex = Label(indices, text=f'BSE Sensex\n{index_values[1]}', bd=5, bg=color, fg=text_color, font=font_,padx=10, pady=10)
		bse_sensex.grid(row=0, column=1)

		nifty_bank =  Label(indices, text=f'Nifty Bank\n{index_values[2]}', bd=5, bg=color,fg=text_color, font=font_,padx=10, pady=10)
		nifty_bank.grid(row=0, column=2)

		nifty_it = Label(indices, text=f'Nifty IT\n{index_values[3]}', bd=5, bg=color,fg=text_color, font=font_,padx=10, pady=10)
		nifty_it.grid(row=0, column=3)

		bse_smallcap = Label(indices, text=f'BSE SmallCap\n{index_values[4]}', bd=5, bg=color, fg=text_color,font=font_,padx=8, pady=10)
		bse_smallcap.grid(row=0, column=4)

		bse_midcap = Label(indices, text=f'BSE MidCap\n{index_values[5]}', bd=5, bg=color,fg=text_color, font=font_, padx=8, pady=10)
		bse_midcap.grid(row=1, column=0)

		nifty_auto = Label(indices, text=f'Nifty Auto\n{index_values[6]}', bd=5, bg=color, fg=text_color, font=font_,padx=8, pady=10)
		nifty_auto.grid(row=1, column=1)

		bse_capgoods = Label(indices, text=f'BSE Cap Goods\n{index_values[7]}', bd=5, bg=color, fg=text_color,font=font_,padx=7, pady=10)
		bse_capgoods.grid(row=1, column=2)


		bse_consdurable = Label(indices, text=f'BSE Cons Durable\n{index_values[8]}', bd=5, bg=color,fg=text_color,font=font_, padx=7, pady=10)
		bse_consdurable.grid(row=1, column=3)

		bse_fmcg = Label(indices, text=f'BSE FMCG\n{index_values[9]}', bd=5, bg=color, fg=text_color,font=font_,padx=8, pady=10)
		bse_fmcg.grid(row=1, column=4)

		bse_healthcare = Label(indices, text=f'BSE Health Care\n{index_values[10]}', bd=5, bg=color,fg=text_color,  font=font_,padx=7, pady=10)
		bse_healthcare.grid(row=2, column=0)

		bse_metals = Label(indices, text=f'BSE Cap Goods\n{index_values[11]}', bd=5, bg=color,fg=text_color, font=font_, padx=7, pady=10)
		bse_metals.grid(row=2, column=1)

		bse_oilngas = Label(indices, text=f'BSE Oil & Gas\n{index_values[12]}', bd=5, bg=color,fg=text_color, font=font_,padx=6, pady=10)
		bse_oilngas.grid(row=2, column=2)

		bse_teck = Label(indices, text=f'BSE Teck\n{index_values[13]}', bd=5, bg=color,fg=text_color,font=font_, padx=8, pady=10)
		bse_teck.grid(row=2, column=3)

		nifty_pse = Label(indices, text=f'Nifty PSE\n{index_values[14]}', bd=5, bg=color, fg=text_color, font=font_,padx=8, pady=10)
		nifty_pse.grid(row=2, column=4)


		most_active = LabelFrame(self.root, text='Most Active')
		most_active.grid(row=1, column=0)


		most_active.configure(bg=color)

		t=Label(most_active, text='Name\n\nLTP\n\nChange', bd=5, bg=color,fg=text_color, font=font_,padx=10, pady=10)
		t.grid(row=0,column=0)

		ma1 = Label(most_active, text="{}".format('\n\n'.join(most_active_values[0])), bd=5, bg=color,fg=text_color,font=font_, padx=10, pady=10)
		ma1.grid(row=0, column=1)

		ma2 = Label(most_active, text="{}".format('\n\n'.join(most_active_values[1])), bd=5, bg=color, fg=text_color, font=font_,padx=10, pady=10)
		ma2.grid(row=0, column=2)

		ma3 =  Label(most_active, text="{}".format('\n\n'.join(most_active_values[2])), bd=5, bg=color,fg=text_color, font=font_, padx=10, pady=10)
		ma3.grid(row=0, column=3)

		ma4 = Label(most_active, text="{}".format('\n\n'.join(most_active_values[3])), bd=5, bg=color,fg=text_color, font=font_, padx=10, pady=10)
		ma4.grid(row=0, column=4)

		ma5 = Label(most_active, text="{}".format('\n\n'.join(most_active_values[4])), bd=5, bg=color,fg=text_color, font=font_,padx=8, pady=10)
		ma5.grid(row=0, column=5)



		top_gainers = LabelFrame(self.root, text='Top Gainers')
		top_gainers.grid(row=2,column=0)

		top_gainers.configure(bg=color)

		t=Label(top_gainers, text='Name\n\nLTP\n\nChange\n\n%Gain', bd=5, bg=color, fg=text_color,font=font_,padx=10, pady=10)
		t.grid(row=0,column=0)

		ma1 = Label(top_gainers, text="{}".format('\n\n'.join(top_gainers_values[0])), bd=5, bg=color,fg=text_color, font=font_,padx=10, pady=10)
		ma1.grid(row=0, column=1)

		ma2 = Label(top_gainers, text="{}".format('\n\n'.join(top_gainers_values[1])), bd=5, bg=color,fg=text_color, font=font_,padx=10, pady=10)
		ma2.grid(row=0, column=2)

		ma3 =  Label(top_gainers, text="{}".format('\n\n'.join(top_gainers_values[2])), bd=5, bg=color,fg=text_color,font=font_, padx=10, pady=10)
		ma3.grid(row=0, column=3)

		ma4 = Label(top_gainers, text="{}".format('\n\n'.join(top_gainers_values[3])), bd=5, bg=color,fg=text_color,font=font_, padx=10, pady=10)
		ma4.grid(row=0, column=4)

		ma5 = Label(top_gainers, text="{}".format('\n\n'.join(top_gainers_values[4])), bd=5, bg=color,fg=text_color, font=font_,padx=8, pady=10)
		ma5.grid(row=0, column=5)


		top_losers = LabelFrame(self.root, text='Top Losers', fg=text_color)
		top_losers.grid(row=3, column=0)


		top_losers.configure(bg=color)

		t=Label(top_losers, text='Name\n\nLTP\n\nChange\n\n%Gain', bd=5, bg=color,fg=text_color,font=font_, padx=10, pady=10)
		t.grid(row=0,column=0)

		ma1 = Label(top_losers, text="{}".format('\n\n'.join(top_losers_values[0])), bd=5, bg=color,fg=text_color,font=font_, padx=10, pady=10)
		ma1.grid(row=0, column=1)

		ma2 = Label(top_losers, text="{}".format('\n\n'.join(top_losers_values[1])), bd=5, bg=color, fg=text_color,font=font_,padx=10, pady=10)
		ma2.grid(row=0, column=2)

		ma3 =  Label(top_losers, text="{}".format('\n\n'.join(top_losers_values[2])), bd=5, bg=color,fg=text_color,font=font_, padx=10, pady=10)
		ma3.grid(row=0, column=3)

		ma4 = Label(top_losers, text="{}".format('\n\n'.join(top_losers_values[3])), bd=5, bg=color,fg=text_color,font=font_, padx=10, pady=10)
		ma4.grid(row=0, column=4)

		ma5 = Label(top_losers, text="{}".format('\n\n'.join(top_losers_values[4])), bd=5, bg=color, fg=text_color,font=font_,padx=8, pady=10)
		ma5.grid(row=0, column=5)


		refresh = Button(self.root, text='Refresh',bd=5, fg='gray31', bg='bisque2',activebackground='azure',relief = GROOVE, command=self.market_act)
		refresh.grid(row=4, column=0)

		self.root.mainloop()


obj = market_action()
obj.market_act()