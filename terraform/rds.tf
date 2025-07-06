resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "rds-subnet-group"
  subnet_ids = [] # You can skip this for default VPC
}

resource "aws_db_instance" "postgres" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "15.4"
  instance_class       = "db.t3.micro"
  db_name              = "securenotesdb"
  username             = "admin"
  password             = "SuperSecure123!" 

  publicly_accessible    = false         
  storage_encrypted      = true          
  backup_retention_period = 7           
  multi_az               = false

  skip_final_snapshot    = true         
  deletion_protection    = false  

  tags = {
    Name = "secure-notes-rds"
    Environment = "dev"
  }
}


