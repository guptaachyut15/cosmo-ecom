# Cosmo-ecom

## Description

This mini dummy ecom backend include apis for getting all the stored products and uploading a paticular order.

## Tech used

- FastApi
- MongoDb

## How to Run

1. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    ```
    or
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

5. **Run the application:**
   -Using Uvicorn
    ```bash
    uvicorn main:app --reload --port 8080
    ```
## Environment Variables

Before running the Zerodha Clone, ensure you have set the following environment variables in a `.env` file at the root of your project. These variables are crucial for the proper functioning of the application.

| Variable                  | Description                                                | Example Value                                      |
|---------------------------|------------------------------------------------------------|----------------------------------------------------|
| `MONGODB_CONNECTION_STRING`| The connection string for your MongoDB database.            | `mongodb://username:password@localhost:27017/` |

Make sure to replace the placeholder values with your actual configuration. Keeping sensitive information, such as secret keys and connection strings, secure is essential for the proper and secure functioning of the application.

The application should now be running locally. Access it through your web browser at http://localhost:8080.

### Requests can be triggered from here:
http://localhost:8080/docs

## Paths

### /products/

#### GET

- **Description**: Get all products
- **Parameters**:
  - `min_price` (query): Minimum price filter (Type: number, Default: null)
  - `max_price` (query): Maximum price filter (Type: number, Default: null)
  - `limit` (query): Number of items to return per page (Type: integer, Minimum: 1, Default: 10)
  - `offset` (query): Number of items to skip for pagination (Type: integer, Default: 0)
- **Responses**:
  - 200: Successful Response
  - 422: Validation Error
  - 500: Server Error

### /orders/

#### POST

- **Description**: Place an order
- **Request Body**:
  - Content Type: application/json
  - Schema: Order
  - Required: true
- **Responses**:
  - 200: Successful Response
  - 422: Validation Error
  - 500: Server Error

## Components

### Schemas

#### HTTPValidationError

- Properties:
  - `detail` (Type: array of ValidationError): Detail
- Type: object

#### Item

- Properties:
  - `productId` (Type: string): Product ID
  - `boughtQuantity` (Type: integer): Bought quantity
- Type: object

#### Order

- Properties:
  - `items` (Type: array of Item): Items
  - `totalAmount` (Type: integer): Total amount
  - `userAddress` (Type: UserAddress): User address
  - `createdOn` (Type: string, Format: date-time, Default: "2024-01-29T18:38:19.631102Z"): Created on
- Type: object

#### UserAddress

- Properties:
  - `city` (Type: string): City
  - `country` (Type: string): Country
  - `zipcode` (Type: integer): Zipcode
- Type: object

#### ValidationError

- Properties:
  - `loc` (Type: array of anyOf [string, integer]): Location
  - `msg` (Type: string): Message
  - `type` (Type: string): Error Type
- Type: object

