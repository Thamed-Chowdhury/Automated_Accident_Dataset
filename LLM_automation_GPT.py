def create_data(description):
    print("Running THis Script")
    print("Length of description is: ", len(description))
    from langchain_core.prompts import ChatPromptTemplate  ### To create a chatbot, chatprompttemplate used
    from langchain_openai import ChatOpenAI ##### For using chat openai features
    from langchain_core.output_parsers import StrOutputParser  ### Default output parser. Custom parser can also be created
    from langchain_community.llms import ollama ### Importing ollama

    
    import os
    from dotenv import load_dotenv
    import pandas as pd


    load_dotenv()

    ### Set all api keys:
    os.environ["OPENAI_API_KEY"]="ENTER YOUR OPENAI API KEY HERE"
    ### Create Prompt Template:
    prompt=ChatPromptTemplate.from_messages(
        {
            ("system", "You are a helpful assistant, please respond to the queries"), ### We need both system and users in prompt
            ("user","question: {question}")
        }
    )

    #### Create OpenAI llm:
    llm=ChatOpenAI(model="gpt-4o")

    ### Create an output parser:
    output_parser=StrOutputParser()

    #### Creating chain: The concept is- output of action before | symbol will be passed as input in action after the symbol.
    #### Here we have created three actions: The prompt, llm and output parser:
    chain=prompt|llm|output_parser

    df = description
    df = df.fillna(0)
    dj=[]
    for i in range(len(df)):
        dj.append(chain.invoke({"question" : df['Description'][i]+" Is the news about road accident? If no, then reply 'General'. Else if the news is about road accident then check if the news is referring to a specific accident incident or accident in general? Answer only in a word: Either specific or general."}))
        
    df2=df.copy()
    df2['Report Type']=dj
    def drp(p):
        df2.drop([p],inplace=True)

    ### Removing the general accident types:
    for p in range(len(df)):
        if "General" in df2['Report Type'][p]:
            drp(p)
            
    ### Reseting index of df3:
    df2.reset_index(drop=True,inplace=True)

    ### Now finding column values using llm:
    ### A function to invoke the llm. For some reason phi3 doesn't give accurate result sometimes if used directly in dj.append()
    def res(i):
        response=chain.invoke({"question" : df2['Description'][i]+f"""Provide only the answers of the following question seperated by a comma only and your answers MUST BE IN ENGLISH:
                            If the news was published on {df2['Publish Date'][i]}, what is the date of accident occurrence? The date must be in Day-Month-Year format. Be careful because publish date and accident occurrence date may or may not be the same. Try to deduce correct accident date and do not include Saturday Sunday etc in your date. Only numerics are needed,
                            Time of Accident occured, How many people were killed in the accident in numeric number?, 
                            How many people were injured in the accident in numeric number?, 
                            Location of the accident, 
                            Type of road where accident occured, 
                            Was there any pedestrian involved?,  
                            Do not include any other sentences except the answers seperated by comma only, 
                            if you cannot find or deduce a answer simply put 'Not Available' in place of it. 
                            If a report mentions more than one specific accident incidents only consider the 1st accident incident and ignore the second one""" })
        return response
    #### dj2 list contains all column values seperated by comma:
    dj2=[]

    for i in range(len(df2)):
        dj2.append(res(i))
    ### Finding vehicle
    def res2(i):
        response=chain.invoke({"question" : df2['Date + Desc'][i]+" Only name the type of vehicles involved in the accident. If multiple vehicles are involved, seperate them by hyphens(-). Example answers: Bus, Truck-Bus etc. If no vehicles are mentioned, your answer will be: Not Available. Your answer should only contain the vehicle name, do not include any extra sentences"})
        return response
    #### vehicle list contains all vehicles involved:
    vehicles=[]

    for i in range(len(df2)):
        vehicles.append(res2(i))
   



    ### Splitting dj2 string based on comma position:
    Date=[]
    Time=[]
    Killed=[]
    Injured=[]
    Location=[]
    Road_Characteristic=[]
    Pedestrian_Involved=[]
    #Vehicles_involved=[]

    for i in range(len(dj2)):
        words = dj2[i].split(",")  # Splitting at the comma delimiter
        #print(f"Date: {words[0]}")
        Date.append(words[0])
            
        #print(f"Time: {words[1]}")
        Time.append(words[1])
            
        #print(f"Casualities: {words[2]}")
        Killed.append(words[2])
        Injured.append(words[3])
        Location.append(words[4])
        Road_Characteristic.append(words[5])
        Pedestrian_Involved.append(words[6])
        #Vehicles_involved.append(words[7])

    #### Probable type of final dataframe:
    df2["Accident Date"]=Date
    df2["Time"]=Time
    df2["Killed"]=Killed
    df2["Injured"]=Injured
    df2["Location"]=Location
    df2["Road_Characteristic"]=Road_Characteristic
    df2["Pedestrian_Involved"]=Pedestrian_Involved
    df2["Vehicles Involved"]=vehicles
    df3=df2.drop(columns=['Description','Date + Desc','Report Type'])
    return df3
   