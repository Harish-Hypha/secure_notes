variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "Name of the existing EC2 key pair"
  type        = string
}

variable "public_key_path" {
  description = "Path to your public key (.pem)"
  type        = string
}
