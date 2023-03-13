from linkedin_api import Linkedin
from pprint import pprint
import streamlit as st
    
# Authenticate using any Linkedin account credentials
api = Linkedin('akabhiaryan1@gmail.com','SamplePass1')
st.title('ESG Scorecard')
st.text('This is a web app to pull social media data and analyze ESG scorecard of comapnies')

key_words =['sustainability','sustainable','esg','environmental social governanace','Sustainability','Environmental','Social','Governance','Corporate responsibility','Ethical investing','Climate change','Green ','finance','Socially responsible investing','ESG performance','Impact investing','Sustainable development','Carbon footprint','Stakeholder ','engagement','Responsible sourcing','Human rights','Diversity and inclusion','Sustainable supply chains','ESG metrics','Sustainability ','reporting']

ESG = ["Environmental, Social, and Governance (ESG) refers to a set of criteria used to assess the performance of companies regarding their impact on the environment, society, and corporate governance practices. ESG has become an increasingly important area of focus for investors, as well as for companies that seek to align their business practices with the needs of stakeholders and the wider society. This document provides an overview of ESG, its importance, and the ways in which it can be incorporated into business practices.","Environmental Factors Environmental factors include the impact of a company’s operations on the environment, including greenhouse gas emissions, waste production, and resource consumption. Companies can improve their ESG performance in this area by adopting sustainable practices, such as reducing energy consumption, implementing renewable energy sources, and reducing waste production. Additionally, companies can invest in research and development to create new technologies and processes that are more environmentally friendly.","Social Factors Social factors refer to a company’s impact on society, including its treatment of employees, community engagement, and human rights practices. Companies can improve their ESG performance in this area by fostering a culture of diversity and inclusion, ensuring fair labor practices, and engaging in philanthropic activities that benefit the communities in which they operate. Companies can also adopt responsible sourcing practices that consider the impact of their supply chain on human rights and social issues.","Governance Factors Governance factors refer to a company’s internal management and decision-making processes, including transparency, accountability, and ethics. Companies can improve their ESG performance in this area by adopting good corporate governance practices, such as establishing independent boards of directors, implementing robust internal controls, and adopting ethical codes of conduct. Additionally, companies can enhance transparency by providing regular reports on their ESG performance to stakeholders.","The Importance of ESG ESG is becoming increasingly important for companies and investors alike. Companies that prioritize ESG are more likely to attract and retain customers, employees, and investors who are concerned about the impact of business practices on the environment and society. Additionally, companies that prioritize ESG are better positioned to anticipate and mitigate risks related to environmental and social issues, such as climate change, resource scarcity, and labor unrest. For investors, ESG provides a means of evaluating the long-term sustainability and performance of companies, taking into account both financial and non-financial factors.", "Incorporating ESG into Business Practices Companies can incorporate ESG into their business practices in several ways. First, companies can develop ESG policies and procedures that outline their commitment to sustainability, social responsibility, and ethical governance practices. These policies should be communicated to employees, stakeholders, and the wider community to ensure that they are understood and implemented effectively. Second, companies can engage with stakeholders, including investors, customers, employees, and local communities, to understand their expectations and concerns regarding ESG issues. Third, companies can establish metrics and targets to measure and track their ESG performance over time. This data can be used to identify areas for improvement and to report on progress to stakeholders. Finally, companies can integrate ESG considerations into their decision-making processes, including investment decisions, product development, and supply chain management.","Conclusion ESG is an increasingly important area of focus for companies and investors. Companies that prioritize ESG are better positioned to create long-term value, mitigate risks, and meet the expectations of stakeholders. By adopting sustainable practices, engaging with stakeholders, and integrating ESG considerations into decision-making processes, companies can improve their ESG performance and contribute to a more sustainable and equitable future."]



def company_details(company):
    try:
        wf = api.get_company(company)
        return wf
    except KeyError:
        st.text("Invalid keyword - search again [Example : for Wells Fargo, the key is wellsfargo]")
        return -1
        
def main():
#     company = st.text_input("Search Client\n")
    i=1
    while(True):
        company = st.text_input("Search Client or (exit to return)\n",key=i)
        if company == 'exit':
            return
            st.stop()
        else:
            details = company_details(company)
            if details == -1:
                break;
            elif details != -1:
                st.text(details['description'])
        i+=1

if __name__=="__main__":
    
    main()
            
