import great_expectations as gx

context = gx.get_context()
batch = context.get_batch("s3://processed-data/")
batch.expect_column_values_to_not_be_null("user_id")
batch.validate()
