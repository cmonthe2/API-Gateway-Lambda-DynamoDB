variable "region" {
  default = "us-east-1"
}

variable "lambda_function_name" {
  default = "UserHandlerFunction"
}

variable "dynamodb_table_name" {
  default = "users"
}
