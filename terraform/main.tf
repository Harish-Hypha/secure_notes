resource "aws_key_pair" "deployer" {
  key_name   = var.key_name
  public_key = file(var.public_key_path)
}

resource "aws_security_group" "allow_web" {
  name        = "allow_web"
  description = "Allow HTTP (6000) access"

  ingress {
    from_port   = 6000
    to_port     = 6000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "secure_notes" {
  ami           = "ami-0f5ee92e2d63afc18"
  instance_type = var.instance_type
  key_name      = var.key_name

  vpc_security_group_ids = [aws_security_group.allow_web.id]

  tags = {
    Name = "secure-notes-app"
  }

  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install python3-pip -y
              EOF
}
