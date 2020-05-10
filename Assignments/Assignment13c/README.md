Created the login with visual studios.  To run the project just open up the folder as a visual studios(2019 community) project.  
It is a ASP.net site using Oauth to give a google login.  For now the google login will only work if ran from https://localhost:44379.  
Login should work from server however it encounters an error when redirecting after selecting a google account.  Does work and display google
email locally though.
Site link: http://ec2-3-23-111-67.us-east-2.compute.amazonaws.com/

if you need to change the port to test the application follow these steps.

In Solution Explorer, right-click the name of the application and then select Properties. Click the Web tab.

In the Servers section, under Use Local IIS Web server, in the Project URL box change the port number.

To the right of the Project URL box, click Create Virtual Directory, and then click OK.

In the File menu, click Save Selected Items.

To verify the change, press CTRL+F5 to run the project. The new port number appears in the address bar of the browser.

