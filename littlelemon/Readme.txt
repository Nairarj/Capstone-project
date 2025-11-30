Little Lemon Restaurant API – Capstone Project
==============================================

This Django REST Framework project exposes APIs for the Little Lemon
restaurant. It includes:

- A static HTML home page
- Menu API
- Table booking API
- User registration and token-based authentication (Djoser + DRF tokens)

How to run the project
----------------------

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

   pip install -r requirements.txt

3. Make sure MySQL is running and that DATABASE settings in
   littlelemon/settings.py point to your MySQL instance.
4. Apply migrations:

   python manage.py migrate

5. Run the development server:

   python manage.py runserver

Then open http://127.0.0.1:8000/ in a browser or use Insomnia/Postman
to hit the endpoints listed below.

Static HTML page
----------------

This is used to verify that Django is serving static HTML content.

- GET `/restaurant/`
  - Renders the Little Lemon HTML home page (index.html).

Menu API
--------

These endpoints are defined in `restaurant/urls.py` and included under
the `/restaurant/` prefix in the project-level `urls.py`.

- GET `/restaurant/menu/`
  - List all menu items.

- POST `/restaurant/menu/`
  - Create a new menu item (send JSON body).

- GET `/restaurant/menu/<id>/`
  - Retrieve a single menu item by its ID.

- PUT `/restaurant/menu/<id>/`
  - Update a menu item.

- DELETE `/restaurant/menu/<id>/`
  - Delete a menu item.

Table Booking API
-----------------

The booking endpoints are provided by a DRF `DefaultRouter` that
registers the `BookingViewSet` under the route `tables`.

Base prefix: `/restaurant/booking/`

- GET `/restaurant/booking/tables/`
  - List all bookings.

- POST `/restaurant/booking/tables/`
  - Create a new booking.

- GET `/restaurant/booking/tables/<id>/`
  - Retrieve a single booking.

- PUT `/restaurant/booking/tables/<id>/`
  - Update an existing booking.

- DELETE `/restaurant/booking/tables/<id>/`
  - Delete a booking.

User registration & authentication
----------------------------------

Djoser endpoints are included under the `/auth/` prefix in the
project-level `urls.py`:

- POST `/auth/users/`
  - Register a new user.

- GET `/auth/users/me/`
  - Get the currently authenticated user's details (requires auth).

- POST `/auth/token/login/`
  - Obtain an auth token (send username and password).

- POST `/auth/token/logout/`
  - Revoke the auth token.

Additional DRF token endpoint (optional, if you want to test it):

- POST `/restaurant/api-token-auth/`
  - Obtain an auth token using DRF’s `obtain_auth_token` view.

Authentication notes
--------------------

- The booking API (`/restaurant/booking/tables/…`) is protected with
  `IsAuthenticated`.  
- Obtain a token using either `/auth/token/login/` or
  `/restaurant/api-token-auth/`, then in Insomnia set:

  Authorization: `Token <your-token>`

Testing with Insomnia
---------------------

Suggested flows for reviewers:

1. Visit `/restaurant/` in a browser to confirm the static HTML index
   page is served.
2. Use Insomnia to:
   - `POST /auth/users/` to create a new user.
   - `POST /auth/token/login/` to obtain a token.
   - With the token, `GET /restaurant/menu/` and `POST /restaurant/menu/`
     to create a new menu item.
   - `GET /restaurant/booking/tables/` (with token) and
     `POST /restaurant/booking/tables/` to create a booking.
   - `PUT` and `DELETE` on `/restaurant/booking/tables/<id>/` to verify
     full CRUD functionality.
