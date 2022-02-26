import pickle
import joblib,os
import streamlit as st


def model(model_file):
	return joblib.load(open(os.path.join(model_file),"rb"))

def main():
    st.title("Weekly walmartsaes prediction")
    st.write("---")
    st.header('Enter values')
    col1, col2, col3 = st.columns(3)
    with col1:
        Store = st.number_input("Store", help="Store")
    with col2:
        Dept = st.number_input("Dept", help="Department")
    with col3:
        Year = st.number_input("Year", help="Year")
    col4, col5, col6 = st.columns(3)
    with col4:
        Month = st.number_input("Month", help="Month")
    with col5:
        Day = st.number_input("Day", help="Day")
    with col6:
        IsHoliday = st.number_input('IsHoliday', help="Whether the day is holiday or no")
    col7, col8, col9 = st.columns(3)
    with col7:
        Temperature = st.number_input("Temperature", help="Temperature") 
    with col8:
        Fuel_Price = st.number_input('Fuel_Price', help="Fuel Price")
    with col9:
        MarkDown1 = st.number_input('MarkDown1', help="MarkDown1")
    col10, col11, col12 = st.columns(3)
    with col10:
        MarkDown2 = st.number_input('MarkDown2', help="MarkDown2")
    with col11:
        MarkDown3= st.number_input('MarkDown3', help="MarkDown3")
    with col12:
        MarkDown4 = st.number_input('MarkDown4', help="MarkDown4")
    col13, col14, col15 = st.columns(3)
    with col13:
        MarkDown5 = st.number_input('MarkDown5', help="MarkDown5")
    with col14:
        CPI= st.number_input('CPI', help="Consumer price index")
    with col15:
        Unemployment = st.number_input('Unemployment', help="Unemployment")
    predict= st.button("Predict")
    if predict:
        model = pickle.load(open('modelradomforest1.pkl', 'rb'))
        prediction= model.predict([[Store,Dept, Year,Month,Day,IsHoliday,Temperature,Fuel_Price,MarkDown1,MarkDown2,MarkDown3,MarkDown4,MarkDown5,CPI,Unemployment]])
        st.header('The Predicted Weekly Sales is {}'.format(prediction*100000))
    
if __name__=='__main__':
    main()