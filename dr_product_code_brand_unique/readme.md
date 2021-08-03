# DR Product Code Brand Unique

This module extends **OCA** module,  [product_code_unique](https://github.com/OCA/product-attribute/tree/14.0/product_code_unique).

It adds a constraint on the **internal reference** `default_code` and **brand** `product_brand_id` of the product `_inherit = "product.template"` to make it unique across the database.

## Usage
It depends on two module:
- product
- product_brand