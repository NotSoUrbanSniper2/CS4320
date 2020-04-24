I looked at openid connect and Oauth.  I chose to implement a project with Oauth authentication.  My project allows you to login with 
your google login using Oauth.  I chose Oauth because it was substantually clearer how to use it compared to OpenID connect.  Microsoft
visual studios ASP.net webapp has a streamlined template for Oauth that I have utilised.  I got the google login to work from the localhost
url.  When I push it to the aws server I just need to update the uri to make it work from the site.  I encountered only one issue, which 
was that I needed to add a redirect uri to the google client.
