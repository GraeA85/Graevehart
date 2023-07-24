<div style="background-color: #F7F7F7; color: black;">

# **Graevehart Digital Designs**

This website has been created to sell digital art prints for all Steampunk fans. It has been designed with a range of different screen sizes in mind so users can make a purchase on a phone/tablet/PC.

!["Am I Responsive" image](static/images/readme/amiresponsive.jpg)

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
* Sort multiple categories of products simultaneously.
* Search for a product by name or description.
* Easily see what I have searched for and the number of results.
* Sort based on what is currently on sale (when a sale is active).

<br/>

#### **Purchasing and Checkout**
* Easily select the quantity of a product when purchasing it.
* View items in my bag to be purchased.
* Adjust the number of individual items in my bag.
* Easily enter my payment information.
* Feel my personal and payment information is safe and secure.
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

The wireframes are mostly adapted versions of the Boutique Ado walkthrough.

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

![Desktop Checkout Success Wireframe](static/images/readme/wireframes/wire_commission_success.jpg)

Mobile

![Mobile Checkout Success Wireframe](static/images/readme/wireframes/wire_mobile_checkout_success.jpg)

</details>
<br>

<br/>

### **Colour Scheme**

Due to the colourful nature of the artwork itself, a minimalist design and colour palette were used, so that it would not clash with any of the artwork displayed.

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
   <br>

<br/>

### **Product Detail**

The Product Detail page has the following features:

   <details>
   <summary>When clicking on the product image, it opens in a new tab for a clearer view.</summary>

   ![Product Image](static/images/readme/product.jpg)

   </details>
   <br>

   <details>
   <summary>Details page show information about the art piece, price and size of the framed product.</summary>

   
   <details>
   <summary>If the user is a superuser, two links appear giving the user the ability to edit or delete the product.</summary>

   ![Edit and Delete](static/images/readme/edit_delete_detail.jpg)

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
   <br>

   <details>
   <summary>A button that will add the product to the logged-in user’s wishlist. This button is only shown if the user is logged in.</summary>

   ![Add to Wishlist Button](static/images/readme/add_wishlist.jpg)
   
   </details>
   <br>

<br/>

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

### **Shopping Bag***

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

   <details>
   <summary>Links to three versions of the products page - all products/prints/posters, which themselves have dropdowns to further filter those pages. / A link to the commission’s page, which is only shown when the user is logged in.</summary>
   
   ![Menu links](static/images/readme/menu_links.jpg)
   
   </details>
   <br>

   <details>
   <summary>A drop-down menu for the user account. Which only shows 'log in' and 'register' if the user is not logged in, but shows 'product management', 'my profile', 'my wishlist', 'my commissions' and 'logout'.
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

* The commission form to automatically fill in the name and email of the logged-in user
* The checkout form to show and automatically fill in the name of the logged-in user
* Improve the responsiveness of a few of the pages in the mobile view

---

<br/>

## **Accessibility**

I have been mindful during coding to ensure that the website is as accessible as possible. I have achieved this by:

* Using semantic HTML.
* Using descriptive alt attributes on images on the site.
* Aria labels - providing information for screen readers where there are icons used and no text, such as footer icons.
* Guaranteeing adequate colour contrast throughout the site.

---
<br/>

## **Technologies Used**

<br/>

### **Languages Used**

HTML5, CSS3, Python, and JavaScript were used to create this website.

<br/>

### **Frameworks, Libraries & Programs Used**

* [Google Fonts](https://fonts.google.com/) was used to import the font used throughout the website.
* [Git](https://git-scm.com/) was used for version control by using the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) was used to store the projects' code, and to handle version control.
* [Photopea](https://www.photopea.com) was used to edit and crop images.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) was used to troubleshoot and test features and solve issues with responsiveness and styling.
* [Am I Responsive?](https://ui.dev/amiresponsive) was used to show the website on a range of devices.
* [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) was used for debugging.
* [SQLAlchemy](https://www.sqlalchemy.org/) was used to connect Python code with the database.
* [Psycopg2](https://www.psycopg.org/docs/) was used to connect Python code with the database. 
* [Django](https://www.djangoproject.com/) is a high-level Python web framework.
* [Bootstrap](https://getbootstrap.com/) was used for responsive and pre-designed CSS.
* [ElephantSQL](https://www.elephantsql.com/) was used to host the database.
* [Heroku](https://www.heroku.com/) was used to deploy the website.
* [Bing Image Creator](https://www.bing.com/create) was used to create the artwork.
* [Font Awesome](https://fontawesome.com/) was used for the icons.
* [Amazon Web Services](https://aws.amazon.com/) was used to host the images for the Heroku-hosted site.
* [RespImageLint](https://ausi.github.io/respimagelint/) was used to see how the images needed to be changed to optimise the page.
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

### **Local Deployment**

<br/>

---

<br/>

## **Testing**

Testing was ongoing throughout the entire build. I utilised Chrome developer tools while building to pinpoint and troubleshoot any issues as I went along. Both manual testing and validation was employed.  

I tested the page and had 3 people also manually test it on their own devices. For validation, I used the W3C validator, CSS validator, Python Linter, JSHint validator, and Lighthouse. 

<br/>

### **Validation**


#### **W3C Validator**

The [W3C HTML Validator](https://validator.w3.org/) was used to validate the HTML on all pages of the website. 

* Results from the [bag](static/images/readme/validation/html/bag.jpg) page check.
* Results from the [checkout](static/images/readme/validation/html/checkout.jpg) page check.
* Results from the [checkout success](static/images/readme/validation/html/checkout_success.jpg) page check.
* Results from the [commission](static/images/readme/validation/html/commission.jpg) page check.
* Results from the [commission success](static/images/readme/validation/html/commission_success.jpg) page check.
* Results from the [my commission](static/images/readme/validation/html/my_commissions.jpg) page check.
* Results from the [index](static/images/readme/validation/html/index.jpg) page check.
* Results from the [products](static/images/readme/validation/html/products.jpg) page check.
* Results from the [product detail](static/images/readme/validation/html/product_detail.jpg) page check.
* Results from the [profile](static/images/readme/validation/html/my_profile.jpg) page check.
* Results from the [sign up](static/images/readme/register.jpg) page check.
* Results from the [log out](static/images/readme/validation/html/logout.jpg) page check.
* Results from the [log in](templates/allauth/account/login.html) page check.
* Results from the [email confirm](static/images/readme/validation/html/email_confirm.jpg) page check.
* Results from the [wishlist](static/images/readme/validation/html/wishlist.jpg) page check.
* Results from the [product management](static/images/readme/validation/html/product_management.jpg) page check.

<br/>

#### **CSS Validator**

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.

* Results from the [checkout](static/images/readme/validation/css/checkout_css.jpg) css.
* Results from the [profile](static/images/readme/validation/css/profile_css.jpg) css.
* Results from the [base](static/images/readme/validation/css/base.jpg) css.

<br/>

#### **Pep8 Validator**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code. From running the validator tool, a list was presented of errors within the code. 
The vast majority of the errors present were relating to the lines of code being over the character limit. These were simply solved through moving lines of code to the next
line down or the use of the \ to break a line where appropriate. Some lines contained very long URLs which are not recommended to be broke. These lines were simply suffixed
with the #noqa command which prevents them showing up in future linter validation scans.
Other errors included no blank lines at the bottom of the python files, these were simply corrected by adding a blank line.

#### **Lighthouse**

Lighthouse in Google Dev Tools was used to check performance, accessibility, best practices and search engine optimisation.

The Graevehart Digital Art shop webpage scored high results throughout the webiste. The only issue was with the performance, 

### **Manual Testing**

To fully test my website, I used Google Chrome Developer Tools to ensure that the pages were responsive enough on all available screen sizes. Testing was performed on a variety of browsers (Chrome, Microsoft Edge, and Firefox) and devices (Gigabyte gaming laptop, iPhone SE, Android one+ 9 mobile, Fair Phone).

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
| Users cannot view confidential information about other users, such as user account details, wish lists, carts, or commissions. |    I logged in as different users with different wish lists and commission requests, to check if either user could see the details of the other | Passed |

<br/>

#### **Database:**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| User data is added and persists over time, including order history, commissions and wishlist. | Added multiple users with different data and checked that throughout logging in and out, and over the course of weeks, the data remained the same | Passed |
| User is linked to their order history, wishlist, and commission data | I made multiple user accounts with different data, and all users can see their own data | Passed |
| User data can be edited and deleted from the database. | I tested that when deleting a user and then reestablishing them, none of their previous data is visible in their account. I also edited data such as user delivery details, and deleted items off the wishlist | Passed |
| Calculations in the models to automatically assign variables to work as expected. | All calculations the model made were independently verified by manipulating the data and checking the results. This focused mostly on sales | Passed |

<br/>

#### **Sale Function**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| If the user is looking at a product that is on sale, and the product is then taken off sale if the user adds it to their cart without refreshing the page, the product will revert to the original price. | Opened the product detail page of a sale item. Took the item off sale. Without refreshing the product detail page, I added the item to my cart. Doing this showed that the item had reverted to its pre-sale price. | Passed |

<br/>

#### **Checkout**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| Adding, editing, and removing products from the bag work as expected.  | I added, edited and removed products from the bag | Passed |
| Users’ correct details auto-fill in the checkout form. | Checked that the same details from the user’s profile are the ones that are auto filling the checkout form. I also checked that editing these details will change those on the form. | Passed |
| Stripe payment goes through without any problems. | I made several orders, which all went through fine. I then checked the Stripe dashboard to make sure it was going through on that side too | Passed |
| The webhook is works so that if the user were to lose connection or close their browser before the transaction completes, the order still goes through, and they are automatically emailed. | I submitted the checkout form but closed the tab before it finished loading. The user still got charged, sent an automatic email, and the order was logged on the system and in their order history | Passed |

<br/>

#### **Wishlist**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| Adding and removing products from the wishlist work as expected. | I tested in different user accounts that I could add and remove products from the wishlist | Passed |
| The email is sent as expected when a user’s wished-for item goes on sale.  | I tested on several user accounts with several different items by adding an item to users wish lists, checking some of their consent boxes, and seeing if only those who consented got an email for the item that just went on sale, if it was in their wishlist | Passed |
| The user can control whether the above happens by turning their consent on or off on their wishlist page. | This was tested for in the test above | Passed |

<br/>

#### **Products**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| The sorting and filtering functions work appropriately. | I clicked on each sort and filter function and check to see if they displayed the right products and, in the order, expected | Passed |
| They can be added from the product management page. | I created several products using the management page, and checked to see that they showed up in the admin and on the website in the appropriate places. | Passed |
| They can be edited or deleted by logged-in superusers from the products or product detail pages. | I edited and deleted several products as a superuser in both the 'all products' and 'product detail' pages | Passed |

<br/>

#### **Commissions**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| They can be added to the database via the commission’s form. | I submitted many commission forms, which then displayed on both the admin page and the user's 'my commissions' page | Passed`` |
| They appear on the 'My Commissions' page, in order of when they were added, with the recently added being at the top. | I added several commissions to a few different users, and all of them had their commissions appear in the correct order | Passed |
| The admin can change the status on the Django admin page, which will change the status on the 'My Commissions' page. | I changed the status on the admin page for several commissions, and each showed this change on the users 'My Commissions' pages. | Passed |

<br/>

#### **Search**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| The search function works as expected. | I searched for a wide variety of artwork based on various parts of their products pages, and this worked as expected. | Passed |

<br/>

#### **Profile**

| Expected | Test Performed | Result |
| :---:    |    :----:      | :---:  |
| Shows the user’s editable details. | I checked on several users’ profiles that their details were editable. | Passed |
| Shows the users order history | I checked on several users’ profiles that their orders were all visible in their order history after making a variety of orders through their accounts | Passed |

<br/>

### **User Testing**

| User | Device | Problem | Screenshot |
| :---:        |    :----:          |        :----:    | :---:     |
| MI | Fair Phone | Can't see the number in the quantity box in the design page | [MI Screenshot](static/images/readme/no_quantity_number.png) |
| CM | Android 1+9 | Price of product is not shown in the order confirmation page | [CM Screenshot 1](static/images/readme/cm_no_price.png) |
| CM | Android 1+9 | In checkout cart, the plus box wraps | [CM Screenshot 2](static/images/readme/cm_plus_wrap.png) |
| SHM | MacBook Air 2017 | Padding is needed on the 'verify email' page | [SHM Screenshot 1](static/images/readme/shm_padding.png) |
| SHM | MacBook Air 2017 | The automatic emails do not say Eponymous Bosch | [SHM Screenshot 2](static/images/readme/shm_email.png) |

<br/>

### **Solved Bugs**

| Bug Number  | Expected behaviour | Actual behaviour | Solution |
| ---:        |    :----:          |        :----:    | :---     |
| 1       |  When clicking on the On Sale dropdown under All Products in the nav bar, the user sees everything on sale   |  When clicking on the On Sale dropdown under All Products in the nav bar, the user sees all products, not just those on sale  | The model has a property called on_sale that determines the Boolean value of on_sale in the Product model. This calculates if an item is on sale based on whether the admin enters a discount or not. So instead of looking for on_sale=True, the code looks for on_sale being greater than 0. So, I changed the all_product view section to "if 'on_sale' in request.GET: products = products.filter(discount__gt=0)" |
| 2       | Commissions shown on the my_commissions page should only be those of the user  | Currently showing every user's commission  | Change part of the my_commissions view code from this -> commissions = Commission.objects.all(), to this -> commissions = Commission.objects.filter(user=request.user) |
| 3 | When marking the discount percentage or a product as '0' in admin, the user should be able to turn off the sale |        Marking the discount percentage as '0' returned a form error, requesting the user enter a discount percentage | Added the discount condition to the Product model |
| 4 | When checking out, after submitting the form, the form should go through, user payment to be processed by Stripe, and the user is sent an automatic email confirmation | When checking out, after submitting the form, the user gets the error - "AttributeError at /checkout/ 'Product' object has no attribute 'price'" | This was because the checkout model save function was not updated when product.price was changed to product.sell_price in the Product model. |
| 5 | When asking to sort products by price in the navigation bar, products should then be sorted by price | Instead the page would not render and threw the error "Cannot resolve keyword 'sell_price' into field." | This issue arose because the field 'sell_price' was not defined in the Product model as a database field, but rather as a property with a getter method |
| 6 | When asking to sort products by price in the dropdown bar, products should then be sorted by price | Instead the page would not render and threw the error "FieldError at /products/ Cannot resolve keyword 'sell' into field. Choices are: category, category_id, description, discount_percentage, id, image, image_url, imperial, metric, name, og_price, on_sale_end, on_sale_start, orderlineitem, orientation, orig_url, original_artist, product_wishlists, sell_price, sku, style, type, users_wishlist, wishlistitem, year" | This issue arose because the sort key used had an underscore in it. Fixing the view to remove this made the page render again, and the sorting function now works. |
| 7 | User can add product via add_product page. | Instead, on form submission, this error is displayed - "TypeError at /products/add/ unsupported operand type(s) for *: 'decimal.Decimal' and 'NoneType'" | This was because I had removed the discount_percentage field, which made the sell_price incalculable. |
| 8 | The Heroku-hosted page renders when visited | The page does not render and shows this error - "SuspiciousOperation at / Attempted access to '/images/logo.webp' denied." | I changed the file path to correct this |
| 9 | When a user clicks on "My Wishlist", it would take them to a rendered page | If a user tried to access their wishlist when they have no wishlist items, the page does not render, and shows the error "NoReverseMatch at /wishlist/. Reverse for 'sale_alert_consent' with arguments '('',)' not found. 1 pattern(s) tried: ['wishlist/sale_alert_consent/(?P<user_id>[0-9]+)/\\Z']". | This happens before a user puts anything on their wishlist and does not happen if they have put something on their wishlist and then take it off again. This happened because sale_alert_consent is necessary for the wishlist view, but this was not set before the user put something in their wishlist. To fix this, I added in the show_wishlist view that a wishlist should be made if the user does not have one already, and that the user's sale_alert_consent should be set to false. A belt and braces approach, since creating the wishlist should mean that this field is automatically set to false. |
| 10 | When manually adding the sale start and end date in the admin, no error should occur | Instead, it throws a validation error and requests that the user enter the discount percentage, even though there is one already there  | The code in the product model was wrong. This has now been fixed. |
| 11 | When registering as a new user, the form should validate, and take the user to the 'confirm email' page | When submitting the signup form, the user sees "Forbidden (403) CSRF verification failed. Request aborted" | Changing the development variable in the github environment to be exclusive to this project, and turning both this variable and the one in Heroku to False, seemed to fix this bug. |
| 12 | On the product detail page, if the user deletes the product quantity value, and then click "add to bag", a validation warning should pop up to say that they need to enter a value. | Instead, the user sees a "server 500" error | I added 'required' to the input boxes, and adjusted the views so that it didn't assume there was an integer value |

<br/>

### **Known Bugs**

There are no known bugs.

---
<br/>

## **Credits**

Thanks are given for the following posts and tutorials:

* ['Platform-based Programming's' Assignment Walkthrough](https://pbp-fasilkom-ui.github.io/ganjil-2023/en/assignments/tutorial/tutorial-1/) was used for the base code for setting up the wishlist.
* ['Funda Web Of It's' tutorial on 'Insert data into database in Django'](https://www.fundaofwebit.com/django/insert-data-into-database-in-django#:~:text=To%20insert%20data%2C%20using%20forms,the%20classname%20as%20shown%20below.&text=Open%20the%20views.py%20file,given%20in%20the%20path%20above.&text=%23%20Create%20your%20views%20here.) was used to understand how to create a wishlist button to send the data to the database.
* [Coding Ninja's 'Django Model Form' tutorial](https://www.codingninjas.com/codestudio/library/django-model-form) was used for the basis of the contact/commission form.
* ['Geeks for Geeks' tutorial on 'Overriding the save method in Django models'](https://www.geeksforgeeks.org/overriding-the-save-method-django-models/) helped me understand how to create the save function in the product model for when products are on sale.
* [Monkut's reply in Stack Overflow post about showing custom model validation exceptions in the Django admin site](https://stackoverflow.com/questions/2177720/showing-custom-model-validation-exceptions-in-the-django-admin-site) helped me understand how to raise validation exceptions for my product model when writing the sale functions.
* [w3school's Django Queryset explanation](https://www.w3schools.com/django/django_queryset_get.php) helped me understand how .values_list() helps to return only certain data. This helped me write the wishlist auto-emailing function.
* [Alasdair's post on Stack Overflow](https://stackoverflow.com/questions/37205793/django-values-list-vs-values) helped point me in the write direction of using flat=True on values_list(), so that I can loop the output.
* [Arie's code on Stack Overflow](https://stackoverflow.com/questions/16277997/field-labels-crispy-forms-django) was used to edit the field names on the commission form.
* [Bipul Jain](https://stackoverflow.com/questions/52107184/suspiciousoperation-when-loading-image-in-django) for explaining how to fix a SeriousOperation error.

<br/>

### **Code Used**

* [Code Institute's 'Boutique Ado' walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/) was used as the starting point for this project.
* [Ajmal Aamir's](https://stackoverflow.com/questions/56580696/how-to-implement-add-to-wishlist-for-a-product-in-django) model code in this Stack Overflow post was used for the wishlist model.
* [Harry Dhillon's Nourish and Lift](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/wishlist/views.py) code was used for the wishlist.
* [Mahammadhusain Kadiwala's](https://stackoverflow.com/questions/73813646/django-models-to-calculate-discount) code was used as a basis for the sale information in the product model.
* [Timmy O'Mahony's](https://stackoverflow.com/questions/6195424/how-to-insert-a-checkbox-in-a-django-form) code was used and edited for the wishlist sales alert checkbox.
* [w3school's](https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp) code was used to hide the arrows on the quantity input boxes.

<br/>

### **Content**

Content for the website was made by Rossanne Hamilton.

<br/>

### **Media Used**

* [StockSnap's image](https://pixabay.com/photos/wall-picture-frame-display-interior-2558279/) on Pixabay was used for the background image of Starry Night and Water Lilies. 
* [Uroburos's image](https://pixabay.com/photos/image-painting-art-gallery-painter-1053852/) on Pixabay was used for the background image of the Mona Lisa. 
* [Uroburos's image](https://pixabay.com/photos/image-painting-piece-the-museum-1053849/) on Pixabay was used for the background image of The Scream. 
* [Counselling's image](https://pixabay.com/photos/oil-painting-picture-frame-492639/) on Pixabay was used for the background image of Ophelia. 
* [Romka's image](https://www.pexels.com/photo/a-single-gold-framed-painting-on-the-wall-2951525/) on Pexels was used for the background image of Dogs Playing Poker. 
* [Google Font Oranienbaum](https://fonts.google.com/specimen/Oranienbaum?preview.text=METROPOLIS&preview.text_type=custom&category=Serif) was used for the font on the Metropolis poster. 
* [Tim Mossholder's image](https://www.pexels.com/photo/white-and-black-strap-on-green-painted-wall-2096622/) on Pexels was used for the background image of Metropolis. 
* [Google Font's Metal Mania](https://fonts.google.com/specimen/Metal+Mania?preview.text=JAWS&preview.size=96&preview.text_type=custom&query=metal+mania) was used for the font on Jaws. 
* [Google Font's Piedra](https://fonts.google.com/specimen/Metal+Mania?preview.text=JAWS&preview.size=96&preview.text_type=custom&query=metal+mania) was used for the font on Hang in There. 
* [Olga Lioncat's image](https://www.pexels.com/photo/palm-leaves-near-the-yellow-wall-7245622/) on Pexels was used for the background image of Hang in There. (The colour was heavily edited.)
* [Cottonbro Studio's image](https://www.pexels.com/photo/man-in-white-crew-neck-shirt-4065136/) on Pexels was used for the background image of Le Chat Noir.
* [SHVETS Production's image](https://www.pexels.com/photo/red-and-blue-curling-stones-in-close-up-photography-7561421/) on Pexels was used for the background image of Rosie the Riveter. (The colour was heavily edited.)
* [Google Font's Dancing Script](https://fonts.google.com/specimen/Dancing+Script?category=Handwriting&preview.text=(eponymous)&preview.text_type=custom) was used for part of the logo's font. 
* [Google Font's Big Shoulders Stencil Text](https://fonts.google.com/specimen/Big+Shoulders+Stencil+Text?category=Handwriting&preview.text=BoscH&preview.text_type=custom) was used for part of the logo's font. 
* [Karolina Grabowska's image](https://www.pexels.com/photo/black-and-white-photo-frame-5978717/) on Pexels was used for the background image of Relativity. (The colour was edited.)
* [Google Font's Big Shoulders Text](https://fonts.google.com/specimen/Big+Shoulders+Text?query=Patric+King) was used for the text body.
* [9699186's image](https://pixabay.com/photos/frame-mockup-flatlay-plant-3681646/) on Pixabay was used for the background image of The Wounded Deer.
* [Eva Bronzini's image](https://www.pexels.com/photo/photo-of-a-blank-picture-frame-7967320/) on Pixabay was used for the background image of The Lovers II.

<br/>

### **Acknowledgements**

I would like to acknowledge the following people who helped me along the way in completing my fourth milestone project:

- My mentor Mitko Bachvarov for helpful feedback and sharing links for further learning.
- Chris Mugridge, Maya Irish, Skye Hillier-Milton, and Roman Rakic for user testing, encouragement, and feedback.
- Thomas Muat for helping me understand how the on_sale filter works in the nav bar.
</div>