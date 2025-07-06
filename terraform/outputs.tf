output "instance_public_ip" {
  value = aws_instance.secure_notes.public_ip
}


output "rds_endpoint" {
  value = aws_db_instance.postgres.address
}
