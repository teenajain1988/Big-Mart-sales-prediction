import numpy as np
from flask import Flask, request, render_template
import pickle
import numpy as np


app = Flask(__name__)



@app.route("/",methods=["GET"])
def home_page():
    return render_template("home.html")

@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method=="POST":

        item_weight=float(request.form["item_weight"])
        item_visibility=float(request.form["item_visibility"])
        item_mrp = float(request.form["item_mrp"])

        outlet_size = request.form["outlet_size"]
        if outlet_size=="Small":
            outlet_size=1
        elif outlet_size=="Medium":
            outlet_size=2
        elif outlet_size=="High":
            outlet_size=3

        item_fat_content = request.form["Item_Fat_Content"]
        Low_Fat = Regular = Non_Edible = 0

        if item_fat_content=="Low Fat":
            Low_Fat=1

        elif item_fat_content=="Regular":
            Regular=1

        else:
            Non_Edible=1

        item_identifier = request.form["Item_Identifier"]
        Drink = Food = Non_Consumable = 0

        if item_identifier == "Drink":
            Drink=1
        elif item_identifier == "Food":
            Food=1
        else:
            Non_Consumable=1

        item_type = request.form["Item_Type"]
        Baking_Goods =  Canned = Dairy = Frozen_Foods = Fruits_Vegetables = 0
        health_hygiene = household = meat = snack_foods = soft_drink = others = 0
        if item_type == "Baking Goods":
            Baking_Goods = 1
        elif item_type == "Canned":
            Canned=1
        elif item_type == "Dairy":
            Dairy=1
        elif item_type == "Frozen Foods":
            Frozen_Foods=1
        elif item_type == "Fruits and Vegetables":
            Fruits_Vegetables=1
        elif item_type == "Health and Hygiene":
            health_hygiene = 1
        elif item_type == "Household":
            household = 1
        elif item_type == "Meat":
            meat = 1
        elif item_type == "Snack Foods":
            snack_foods = 1
        elif item_type == "Soft Drink":
            soft_drink = 1
        elif item_type == "Others":
            others = 1

        outlet_location_type = request.form["Outlet Location Type"]
        Tier1 = Tier2 = Tier3 = 0
        if outlet_location_type == "Tier1":
            Tier1=1
        elif outlet_location_type == "Tier2":
            Tier2=1
        else:
            Tier3 = 1

        outlet_type = request.form["Outlet Type"]
        Grocery_Store = SuperMarketType1 = SuperMarketType2 = SuperMarketType3 = 0
        if outlet_type == "Grocery Store":
            Grocery_Store = 1
        elif outlet_type == "SuperMarket Type1":
            SuperMarketType1 = 1
        elif outlet_type == "SuperMarket Type2":
            SuperMarketType2 = 1
        else:
            SuperMarketType3= 1

        outlet_identifier = request.form["Outlet Identifier"]
        OUT010 = OUT013 = OUT017 =  OUT018 = OUT019 = OUT027 = OUT035 = OUT045 = OUT046 = OUT049 = 0
        if outlet_identifier == "OUT010":
            OUT010 = 1
        elif outlet_identifier == "OUT013":
            OUT013 = 1
        elif outlet_identifier == "OUT017":
            OUT017 = 1
        elif outlet_identifier == "OUT018":
            OUT018 = 1
        elif outlet_identifier == "OUT019":
            OUT019 = 1
        elif outlet_identifier == "OUT027":
            OUT027 = 1
        elif outlet_identifier == "OUT035":
            OUT035 = 1
        elif outlet_identifier == "OUT045":
            OUT045 = 1
        elif outlet_identifier == "OUT046":
            OUT046 = 1
        else:
            OUT049 = 1

        f2 = open("big_mart.pickle", "rb")
        model = pickle.load(f2)

        result=model.predict([[item_weight,
        item_visibility,
        item_mrp,
        outlet_size,
        Non_Edible,
        Low_Fat,
        Regular,
        Drink,
        Food,
        Non_Consumable,
        Baking_Goods,
        Canned,
        Dairy,
        Frozen_Foods,
        Fruits_Vegetables,
        health_hygiene,
        household,
        meat,
        snack_foods,
        soft_drink,
        others,
        Tier1,
        Tier2,
        Tier3,
        Grocery_Store,
        SuperMarketType1,
        SuperMarketType2,
        SuperMarketType3,
        OUT010,
        OUT013,
        OUT017,
        OUT018,
        OUT019,
        OUT027,
        OUT035,
        OUT045,
        OUT046,
        OUT049]])

        result=np.exp(result[0])-1

        return render_template("home.html",result="Your item outlet sale is  {}".format(result))

    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run()