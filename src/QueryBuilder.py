select = {
    "exists": "",
	"columns": [],
	"from": "",
	"subQuery": "",
	"fromAlias": "",
	"joins": [],
	"where": "",
	"groupBy": [],
	"orderBy": [],
	"limit": "",
	"offset": "",
    "insertvalue": ""
}

class QueryBuilder():

    def __init__(self):
        self.query = ""
        self.selectdict = select.copy()
    
    def columns(self, columns):
        self.selectdict["columns"] = columns
    
    def from_table(self, table):
        self.selectdict["from"] = table
    
    def where(self, where):
        self.selectdict["where"] = where
    
    def value(self, value):
        self.selectdict["insertvalue"] = value
        
    def build_select(self):
        self.query = ""
        if len(self.selectdict["columns"]) > 0:
            self.query = "SELECT " + ', '.join(self.selectdict["columns"])
        if self.selectdict["from"]:
            self.query += " FROM " + self.selectdict["from"]
        if self.selectdict["where"]:
            self.query += " WHERE " + " ".join([self.selectdict["where"][0],self.selectdict["where"][1],"'" + self.selectdict["where"][2] + "'"])
        return self.query
    
    def build_insert(self):
        self.query = "INSERT INTO "
        if self.selectdict["from"]:
            self.query += self.selectdict["from"]
        if self.selectdict["insertvalue"]:
            values = list(self.selectdict["insertvalue"])
            values[2] = "'" + values[2].strftime("%Y-%m-%d %H:%M:%S") + "'"
            values[1] = "'" + values[1] + "'"
            values[0] = str(values[0])
            print(values)
            self.query += " VALUES (" + ",".join(values) + ")"
        return self.query