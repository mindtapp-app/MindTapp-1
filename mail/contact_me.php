<?php
require '../lib/phpmailer/PHPMailerAutoload.php';
require 'creds.php';

date_default_timezone_set('Etc/UTC');

// Check for empty fields
if(empty($_POST['name'])      ||
   empty($_POST['email'])     ||
   empty($_POST['phone'])     ||
   empty($_POST['message'])   ||
   !filter_var($_POST['email'],FILTER_VALIDATE_EMAIL))
   {
   echo "No arguments Provided!";
   return false;
   }


$name = strip_tags(htmlspecialchars($_POST['name']));
$email_address = strip_tags(htmlspecialchars($_POST['email']));
$phone = strip_tags(htmlspecialchars($_POST['phone']));
$message = strip_tags(htmlspecialchars($_POST['message']));
$company = strip_tags(htmlspecialchars($_POST['company']));
$jobTitle = strip_tags(htmlspecialchars($_POST['jobTitle']));

$email_subject = "Website Contact Form:  $name";
$email_body = "You have received a new message from your website contact form.\n\n"."Here are the details:\n\nName: $name\n\nCompany: $company\n\nJob Title: $jobTitle\n\nEmail: $email_address\n\nPhone: $phone\n\nMessage:\n$message";

$mail = new PHPMailer;
$mail->isSMTP();

$mail->SMTPDebug = 2;
$mail->Host = $SMTP;
$mail->Port = $SMTPport;
$mail->SMTPSecure = 'ssl';
$mail->SMTPAuth = true;
$mail->Username = $username;
$mail->Password = $password;
$mail->setFrom('website@mindtapp.com', 'First Last');
$mail->addAddress('mindtrainingapp@gmail.com', 'First Last');
$mail->Subject = $email_subject;
$mail->AltBody = $email_body;

if (!$mail->send()) {
    error_log("Mailer Error: " . $mail->ErrorInfo);
} else {
    error_log("Message sent!");
}

return true;
?>
