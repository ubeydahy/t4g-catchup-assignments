**WHAT HAPPENS WHEN YOU TYPE A URL AND PRESS ENTER**
When I type a URL into my browser and press Enter, several processes happen within milliseconds before the webpage appears on my screen.
Firstly, my device acts as the client. The browser sends a request asking to access a particular website. However, computers do not understand names like google.com but they rather understand IP addresses. So the browser first contacts the Domain Name System (DNS) to translate the given name into its corresponding IP address. Once the IP address is obtained, the client establishes a TCP/IP connection with the server. This ensures reliable communication between my device and the server hosting the website. During this process, firewalls may inspect the traffic to ensure it is safe and not malicious.
After the connection is established, the browser sends an HTTP or HTTPS request to the server.
If the website receives heavy traffic, the request first goes through a load balancer. The load balancer distributes incoming requests across multiple servers so that no single server becomes overloaded. The request is then forwarded to the web server. The web server handles HTTP requests and serves static content like HTML, CSS, and images. If the request requires dynamic processing such as logging in or retrieving users data, the web server forwards the request to the application server.
The application server processes the logic of the application. It may query a database to retrieve or store information. The database sends the requested data back to the application server. Finally, the server sends a response back to the client. The browser renders the content, and the website appears on my screen.

**DIFFERENCES BETWEEN A WEB SERVER AND AN APPLICATION SERVER**
A web server is responsible for handling HTTP requests and serving static content such as the HTML files, images, and CSS files, whiles an application server handles the logic and dynamic processing, Which is processing the users input, interacting with the database, and generating dynamic responses.
For example, imagine an online food ordering platform.
The web server shows the homepage layout, menu images, etc. But when I log in and place an order, or track my delivery, the application server processes those actions. It checks my login details, stores my order in the database, calculates the total costs, and updates my order status.
So the web server basically shows you the frontend (what you see), while the application server makes decisions and processes the logic behind the scenes.

**WHY THE CLIENTS NEVER TALKS DIRECTLY WITH THE DATABASE**
The client never communicates directly with the database beacuse of security reasons and also archiectural reasons. If clients had direct access to the database:
1. Anyone could manipulate the data.
2. Senitive informtaions can be exposed.
3. Logic rules could be bypassed.
So instead, the application server acts as a middle layer which validates requests, enforces rules, and controls what data can be accessed or modified.