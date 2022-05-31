def parser():
	f = open("periodic_table.txt", "r")
	periodic_table = []
	list = []
	for line in f.readlines():
		list.append(line[0:line.find(' ')])
		list.append(line[line.find(":")+1:line.find(", number:")])
		list.append(line[line.find("ber:")+4:line.find(", small:")])
		list.append(line[line.find("all:")+4:line.find(", molar:")])
		list.append(line[line.find("lar:")+4:line.find(", electron:")])
		list.append(line[line.find("tron:")+5:line.find("\n")])
		periodic_table.append(list)
		list = []
	print(periodic_table)

	HTML = """
		<html>
		<head>
		<title>periodic_table</title>
		<style>
			ul {
			list-style:none;
			padding-left:0px;
			}
		</style>
		</head>
		<body>
		<table>
	"""
	body =''
	
	for i in range(len(periodic_table)):


		if int(periodic_table[i][1]) == 0:
			body +=	'<tr>'
		if i > 0 and int(periodic_table[i][1]) - int(periodic_table[i-1][1]) != 1:
			cnt = int(periodic_table[i][1]) - int(periodic_table[i-1][1])
			for j in range(cnt - 1):	
				body+='<td></td>\n'
		body +=	'<td style="border: 1px solid black;					padding:10px">'
		body += f'<h4>{periodic_table [i][0]}</h4>\n'
		body +=	'<ul>\n'
		body += f'<li>No {periodic_table [i][2]}</li>\n'
		body += f'<li>{periodic_table [i][3]}</li>\n'
		body += f'<li>{periodic_table [i][4]}</li>\n'
		body +=	f'<li>{periodic_table [i][5]} electron</li>\n'
		body += '<ul>\n'
		body += '</td>\n'
		if int(periodic_table[i][1]) == 17:
			body += '</tr>\n'
		
	end = """</table></body></html>
	"""
	f = open("periodic_table.html", "w")
	f.write(HTML)
	f.write(body)
	f.write(end)	
	f.close() 

if __name__ == '__main__':
    parser()