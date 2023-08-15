# Adoptly README  

Adoptly - find your pawfect match

Group project (3) - Python, Django - 1 week timeline

Adoptly was my third project when studying General Assembly.  In our project, Adoptly, we aimed to create a unique and personalised pet adoption app that stood out from existing offerings. Our main focus was on fostering a deep connection between the adopter and the pet even before the adoption process began. We wanted to provide a platform that allowed adopters to engage with pets on a more personal level, understanding their needs and personalities. By creating an immersive and interactive experience, we hoped to inspire and encourage more people to consider adopting pets in need of loving homes.


Deployment link

https://adoptly-renad.fly.dev/

The link above is the deployed App, user must login or signup to be able to view the website.

In the deployed version of Adoptly on Fly.io, users are required to create an account and specify whether they are an adopter or a pet owner. Upon signing up, users are guided through a questionnaire designed to understand their preferences and requirements. This questionnaire serves two purposes:

For Adopters: It helps potential adopters find the perfect breed and pet that suits their lifestyle and preferences. By collecting information about their living situation, activity level, and preferences regarding size, age, and personality, the questionnaire generates tailored recommendations to help users find the most suitable pets for adoption.

For Pet Owners: The questionnaire assists pet owners in building a comprehensive profile for their pets. By gathering details about the pet's breed, age, size, personality traits, and specific needs, owners can create a detailed profile that provides potential adopters with a better understanding of the pet's characteristics and requirements.

By personalising the experience through the questionnaire, Adoptly aims to enhance the connection between adopters and pets, making the adoption process more informed and successful.

Getting Started/Code Installation



Is deployed and code can also found on my github
https://github.com/renad1999/Adoptly


Timeframe & Working Team (Solo/Pair/Group)

Our team of three, consisting of myself, Louise, and Kyle, collaborated on the development of Adoptly. With a tight deadline of just one week, which included the weekend, we dedicated our efforts to ensure the of the app within the given timeframe. As a group project, we divided tasks and responsibilities efficiently between us and were always communicating and helping each other out when needed. Right from the initial planning stage, our team maintained a collaborative and inclusive approach. We actively engaged in brainstorming sessions, where we bounced ideas off each other to shape the direction and features of Adoptly. During this process, we ensured that everyone's opinions and suggestions were respected and taken into consideration.
To facilitate the development process, we created wireframes to visualise the app's layout and flow. Additionally, we developed Entity-Relationship Diagrams (ERDs) to establish the database structure and relationships between different entities within the app(added below).


Throughout this iterative process, our team prioritised open communication and mutual satisfaction. We discussed and deliberated on various aspects, making collective decisions that aimed to accommodate the preferences and needs of each team member. This approach fostered a positive and collaborative environment.


Technologies Used

Instructions
Backend development (Python, Django, PostgreSQL)
Frontend development (HTML, CSS)
Collaborative design (Excalidraw)
Project management (Trello)
Collaboration(GitHub)
Deployment (Fly.io).



Brief

<img width="619" alt="Screenshot 2023-08-15 at 21 19 19" src="https://github.com/renad1999/Adoptly/assets/112344006/193ecf6a-9743-41e1-99a7-059933febd70">

This diagram was our brief for our presentation 

☐ Be a full-stack Django application.
☐ Connect to and perform data operations on a PostgreSQL database (the default SQLLite3 database is not acceptable).

☐ If consuming an API (OPTIONAL), have at least one data entity (Model) in addition to the built-in User model. The related entity can be either a one-to-many (1:M) or a many-to-many (M:M) relationship.

☐ If not consuming an API, have at least two data entities (Models) in addition to the built-in User model. It is preferable to have at least one one-to-many (1:M) and one many-to-many (M:M) relationship between entities/models.

☐ Have full-CRUD data operations across any combination of the app's models (excluding the User model). For example, creating/reading/updating posts and creating/deleting comments qualifies as full-CRUD data operations.

☐ Authenticate users using Django's built-in authentication.

☐ Implement authorization by restricting access to the Creation, Updating & Deletion of data resources using the login_requireddecorator in the case of view functions; or, in the case of class-based views, inheriting from the LoginRequiredMixin class.

☐ Be deployed online using Heroku. Presentations must use the deployed application.

The app may optionally:

☐ Upload images to AWS S3

☐ Consume an API (installation of the Requests package will be necessary)



Planning

Insert your Planning here:



We used Trello as a workspace for us to plan for our project. 
Below are screenshots of our Trello board. We assigned different colours to each person so tasks are clearer. I was in charge of documentation, Louise was Scrum Master and Kyle was GitHub Manager. We had daily stand ups on Zoom to keep eachother updated on what we have achieved the day before, discussing any issues we faced and helping each other out if needed. We were also in contact throughout the day on Slack. Lastly, we tried to keep our Trello board updated also on what task everyone was doing, and when the task was completed we moved it into the completed section on our Trello board.

<img width="616" alt="Screenshot 2023-08-15 at 21 20 19" src="https://github.com/renad1999/Adoptly/assets/112344006/c8992f32-cbee-4d9e-8046-5f881dd6d7aa">

<img width="619" alt="Screenshot 2023-08-15 at 21 20 37" src="https://github.com/renad1999/Adoptly/assets/112344006/07bc6f44-8d38-4686-be80-889309d49e47">

ERD DIAGRAM
The diagram shows the relationship between our models.<img width="627" alt="Screenshot 2023-08-15 at 21 21 03" src="https://github.com/renad1999/Adoptly/assets/112344006/e2cb951b-6d7e-42c6-a94e-51be010457d0">

OUR WIREFRAMES

<img width="619" alt="Screenshot 2023-08-15 at 21 21 30" src="https://github.com/renad1999/Adoptly/assets/112344006/dff9d3c1-3312-4dc6-a701-41842e149b86">

Build/Code Process
<img width="617" alt="Screenshot 2023-08-15 at 21 22 02" src="https://github.com/renad1999/Adoptly/assets/112344006/2bbbe72e-951e-4801-9bd1-e93875d33b6b">



<img width="613" alt="Screenshot 2023-08-15 at 21 22 17" src="https://github.com/renad1999/Adoptly/assets/112344006/0599a861-b237-4c79-8dd5-33ef5673b613">

The code above is a wizard form, it uses the post method for file uploads and includes a CSRF token for security. It iterates through forms and fields within the wizard, displaying each field's label as a button within a labeled <div>, along with error messages, help text, and the field itself. The design logic appears to be complex, with buttons inside labels, possibly used for progressing through the wizard. The code concludes with a submit button and an input element with the ID "pet-pp." The purpose and functionality of the wizard's navigation and overall interaction would require additional context to fully understand.


#! tuples here
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

HEALTH_STATUS_CHOICES = (
    ('Good health', 'Good Health'),
    ('Needs medication', 'Needs Medication'),
    ('Disabled', 'Disabled'),
)

ACTIVITY_LEVEL_CHOICES = (
    ('Low', 'Less than an hour'),
    ('Moderate', 'One to two hours'),
    ('High', 'Two hours minimum'),
)

In the provided code, there are three sets of predefined tuples, each representing different sets of choices. The first tuple, GENDER_CHOICES, contains options for gender, where each option is a tuple with a display value and its corresponding database value. The second tuple, HEALTH_STATUS_CHOICES, includes choices related to health status, again with display and database values. The third tuple, ACTIVITY_LEVEL_CHOICES, offers choices for activity levels, indicating time commitments associated with each level. These tuples are commonly used in Django to provide selectable options for fields within models or forms, allowing users to choose from the provided values when interacting with the application.


Challenges

One of the challenges we faced was how to display the questionnaire, showing only one question at a time along with its multiple choices, and dynamically change the page without redirecting the user to another URL. We wanted to maintain the same URL path throughout the process. After conducting research, my colleague Louise came across the concept of Wizard Forms, which seemed promising.


I was specifically working on the adopter questionnaire and faced the additional challenge of learning something new while striving to complete the task as quickly as possible. Additionally, I encountered difficulties while trying to style the wizard form to meet our design requirements. ( code above)


Another difficulty I faced was while working on the profile settings page. I was able to smoothly add redirect buttons and URLs to each of the desired pages, except for the pet_update page. It was supposed to redirect to the pet questionnaire page, but it kept crashing repeatedly. Fortunately, I received assistance from my colleagues, and together, we were able to fix the issue. Even though it required a few modifications, the solution turned out to be relatively simple. I struggled with it initially, but I was grateful to be part of a team where we could pool our collective thinking power to find a solution, rather than relying on just one individual. (code below)

<img width="590" alt="Screenshot 2023-08-15 at 21 23 14" src="https://github.com/renad1999/Adoptly/assets/112344006/6df4d066-783b-47c4-adff-ae27d87af00f">

One of the most significant challenges we faced as a team was dealing with merging conflicts on GitHub. Unfortunately, we made the critical mistake of not gitignoring the pycache files. What seemed like a small oversight turned out to be a major mistake that cost us hours of lost time. Every time we pushed our work and pulled it, our code broke, resulting in the deletion of a significant portion of our codebase. We encountered constant issues due to these pycache files, and it became a frustrating and time-consuming problem for us.
We learned a valuable lesson the hard way. This issue even occurred on the morning of our presentation, leading to the deletion of a substantial amount of code. We had to work diligently to retrieve as much as possible and fix all the errors that arose. Despite our efforts to avoid pushing any broken code to development and our thorough checks with each other before pushing and merging, the pycache files continued to cause problems for us. It was a frustrating experience for the entire team, but it emphasised the importance of properly managing version control and being cautious with ignored files like pycache.
Regrettably, the challenge we faced with merging conflicts and the issues caused by pycache files had a significant impact on the development of our website. We were unable to complete it as originally intended. However, I want to highlight the positive aspects of how we overcame this challenge.
Our team's ability to communicate effectively and our willingness to support one another played a crucial role. We recognized the importance of open and efficient communication, which allowed us to share our concerns, seek help, and find solutions together. Working as a team, we learned the value of productivity, understanding, and mutual assistance.


While our website may not have been completed exactly as we had initially envisioned, the lessons we learned and the experience gained from overcoming this challenge were invaluable. Collaboration and a supportive team environment can make a tremendous difference in facing and overcoming obstacles. Moving forward, we can apply these lessons to future projects.


<img width="256" alt="Screenshot 2023-08-15 at 21 24 04" src="https://github.com/renad1999/Adoptly/assets/112344006/aabc089b-d0fd-4fba-9e65-6756b5c14b8e">


Wins

One significant win we experienced during the development of the pet adoption app was the initial ideation process. Having a brilliant idea and seeing the potential in it was truly exciting. It showcased our team's creativity and problem-solving abilities, setting the foundation for the project's success.

Moreover, we celebrated the small wins throughout the development journey. Recognizing and appreciating these milestones helped us stay motivated and inspired. These small wins could include successfully implementing a specific feature, fixing a challenging bug, or achieving a smooth integration between different components. Acknowledging and celebrating these achievements fostered a positive atmosphere within the team and encouraged us to continue our hard work.

These wins, both big and small, not only boosted team morale but also acted as indicators of progress and validation of our efforts. They reminded us of our collective potential and the positive impact we could make when working together towards a common goal.


Key Learnings/Takeaways

Throughout the process of developing a pet adoption app using Django, MongoDB, and Python, I have gained a wealth of knowledge and valuable skills that have significantly contributed to my growth as a developer. Firstly, by utilising the Django framework, I have gained a deep understanding of its core components and functionality. Working with models has taught me how to define the structure of the application's data and establish relationships between different entities. 


I had the opportunity to learn and utilize the wizardForms, which proved to be incredibly useful. This allowed me to create a questionnaire that displayed one question at a time, streamlining the user experience and improving usability.

Another valuable lesson I learned was working with GitHub in a collaborative group project. I gained a thorough understanding of the necessary steps involved in merging and pushing our changes to the repository. This included managing branches, resolving conflicts, and ensuring a smooth collaboration process. Although we faced our issues with GitHub, I now know exactly what to do the next time to avoid the issues we were having with merging.

Furthermore, this project emphasised the importance of clear communication and respecting the choices and ideas of team members. Effective communication played a crucial role in ensuring everyone's opinions were heard and considered. By actively working together and finding common ground, we were able to build an app that satisfied everyone's expectations and created a harmonious working environment.

Bugs

We have several bugs in our code. Currently, the redirect page that prompts the user to choose whether they are an owner or adopter is not functioning correctly it is supposed to redirect the user to a different page that starts the survey they need. The like and dislike buttons on the pet profile pages are not operational. The matching functionality is not working.

Future Improvements


I have several improvements planned for the future, but my primary focus at the moment is to ensure that the app functions correctly according to its intended purpose. Once the core functionality is in place, I will proceed with the following enhancements:

Styling refinement: I will work on polishing the app's visual design, improving the overall aesthetics, and ensuring consistency in the use of colours, fonts, and layout. This will contribute to a more visually appealing and user-friendly experience.
Chatting feature: I will integrate chat functionality into the app, enabling real-time communication between users. This feature will allow users to engage in conversations, ask questions, and share information related to pet adoption or any other relevant topics.

Cross-platform compatibility: I aim to optimise the app for both web and mobile platforms, ensuring seamless functionality across different devices and screen sizes. This will involve responsive design techniques and thorough testing to ensure a consistent and smooth user experience.

By prioritising these improvements, we can create an app that not only functions correctly but also delivers a visually pleasing experience, fosters user engagement through real-time communication, and works seamlessly on various platforms.

