import re

#https://stackoverflow.com/questions/1007481/how-do-i-replace-whitespaces-with-underscore-and-vice-versa
def urlify(query):
	query = re.sub(r"[^\w\s]", '', query)
	query = re.sub(r"\s+", '+', query)
	return query
