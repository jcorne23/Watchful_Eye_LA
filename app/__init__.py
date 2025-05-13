import os 
import random 
import sqlalchemy 
from sqlalchemy import text
from yaml import load, Loader 
from flask import Flask, render_template, request
app = Flask(__name__)

def init_connect_engine():
    if os.environ.get('GAE_ENV') != 'standard': #a file that will appear on GCP 
        variables = load(open("app.yaml"), Loader=Loader)
        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername = "mysql+pymysql",
            username = os.environ.get('MYSQL_USER'),
            password = os.environ.get('MYSQL_PASSWORD'), 
            database = os.environ.get('MYSQL_DB'), 
            host = os.environ.get('MYSQL_HOST'),
            port=3306,  # Replace with your MySQL port
            query={"charset": "utf8"}
        )
    )
    return pool 

db = init_connect_engine()
#conn = db.connect()


#query = text("""
#        SELECT COUNT(*), Victim_Sex 
#        FROM Cases 
#        NATURAL JOIN Victim 
#        WHERE Victim_Age > 18 AND Victim_age < 21 
#        GROUP BY Victim_Sex 
#       ORDER BY Victim_Sex
#   """)
    
    # Execute the SQL expression
#results = conn.execute(query)

#results = conn.execute("SELECT COUNT(*), Victim_Sex FROM Cases NATURAL JOIN Victim WHERE Victim_Age > 18 AND Victim_age < 21 GROUP BY Victim_Sex ORDER BY Victim_Sex;").fetchall()
#print([x for x in results])
#conn.close()
@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        crime_code = request.form.get("crime_code")
        location = request.form.get("location")
        weapon = request.form.get("weapon")
        result_count = int(request.form.get('result_count', 10))  # Default to 10 if not selected

        print(weapon)
        print(crime_code)
        print(location)
        if (not crime_code and not location and not weapon):
            query = text(f"""
            SELECT  Crime_Code_Desc, Area_Name, Weapon_Code_Desc, Victim_Age, Victim_Sex, Date_Occurred
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            LIMIT {result_count}
            """)   
            long = text(f"""
            SELECT Longitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            LIMIT {result_count}         
            """)    

            lat = text(f"""
            SELECT Latitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            LIMIT {result_count}  """)  

        if(crime_code and not location and not weapon):
            query = text(f"""
            SELECT  Crime_Code_Desc, Area_Name, Weapon_Code_Desc, Victim_Age, Victim_Sex, Date_Occurred
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Crime_Code_Desc = "{crime_code}" 
            LIMIT {result_count}
            """)    
            #query for returning longittude and latitude from the main query 
            long = text(f"""
            SELECT Longitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE  Crime_Code_Desc = "{crime_code}" 
            LIMIT {result_count}         
            """)    

            lat = text(f"""
            SELECT Latitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE  Crime_Code_Desc = "{crime_code}" 
            LIMIT {result_count}         
            """) 

        if(not crime_code and location and not weapon):
            query = text(f"""
            SELECT  Crime_Code_Desc, Area_Name, Weapon_Code_Desc, Victim_Age, Victim_Sex, Date_Occurred
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" 
            LIMIT {result_count}
            """)    
            #query for returning longittude and latitude from the main query 
            long = text(f"""
            SELECT Longitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" 
            LIMIT {result_count}         
            """)    

            lat = text(f"""
            SELECT Latitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" 
            LIMIT {result_count}         
            """)     
        
        if(not crime_code and not location and weapon):

            query = text(f"""
            SELECT  Crime_Code_Desc, Area_Name, Weapon_Code_Desc, Victim_Age, Victim_Sex, Date_Occurred
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}
            """)    
            #query for returning longittude and latitude from the main query 
            long = text(f"""
            SELECT Longitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}         
            """)    

            lat = text(f"""
            SELECT Latitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}         
            """) 
        if(crime_code and location and not weapon):
            query = text(f"""
            SELECT  Crime_Code_Desc, Area_Name, Weapon_Code_Desc, Victim_Age, Victim_Sex, Date_Occurred
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" AND Crime_Code_Desc = "{crime_code}" 
            LIMIT {result_count}
            """)    
            #query for returning longittude and latitude from the main query 
            long = text(f"""
            SELECT Longitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" AND Crime_Code_Desc = "{crime_code}" 
            LIMIT {result_count}         
            """)    

            lat = text(f"""
            SELECT Latitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" AND Crime_Code_Desc = "{crime_code}" 
            LIMIT {result_count}         
            """)

        if(crime_code and not location and weapon):
            query = text(f"""
            SELECT  Crime_Code_Desc, Area_Name, Weapon_Code_Desc, Victim_Age, Victim_Sex, Date_Occurred
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Crime_Code_Desc = "{crime_code}" AND Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}
            """)    
            #query for returning longittude and latitude from the main query 
            long = text(f"""
            SELECT Longitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Crime_Code_Desc = "{crime_code}" AND Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}         
            """)    

            lat = text(f"""
            SELECT Latitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Crime_Code_Desc = "{crime_code}" AND Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}         
            """)         
            
        if(not crime_code and location and weapon):
            query = text(f"""
            SELECT  Crime_Code_Desc, Area_Name, Weapon_Code_Desc, Victim_Age, Victim_Sex, Date_Occurred
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}"  AND Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}
            """)    
            #query for returning longittude and latitude from the main query 
            long = text(f"""
            SELECT Longitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" AND Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}         
            """)    

            lat = text(f"""
            SELECT Latitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" AND Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}         
            """)         

        if(crime_code and location and weapon):
            query = text(f"""
            SELECT  Crime_Code_Desc, Area_Name, Weapon_Code_Desc, Victim_Age, Victim_Sex, Date_Occurred
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" AND Crime_Code_Desc = "{crime_code}" AND Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}
            """)    
            #query for returning longittude and latitude from the main query 
            long = text(f"""
            SELECT Longitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" AND Crime_Code_Desc = "{crime_code}" AND Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}         
            """)    

            lat = text(f"""
            SELECT Latitude
            FROM Cases NATURAL JOIN Weapons NATURAL JOIN Location NATURAL JOIN Victim NATURAL JOIN CrimeCodes
            WHERE Area_name = "{location}" AND Crime_Code_Desc = "{crime_code}" AND Weapon_Code_Desc = "{weapon}"
            LIMIT {result_count}         
            """)         

        results = db.connect().execute(query).fetchall()
        longitude = db.connect().execute(long).fetchall()
        latitude = db.connect().execute(lat).fetchall()
        longitude = listhelper(longitude)
        latitude = listhelper(latitude)

        #lower_limit = 0.1
        #upper_limit = 0.5

        #longitude = [x + random.uniform(lower_limit, upper_limit) for x in longitude]
        #latitude = [x + random.uniform(lower_limit, upper_limit) for x in latitude]

        coordinates = [{'lat': lat, 'lng': lng} for lat, lng in zip(latitude, longitude)]
        print(coordinates)
        print(longitude)
        print(latitude)
        


        return render_template("index.html", results=results, location=location, crime_code=crime_code, weapon = weapon, coordinates = coordinates, result_count = result_count)
            

    return render_template("index.html")


@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/funfacts')
def funfacts():
    return render_template('funfacts.html')


def listhelper(x):
    newx = []
    for i in range(len(x)):
        newx.append(float(x[i][0]))
    return newx





#we will have to create a homepage for the stored procedure to run
#report a crime for the fields with CRUD reequirement 
#for delete we will have the possibility to delete 
