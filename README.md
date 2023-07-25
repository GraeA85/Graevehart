<div style="background-color: #F7F7F7; color: black;">

# **Graevehart Digital Designs**

This website has been created to sell digital art prints for all Steampunk fans. It has been designed with a range of different screen sizes in mind so users can make a purchase on a phone/tablet/PC.

!["Am I Responsive" image](static/images/readme/amiresponsivegraevehart.jpg)

[View the live project here](https://graevehart-8728b4cc664b.herokuapp.com/)

---
<br/>

## **Table of Contents**

1. [User Experience](#user-experience)
3. [Design](#design)
5. [Features](#features)
6. [Accessibility](#accessibility)
7. [Technologies Used](#technologies-used)
8. [Deployment and Local Development](#deployment-and-local-development)
9. [Testing](#testing)
10. [Credits](#credits)

---
<br/>
    
## **User Experience**
<br/>

### **Initial Discussion**

Steampunk inspired art is a relatively new and modern branch of art which has become very popular over the last few years. I decided to create Steampunk inspired digital art featuring a range of animals. The website currently offers these art prints for sale in Oak wood frames or Walnut wood frames.
<br/><br/>

### **User Stories**

#### **Viewing and Navigation**
* View the site on a range of device sizes.
* View a list of art prints. 
* View individual product details.
* Easily view the total of my purchases at any time.
* View products by category (frame type or miscellaneous pieces) and sort functions accordingly.

<br/>

#### **Registration and User Accounts**
* Easily register for an account.
* Easily log in or log out.
* Easily recover my password in case I forget it.
* Receive an email confirmation after registering.
* Have a personalised user profile.
* See previous orders listed when logged into profile.

<br/>

#### **Sorting and Setting**
* Sort the list of available products.
* Sort a specific category of product.
* Search for a product by name or description.
* Easily see what I have searched for and the number of results.

<br/>

#### **Purchasing and Checkout**
* Easily select the quantity of a product when purchasing it.
* View items in my bag to be purchased.
* Adjust the number of individual items in my bag.
* Easily enter my payment information.
* Ensure personal and payment information is safe and secure.
* View an order confirmation after checkout.
* Receive an email confirmation after checking out.

<br/>

#### **Admin and Store Management**
* Add product.
* Edit/update a product.
* Delete a product.
* Create further categories via the Django admin page, allowing for the creation of sales for example.

---
<br/>

## **Design**
<br/>

### **Wireframes**

Wireframes for the website (please click arrows for images).

<details>
<summary>Index</summary>

Desktop

![Desktop Index Wireframe](static/images/readme/wireframes/wire_index.jpg)

Mobile

![Mobile Index Wireframe](static/images/readme/wireframes/wire_mobile_index.jpg)

</details>
<br>

<details>
<summary>Products</summary>

Desktop

![Desktop Products Wireframe](static/images/readme/wireframes/wire_products.jpg)

Mobile

![Mobile Products Wireframe](static/images/readme/wireframes/wire_mobile_products.jpg)

</details>
<br>

<details>
<summary>Product Detail</summary>

Desktop

![Desktop Products Wireframe](static/images/readme/wireframes/wire_product_detail.jpg)

Mobile

![Mobile Products Wireframe](static/images/readme/wireframes/wire_mobile_products.jpg)

</details>
<br>

<details>
<summary>Product Management</summary>

Desktop

![Desktop Product Management Wireframe](static/images/readme/wireframes/wire_product_management.jpg)

Mobile

![Mobile Product Management Wireframe](static/images/readme/wireframes/wire_mobile_product_management.jpg)

</details>
<br>

<details>
<summary>My Profile</summary>

Desktop

![Desktop My Profile Wireframe](static/images/readme/wireframes/wire_profile.jpg)

Mobile

![Mobile My Profile Wireframe](static/images/readme/wireframes/wire_mobile_profile.jpg)

</details>
<br>

<details>
<summary>Logout</summary>

Desktop

![Desktop Logout Wireframe](static/images/readme/wireframes/wire_sign_out.jpg)

Mobile

![Mobile Logout Wireframe](static/images/readme/wireframes/wire_mobile_logout.jpg)

</details>
<br>

<details>
<summary>Register</summary>

Desktop

![Desktop Register Wireframe](static/images/readme/wireframes/wire_sign_up.jpg)

Mobile

![Mobile Register Wireframe](static/images/readme/wireframes/wire_mobile_register.jpg)

</details>
<br>

<details>
<summary>Sign-in</summary>

Desktop

![Desktop Register Wireframe](static/images/readme/wireframes/wire_sign_in.jpg)

Mobile

![Mobile Register Wireframe](static/images/readme/wireframes/wire_mobile_login.jpg)

</details>
<br>

<details>
<summary>Shopping Bag</summary>

Desktop

![Desktop Shopping Bag Wireframe](static/images/readme/wireframes/wire_bag.jpg)

Mobile

![Mobile Register Wireframe](static/images/readme/wireframes/wire_mobile_bag.jpg)

</details>
<br>

<details>
<summary>Checkout</summary>

Desktop

![Desktop Checkout Wireframe](static/images/readme/wireframes/wire_checkout.jpg)

Mobile

![Mobile Checkout Wireframe](static/images/readme/wireframes/wire_mobile_checkout.jpg)

</details>
<br>

<details>
<summary>Checkout Success</summary>

Desktop

![Desktop Checkout Success Wireframe](static/images/readme/wireframes/wire_checkout_success.jpg)

Mobile

![Mobile Checkout Success Wireframe](static/images/readme/wireframes/wire_mobile_checkout_success.jpg)

</details>
<br>

<br/>

### **Colour Scheme**

As the artwork is the primary product of the website, I have chose to keep the product pages as clean as possible, therefore a minimalist design and colour palette were used. The main index.html has a striking design to draw interest to the webpage.

<br/>

### **Typography**

Google Fonts was used to import the "Handlee" Font. This is used for all text throughout the website.

<br/>

---
<br/>

## **Features**

The website is made up of 12 pages:

* Index
* Products
* Product Detail
* Clearance
* Product Management
* My Profile
* Logout
* Register
* Sign-in
* Shopping Bag
* Checkout
* Checkout Success

Previews of each part can be viewed by clicking the arrows below.

<br/>

### **Index**

The index page has:

   <details>
   <summary>A "Shop Now" button, which takes the user to the "All Products" page</summary>

   ![Shop Now Button](static/images/readme/shop_now.jpg)

   </details>     

<br/>

### **Products**

The Products page has the following features:

   <details>
   <summary>A list of products, which, when clicked, takes the user to the detail page of that specific product. If the product is on sale, the price is updated and the text is red, with additional text labelinglabelling it as on sale.</summary>

   ![Products](static/images/readme/products.jpg)

   </details>
   <br>

   <details>
   <summary>If the user is a superuser, then at the bottom of each product are links to either edit or delete the product.</summary>

   ![Edit or Delete](static/images/readme/edit_delete.jpg)

   </details>
   <br>

   <details>
   <summary>Text which lets the user know how many products there are in the category they are browsing. When the user is filtering products, this also shows a link to "Products Home"</summary>

   ![Product Amount & Link](static/images/readme/product_amount.jpg)

   </details>
   <br>

   <details>
   <summary>A dropdown box with the ability to sort by price (low to high), price (high to low), name (a-z), name (z-a), year of original (past-present), year of original (present - past). The year of the original denotes the year that the artwork was made that the piece was based on.</summary>

   ![Sort Dropdown](static/images/readme/sort_dropdown.jpg)

   </details>
   <br>

   <details>
   <summary>Category boxes appear when you are seeing the product page in any view other than 'all products'. They show the user which categories they are currently viewing and can be clicked on to take the user to a specific category.</summary>

   ![Category Boxes](static/images/readme/categories.jpg)

   </details>
   <br>

   <details>
   <summary>A scroll-up button on the bottom-right-hand-side of the page, which when clicked, will automatically scroll the page up to the top.</summary>

   ![Scroll Up](static/images/readme/scroll.jpg)

   </details>

### **Product Detail**

The Product Detail page has the following features:

   <details>
   <summary>When clicking on the product image, it opens in a new tab for a clearer view.</summary>

   ![Product Image](static/images/readme/product.jpg)

   </details>
   <br>

   <details>
   <summary>Details page showing information about the artpiece, price and size of the framed product.</summary>

   ![Product Details](static/images/readme/details.jpg)

   </details>
   <br>
   
   <details>
   <summary>If the user would like more than one of the products, they can adjust the quantity.</summary>

   ![Quantity Adjuster](static/images/readme/quantity.jpg)

   </details>
   <br>

   <details>
   <summary>A keep shopping button that takes the user back to the products page to view all products.</summary>

   ![Keep Shopping Button](static/images/readme/keep_shopping.jpg)

   </details>
   <br>

   <details>
   <summary>A button that will add the desired quantity of the product to the user’s checkout cart.</summary>

   ![Add to Bag Button](static/images/readme/add.jpg)

   </details>
  

### **Product Management** 

   <details>
   <summary>The Product Management page is only available to logged-in superusers and has a form that will allow the user to add a product.</summary>

   ![Add Product Form](static/images/readme/add_product.jpg)
   
   </details>
   <br>

<br/>

### **My Profile**

The My Profile page has the following features:

   <details>
   <summary>A form where the user can update their personal information, which is then auto filled on the checkout form.</summary>

   ![User Information Form](static/images/readme/user_info.jpg)
   
   </details>
   <br>

   <details>
   <summary>A section that shows the user their order history.</summary>

   ![Order History](static/images/readme/order_history.jpg)
   
   </details>
   <br>

<br/>

### **Logout**

   <details>
   <summary>The Logout page has a cancel button which takes the user back to the product page, and a sign-out button, which signs the user out.</summary>

   ![Sign Out](static/images/readme/sign_out.jpg)
   
   </details>
   <br>

<br/>

### **Register**

   <details>
   <summary>The Sign-Up page has the following features:</summary>
   
   * A link to take the user to the sign-in page if they already have an account. 
   * A form for the user to sign up if they do not already have an account. 
   * This page is only seen if the user is not signed in.

      ![Register](static/images/readme/register.jpg)
   
   </details>
   <br>

<br/>

### **Sign In** 

   <details>
   <summary>The Sign In page has the following features:</summary>
   
   * A login button that takes the user to the login page in case they already have an account.
   * A form for the user to input the necessary details to create an account.

      ![Sign In](static/images/readme/sign_in.jpg)
   
   </details>
   <br>

<br/>

### **Shopping Bag**

The Shopping bag page has the following features:

   <details>
   <summary>The details of the products being bought, with an option to update the amount or remove each product.</summary>
   
   ![Shopping Bag](static/images/readme/shopping_bag.jpg)
   
   </details>
   <br>

   <details>
   <summary> The details of the total and delivery price, as well as information on how much extra the user should spend to get free postage.
   / A button to return the user to the products page.
   / A button to continue to the checkout.</summary>
   
   ![Shopping Buttons](static/images/readme/shopping_buttons.jpg)
   
   </details>
   <br>

<br/>

### **Checkout**

The Checkout page has the following features:

   <details>
   <summary>A form for the user details needed to check out.</summary>
   
   ![Checkout Form](static/images/readme/checkout_form.jpg)
   
   </details>
   <br>

   <details>
   <summary>The order summary / A button to send the user back to be able to adjust their bag / A button to submit their order</summary>
   
   ![Order Summary](static/images/readme/order_summary.jpg)
   
   </details>
   <br>

<br/>

### **Checkout Success**

The Checkout success page has the following feature:

   <details>
   <summary>Information about the user order</summary>
   
   ![Checkout Success](static/images/readme/checkout_success.jpg)
   
   </details>
   <br>

<br/>

### **All pages have the following features**

   <details>
   <summary>A logo that when clicked takes the user back to the index page.</summary>
   
   ![Logo](static/images/readme/logo.jpg)
   
   </details>
   <br>

   <details>
   <summary>A search function</summary>
   
   ![Search bar](static/images/readme/search.jpg)
   
   </details>
   <br>

   ![Menu links](static/images/readme/menu_links.jpg)
   
   </details>
   <br>

   <details>
   <summary>A drop-down menu for the user account. Which only shows 'log in' and 'register' if the user is not logged in, but shows 'product management' (if superuser), 'my profile', and 'logout'.
   / A link to the user’s shopping trolley</summary>
   
   ![My Account](static/images/readme/my_account.jpg)
   
   </details>
   <br>

<br/>

### **Toasts & Messages**

Many messages are included to alert the user that they have accomplished an action. Such as:

   <details>
   <summary>When adding a product to their checkout bag.</summary>
   
   ![Add Product to Bag](static/images/readme/add_product_toast.jpg)
   
   </details>
   <br>

   <details>
   <summary>Successfully placing an order.</summary>
   
   ![Order Success](static/images/readme/order_success_toast.jpg)
   
   </details>
   <br>

   <br/>

### **Future Features**

* The checkout form to show and automatically fill in the name of the logged-in user.
* Ability to run a sale on the website, caluclating discount for each item.
* Confirmation before deletion option, to prevent items been deleted by mistake. 

---

<br/>

## **Accessibility**

I have been mindful during coding to ensure that the website is as accessible as possible. I have achieved this by:

* Using semantic HTML.
* Using descriptive alt attributes on images on the site.
* Aria labels - providing information for screen readers where there are icons used and no text, such as footer icons.
* Ensuring there is adequate colour contrast throughout the site.

---
<br/>

## **Technologies Used**


### **Languages Used**

HTML5, CSS3, Python, and JavaScript were used to create this website.


### **Frameworks, Libraries & Programs Used**

* [Google Fonts](https://fonts.google.com/) was used to import the font used throughout the website.
* [Git](https://git-scm.com/) was used for version control by using the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) was used to store the projects' code, and to handle version control.
* [Photopea](https://www.photopea.com) was used to edit and crop images.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) was used to troubleshoot and test features and solve issues with responsiveness and styling.
* [Am I Responsive?](https://ui.dev/amiresponsive) was used to show the website on a range of devices.
* [Psycopg2](https://www.psycopg.org/docs/) was used to connect Python code with the database. 
* [Django](https://www.djangoproject.com/) is a high-level Python web framework.
* [Bootstrap](https://getbootstrap.com/) was used for responsive and pre-designed CSS.
* [ElephantSQL](https://www.elephantsql.com/) was used to host the database.
* [Heroku](https://www.heroku.com/) was used to deploy the website.
* [Bing Image Creator](https://www.bing.com/create) was used to create the artwork.
* [Font Awesome](https://fontawesome.com/) was used for the icons.
* [Amazon Web Services](https://aws.amazon.com/) was used to host the images for the Heroku-hosted site.
* [Favicon Generator](https://favicon.io/favicon-converter/) was used to use convert my favicon design into something useable.

---

<br/>

## **Deployment and Local Development**

<br/>

### **Deployment**

This project was deployed to Heroku using the following steps:

<br/>

#### **ElephantSQL**

1. Navigate to ElephantSQL.com and create a user account, by using the log-in with GitHub option.
2. Click “Create New Instance”.
3. Set up your plan. (You can leave the 'tags' field blank.)
4. Select a region.
5. Select a data centre near you
6. Then click “Review”.
7. Check your details are correct and then click “Create instance”.
8. Return to the ElephantSQL dashboard and click on the database instance name for this project
9. In the URL section, clicking the copy icon will copy the database URL to your clipboard
10. Leave this tab open, we will come back here later

<br/>

#### **Heroku**

1. Log into Heroku.com, click “New” and then “Create a new app”.
2. Choose a unique name for your app, select the region closest to you, and click “Create app”.
3. Go to the Settings tab of your new app
4. Click Reveal Config Vars
5. Return to your ElephantSQL tab and copy your database URL
6. Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add.”
7. Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var. 
8. Navigate to the “Deploy” tab of your app.
9. select “Connect to GitHub” in the Deployment method section.
10. Search for your repo and click Connect
11. Optional: You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository.
12. As we already have all our changes pushed to GitHub, we will use the Manual Deploy section and click Deploy Branch. This will start the build process. 
13. Now, we have our project in place, and we have an empty database ready for use. As you may remember from our local development, we still need to add our tables to our database. To do this, we can click the “More” button and select “Run console.”
14. Type python3 into the console and click Run
15. In the terminal that opens, write "from eponymous_bosch import db" and then press enter.
16. In the terminal, write "db.create_all()" and then press enter.
17. Exit the Python terminal, by typing exit() and hitting enter, and close the console. Our Heroku database should now have the tables and columns created from our models.py file.
18. The app should be up and running now, so click the “Open app” button

<br/>

---

## **Testing**

Testing was ongoing throughout the entire build. I utilised Chrome developer tools while building to pinpoint and troubleshoot any issues as I went along. Both manual testing and validation was employed.  

I tested the page and had 3 people also manually test it on their own devices. For validation, I used the W3C validator, CSS validator, Python Linter and Lighthouse. 

<br/>

### **Validation**


#### **W3C Validator**

The [W3C HTML Validator](https://validator.w3.org/) was used to validate the HTML on all pages of the website. 

No HTML errors were found on the website.

<br/>

#### **CSS Validator**

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.

No CSS errors were found on the website.

<br/>

#### **Pep8 Validator**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code. From running the validator tool, a list was presented of errors within the code. 
The vast majority of the errors present were relating to the lines of code being over the character limit. These were simply solved through moving lines of code to the next
line down or the use of the \ to break a line where appropriate. Some lines contained very long URLs which are not recommended to be broke. These lines were simply suffixed
with the #noqa command which prevents them showing up in future linter validation scans.
Other errors included no blank lines at the bottom of the python files, these were simply corrected by adding a blank line.
Some 

#### **Lighthouse**

Lighthouse in Google Dev Tools was used to check performance, accessibility, best practices and search engine optimisation.

The Graevehart Digital Art shop webpage scored high results throughout the website for accessibility, best practices and search engine optimisation. The only issue was with the performance, all image files were compressed to load quicker, however due to the
quality of the files and art being the main product on the page, I did not want to suffer quality issues. Therefore performance score is quite low on the pages containing large amount of image files. The loading speed does not suffer too much from this however.

### **Manual Testing**

To fully test my website, I used Google Chrome Developer Tools to ensure that the pages were responsive enough on all available screen sizes. Testing was performed on a variety of browsers (Microsoft Edge and Firefox) and devices (PC,Microsoft Surface, Nothing Phone 1, IPhone 12, Samsung S21 and OnePlus Phone).
The following tests were carried out by several people using several devices, each asked to complete all tasks listed.

<br/>

#### **Links:**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| That the user will be taken to the right page when clicking on links | Clicked on every link to make sure that it took the user to the right page | Passed |

<br/>

#### **Buttons:**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| That each button will do what the user expects it to | Clicked on every button to make sure that it worked as expected | Passed |

<br/>

#### **Forms:**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| The form will not submit when required fields are left blank | Checked every form to see if it would be submitted if any of the required fields were left blank | Passed |
| The user sees a success message when having successfully submitted a form | Successfully submitted all forms to check if they all had success messages | Passed |
| The form will not submit when input types and lengths/amounts are not appropriate | Tested every form field that takes a specific input type to see if it would submit with an undesired input type | Passed |

<br/>

#### **Authentication:**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| Non-logged-in users cannot see or access the parts of the site that are off-limits to them, and vice versa. | I logged in and out and, on both occasions, I checked to see what options were available to the user | Passed |
| Users cannot view confidential information about other users, such as user account details or order history. |    I logged in as different users with different credentials saved on their accounts, to check if either user could see the details of the other | Passed |

<br/>

#### **Database:**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| User data is added and persists over time, including order history and personal information | Added multiple users with different data and checked that throughout logging in and out, and over the course of weeks, the data remained the same | Passed |
| User is linked to their order history and personal data | I made multiple user accounts with different data, and all users can see their own data | Passed |
| User data can be edited and deleted from the database. | I tested that when deleting a user and then reestablishing them, none of their previous data is visible in their account. I also edited data such as user delivery details | Passed |

<br/>

#### **Checkout**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| Adding, editing, and removing products from the bag work as expected.  | I added, edited and removed products from the bag | Passed |
| Users’ correct details auto-fill in the checkout form. | Checked that the same details from the user’s profile are the ones that are auto filling the checkout form. I also checked that editing these details will change those on the form. | Passed |
| Stripe payment goes through without any problems. | I made several orders, which all went through fine. I then checked the Stripe dashboard webhooks and the three parts to the order submission process all worked sucessfully.| Passed |
| The webhook is works so that if the user were to lose connection or close their browser before the transaction completes, the order still goes through, and they are automatically emailed. | I submitted the checkout form but closed the tab before it finished loading. The user still got charged, sent an automatic email, and the order was logged on the system and in their order history | Passed |

<br/>

#### **Products**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| The sorting and filtering functions work appropriately. | I clicked on each sort and filter function and check to see if they displayed the right products and, in the order, expected | Passed |
| They can be added from the product management page. | I created several products using the management page, and checked to see that they showed up in the admin and on the website in the appropriate places. | Passed |
| They can be edited or deleted by logged-in superusers from the products or product detail pages. | I edited and deleted several products as a superuser in both the 'all products' and 'product detail' pages | Passed |

<br/>

#### **Search**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| The search function works as expected. | I searched for a wide variety of artwork based on various parts of their products pages (category, product name for e.g.), and this worked as expected. | Passed |

<br/>

#### **Profile**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| Shows the user’s editable details. | I checked on several users’ profiles that their details were editable. | Passed |
| Shows the users order history | I checked on several users’ profiles that their orders were all visible in their order history after making a variety of orders through their accounts | Passed |

<br/>

### **Solved Bugs**

| Expected behaviour | Actual behaviour | Solution |
|    :----:          |        :----:    | :---     |
|Verification email to be recieved by the user when registration process has been completed|No verification email was being recieved when the user signed up for a new account|This was due to a setting issue in the main app settings.py file. This was changed to mandatory and verification emails were again recieved by the user.

<br/>

### **Known Bugs**

There are no known bugs outstanding within the Graevehart Website.

---
<br/>

## **Credits**

Slack - for answering many queries during the coding process.
Stack overflow - For obscure answers during the coding process.


<br/>

### **Code Used**

* [Code Institute's 'Boutique Ado' walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/) was used as the starting point for this project.

<br/>

### **Content**

All content used in the website was created by me, primarily using AI.

<br/>

### **Acknowledgements**

I would like to acknowledge the following people who helped me along the way in completing my fourth milestone project:

- My family and friends for user testing the website on a variety of devices they had available.

</div>